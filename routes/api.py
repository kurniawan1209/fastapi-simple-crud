from fastapi import APIRouter
from src.endpoints import book, book_type

router = APIRouter()
router.include_router(book.router)
router.include_router(book_type.router)