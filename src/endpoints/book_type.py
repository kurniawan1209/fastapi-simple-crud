from src.endpoints.base import APIRouter, DataNotFoundError, HTTPException, Optional, Query, db, and_
from src.models.book_type import ModelBookType
from src.schema.book_type import SchemaBookType, SchemaBookTypeUpdate
from datetime import datetime


router = APIRouter(
    prefix="/book-types",
    tags=["Book Types"]
)

@router.post("/create-book-type")
async def create_book_type(payload: SchemaBookType):
    """
    function to create book type record
    """
    try:
        new_type = ModelBookType(**payload.dict())
        db.session.add(new_type)
        db.session.commit()
        return {"status":"success"}
    except:
        raise HTTPException(status_code=500)


@router.get("/get-book-type")
async def get_book_types(type_id: Optional[str] = None, is_active: str = Query("y", description="Fill using y or n, if None then get all active record")):
    """
    function get book types. If the type_id parameter is None 
    then get all book types. But if not none then get 
    the detail book types based on parameter. And if is_active
    is None then get all types 
    """
    try:
        is_active = True if is_active == "y" or is_active is None else False
        if type_id:
            types = db.session.query(ModelBookType).filter(ModelBookType.type_id == type_id, ModelBookType.active_flag == is_active).all()
        else:
            types = db.session.query(ModelBookType).filter(ModelBookType.active_flag == is_active).all()
        if not types:
            raise DataNotFoundError
        return {"status": "success", "datas": types}
    except Exception as error:
        if isinstance(error, DataNotFoundError):
            raise HTTPException(status_code=404)
        raise HTTPException(status_code=500)


@router.put("/update-book-type/{pk}")
async def update_book_types(pk: str, payload: SchemaBookTypeUpdate):
    """
    update a book type based on user input
    """
    try:
        types = db.session.get(ModelBookType, pk)
        if types:
            for key, value in payload.dict().items():
                if value:
                    setattr(types, key, value)
            types.last_update_date = datetime.now()
            db.session.add(types)
            db.session.commit()
            return {"status": "success"}
        raise DataNotFoundError
    except Exception as error:
        if isinstance(error, DataNotFoundError):
            raise HTTPException(status_code=404)
        raise HTTPException(status_code=500)


@router.put("/delete-book-types/{pk}")
async def delete_book_types(pk: str):
    """
    there is no delete process in this function,
    it just updating active_flag to false
    """
    try:
        types = db.session.get(ModelBookType, pk)
        if types:
            types.active_flag = False
            types.inactive_date = datetime.now()
            db.session.add(types)
            db.session.commit()
            return {"status": "success"}
        raise DataNotFoundError
    except Exception as error:
        if isinstance(error, DataNotFoundError):
            raise HTTPException(status_code=404)
        raise HTTPException(status_code=500)