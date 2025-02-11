from fastapi import APIRouter, HTTPException
from api.routes import books

router = APIRouter()
router.include_router(books.router, prefix="/books", tags=["books"])

@router.get("/api/v1/books/{book_id}")
async def get_book(book_id: int):
    """Fetch book details by ID."""
    # Ensure books is a dictionary for O(1) lookup, else adjust lookup method
    book = books.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]

# Rename router for correct import
api_router = router
