from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data Model
class Book(BaseModel):
    id: int
    title: str
    author: str

# Fake DB
books: List[Book] = [
    Book(id=1,title="Nirosh's New Book", author="Nirosh"),
    Book(id=2, title="Building APIs", author="Unknown")
]

# Root Endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Nirosh's Library API"}

# Getting all books - Endpoint
@app.get("/books",response_model=List[Book])
def get_books():
    return books

# Write an endpoint that takes a user ID and returns the specific book.
@app.get("/book/{book_id}",response_model=List[Book])
def get_book(target_id):
    result = [item for item in books if item['id'] == target_id]
    return result

#
@app.get("/book2/{book_id}",response_model=Book)
def get_book2(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"error":"Book not found"}
    #return next((b for b in books if b["id"] == book_id), None)