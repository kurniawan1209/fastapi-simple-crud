from datetime import datetime
from src.endpoints.base import *
from src.models.book import ModelBook
from src.schema.book import SchemaBook, SchemaBookUpdate

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.post("/create-book")
async def create_book(payload: SchemaBook):
    """
    function to create new book
    """
    try:
        new_book = ModelBook(**payload.dict())
        db.session.add(new_book)
        db.session.commit()
        return {"status": "success"}
    except Exception as err:
        print("Exception =", err)
        raise HTTPException(status_code=500)


@router.get("/get-book")
async def get_books(book_id: Optional[str] = None, is_active: str = Query("y", description="Fill using y or n, if None then get all active record")):
    """
    function get books. If the type_id parameter is None 
    then get all books. But if not none then get 
    the detail book based on parameter. And if is_active
    is None then get all books 
    """
    try:
        is_active = True if is_active.lower() == "y" or is_active is None else False
        if book_id:
            books = db.session.query(ModelBook).filter(ModelBook.book_id == book_id, ModelBook.active_flag == is_active).all()
        else:
            books = db.session.query(ModelBook).filter(ModelBook.active_flag == is_active).all()
        if not books:
            raise DataNotFoundError
        return {"status": "success", "datas": books}
    except Exception as error:
        if isinstance(error, DataNotFoundError):
            raise HTTPException(status_code=404)
        raise HTTPException(status_code=500)


@router.put("/update-book/{pk}")
async def update_book(pk: str, payload: SchemaBookUpdate):
    """
    update a book based on use input
    """
    try:
        if pk:
            book = db.session.get(ModelBook, pk)
            if not book:
                raise DataNotFoundError
            for key, value in payload.dict().items():
                if value:
                    setattr(book, key, value)
            book.last_update_date = datetime.now()
            db.session.add(book)
            db.session.commit()
            return {"status": "success"}
    except Exception as error:
        if isinstance(error, DataNotFoundError):
            raise HTTPException(status_code=404)
        raise HTTPException(status_code=500)


@router.put("/delete-book/{pk}")
async def delete_book(pk: str):
    """
    there is no delete process in this function,
    it just updating active_flag to false
    """
    try:
        book = db.session.get(ModelBook, pk)
        if not book:
            raise DataNotFoundError
        book.active_flag = False
        book.inactive_date = datetime.now()
        db.session.add(book)
        db.session.commit()
        return {"status": "success"}
    except Exception as error:
        if isinstance(error, DataNotFoundError):
            raise HTTPException(status_code=404)
        raise HTTPException(status_code=500)