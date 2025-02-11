from fastapi import APIRouter, HTTPException

from api.routes import books

router = APIRouter()
router.include_router(books.router, prefix="/books", tags=["books"])

@router.get("/api/v1/books/{book_id}")
async def get_book(book_id: int):
    """Fetch book details by ID."""
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]

# Rename router to api_router for correct import
api_router = router