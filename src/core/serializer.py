from pydantic import BaseModel, ConfigDict


class BaseSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)
