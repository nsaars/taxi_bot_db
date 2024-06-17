import pydantic
from pydantic import BaseModel


class Base(BaseModel):
    model_config = pydantic.ConfigDict(from_attributes=True)
