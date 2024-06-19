from fastapi import APIRouter, Depends, HTTPException, status, Request
from typing import cast

from pydantic import BaseModel
from sqlalchemy import Integer, Float, Double, Boolean
from that_depends import Provide
from that_depends.providers import container_context

import models
import schemas
from repositories import repositories
from ioc import IOCContainer

ROUTER = APIRouter()


class DeleteResponse(BaseModel):
    status: str
    message: str


def get_type(sql_type):
    if isinstance(sql_type, Integer):
        return int
    if isinstance(sql_type, Float) or isinstance(sql_type, Double):
        return float
    if isinstance(sql_type, Boolean):
        return bool
    return str


def get_filters(query_params, model):
    filters = {}
    for attr, value in query_params.items():

        attr_string = None
        if '__' in attr:
            attr_string = attr
            attr = attr.split('__')[0]

        if hasattr(model, attr):
            value = get_type(model.__dict__[attr].type)(value)

            filters[attr_string or attr] = value
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid attribute: {attr}")

    return filters


def generate_crud_endpoints(model_name: str, schema_view_name: str = None, schema_create_name: str = None,
                            schema_update_name: str = None, schema_list_name: str = None,
                            repo_instance_name: str = None, repo_lower_name: str = None, url: str = None):
    model = getattr(models, model_name)

    if schema_view_name is None:
        schema_view_name = model_name
    if schema_create_name is None:
        schema_create_name = model_name + "Create"
    if schema_update_name is None:
        schema_update_name = model_name + "Update"
    if schema_list_name is None:
        schema_list_name = model_name + "s"
    if repo_instance_name is None:
        repo_instance_name = model_name + "Repository"
    if repo_lower_name is None:
        repo_lower_name = f"{model_name.lower()}_repo"
    if url is None:
        url = f"{model_name.lower()}s"

    schema_view = getattr(schemas, schema_view_name)
    schema_create = getattr(schemas, schema_create_name)
    schema_update = getattr(schemas, schema_update_name)
    schema_list = getattr(schemas, schema_list_name)
    repo_instance = getattr(repositories, repo_instance_name)

    @ROUTER.get(f"/{url}/", response_model=schema_list)
    @container_context()
    async def get_items(
            request: Request,
            repo: repo_instance = Depends(Provide[getattr(IOCContainer, repo_lower_name)]),
    ) -> schema_list:
        print("GET")
        filters = get_filters(request.query_params, model)
        objects = await repo.filter(filters=filters)

        if not objects:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{model_name}s are not found")
        return cast(schema_list, {url: objects})

    @ROUTER.post(f"/{url}/", response_model=schema_view)
    @container_context()
    async def create_item(
            data: schema_create,
            repo: repo_instance = Depends(Provide[getattr(IOCContainer, repo_lower_name)]),
    ) -> schema_view:
        print("POST")
        
        instance = model(**data.dict())
        await repo.save(instance)
        return cast(schema_view, instance)

    @ROUTER.patch(f"/{url}/{{item_id}}/", response_model=schema_view)
    @container_context()
    async def partial_update_item(
            item_id: int,
            data: schema_update,
            repo: repo_instance = Depends(Provide[getattr(IOCContainer, repo_lower_name)]),
    ) -> schema_view:
        instance = await repo.get_by_id(item_id)
        if not instance:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{model_name} not found")

        update_data = data.dict(exclude_unset=True)
        await repo.update_attrs(instance, **update_data)
        await repo.save(instance)
        return instance

    @ROUTER.delete(f"/{url}/", response_model=DeleteResponse)
    @container_context()
    async def delete_items(
            request: Request,
            repo: repo_instance = Depends(Provide[getattr(IOCContainer, repo_lower_name)]),
    ) -> DeleteResponse:
        filters = get_filters(request.query_params, model)
        objects = await repo.filter(filters=filters)

        if not objects:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{model_name}s are not found")

        for obj in objects:
            await repo.delete(obj)

        return DeleteResponse(status="success", message=f"Deleted {len(objects)} {model_name}(s)")


# Generate endpoints for each model
models_to_generate = [
    ("User",),
    ("Driver",),
    ("Admin",),
    ("Manager",),
    ("Employee",),
    ("Product",),
    ("Office",),
    ("ProductsOffices", None, None, None, "ProductsOfficesList", None, "products_offices_repo", "products_offices"),
    ("Cart",),
    ("CartsProducts", None, None, None, "CartsProductsList", None, "carts_products_repo", "carts_products"),
    ("Settings", None, None, None, "SettingsList", None, "settings_repo", "settings"),
    ("State", None, None, None, "States", None, "state_repo", "states"),

]

for args in models_to_generate:
    generate_crud_endpoints(*args)
