from src.schema.base import BaseModel, Optional

class SchemaBookTypeUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class SchemaBookType(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True