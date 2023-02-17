from src.schema.base import BaseModel, Optional

class SchemaBook(BaseModel):
    title: str
    description: str
    type_id: str

    class Config:
        orm_mode = True

class SchemaBookUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    type_id: Optional[str]

    class Config:
        orm_mode = True