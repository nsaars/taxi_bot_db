from fastapi import APIRouter, Depends, HTTPException, status, Request
from typing import cast

from that_depends import Provide
from that_depends.providers import container_context

from app.models import models
from app.schemas import schemas
from app.repositories import repositories
from app.ioc import IOCContainer


ROUTER = APIRouter()

# Helper function to generate CRUD endpoints
def generate_crud_endpoints(model_name: str, schema, repo):
    model = getattr(models, model_name)
    schema_list = getattr(schemas, model_name + ("s" if not model_name.endswith('s') else "List"))
    schema_single = getattr(schemas, model_name + "Schema")
    repo_instance = getattr(repositories, repo)

    @ROUTER.get(f"/{model_name.lower()}s/", response_model=schema_list)
    @container_context()
    async def get_items(
            request: Request,
            repo: repo_instance = Depends(Provide[getattr(IOCContainer, f"{model_name.lower()}_repo")]),
    ) -> schema_list:
        query_params = request.query_params

        filters = {}
        for attr, value in query_params.items():
            attr_string = None
            op = None
            if '__' in attr:
                attr_string = attr
                attr, op = attr.split('__')
            print(attr_string, attr, op)
            if hasattr(model, attr):
                filters[attr_string or attr] = value
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid attribute: {attr}")

        objects = await repo.filter(filters=filters)
        if not objects:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{model_name}s are not found")
        return cast(schema_list, {f"{model_name.lower()}s": objects})

    @ROUTER.patch(f"/{model_name.lower()}s/{{item_id}}/", response_model=schema_single)
    @container_context()
    async def partial_update_item(
            item_id: int,
            data: schema_single,
            repo: repo_instance = Depends(Provide[getattr(IOCContainer, f"{model_name.lower()}_repo")]),
    ) -> schema_single:
        instance = await repo.get_by_id(item_id)
        if not instance:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{model_name} not found")

        update_data = data.dict(exclude_unset=True)
        await repo.update_attrs(instance, **update_data)
        await repo.save(instance)
        return instance

    @ROUTER.put(f"/{model_name.lower()}s/{{item_id}}/", response_model=schema_single)
    @container_context()
    async def update_item(
            item_id: int,
            data: schema_single,
            repo: repo_instance = Depends(Provide[getattr(IOCContainer, f"{model_name.lower()}_repo")]),
    ) -> schema_single:
        instance = await repo.get_by_id(item_id)
        if not instance:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{model_name} is not found")

        await repo.update_attrs(instance, **data.dict())
        await repo.save(instance)
        return cast(schema_single, instance)

    @ROUTER.post(f"/{model_name.lower()}s/", response_model=schema_single)
    @container_context()
    async def create_item(
            data: schema_single,
            repo: repo_instance = Depends(Provide[getattr(IOCContainer, f"{model_name.lower()}_repo")]),
    ) -> schema_single:
        instance = model(**data.dict())
        await repo.save(instance)
        return cast(schema_single, instance)

# Generate endpoints for each model
models_to_generate = [
    ("Driver", schemas.DriverSchema, "DriversRepository"),
    ("Admin", schemas.AdminSchema, "AdminsRepository"),
    ("Manager", schemas.ManagerSchema, "ManagersRepository"),
    ("Employee", schemas.EmployeeSchema, "EmployeesRepository"),
    ("Product", schemas.ProductSchema, "ProductsRepository"),
    ("Office", schemas.OfficeSchema, "OfficesRepository"),
    ("ManagersOffices", schemas.ManagersOfficesSchema, "ManagersOfficesRepository"),
    ("ProductsOffices", schemas.ProductsOfficesSchema, "ProductsOfficesRepository")
]

for model_name, schema, repo in models_to_generate:
    generate_crud_endpoints(model_name, schema, repo)
