from fastapi import FastAPI, Query
app = FastAPI()
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id":item_id}

# What Are Query Parameters?
# They are values you pass after a question mark (?) in the URL.
# Query parameters = filters.
@app.get("/products")
def get_products(category: str=None, limit: int=None):
    return {
        "category" : category,
        "limit": limit
    }

@app.get("/users/{user_id}")
def get_user(user_id: int, active: bool=True):
    return {
        "user_id": user_id,
        "active": active
    }

@app.get("/books/{book_id}")
def get_book(book_id : int, author:str=None, available:bool=True):
    return {
        "book_id":book_id,
        "author": author,
        "available": available
    }

@app.get("/products/{product_id}")
def get_pro(
    product_id:int, 
    discount:float = Query(0, ge=0, le=50), 
    in_stock:bool=True, 
    quantity:int=Query(1, ge=1)
    ):
    return {
        "product_id": product_id,
        "discount": discount,
        "in_stock": in_stock,
        "quantity": quantity
    }