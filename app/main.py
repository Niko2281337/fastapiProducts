from fastapi import FastAPI
from datetime import datetime
from typing import Optional
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn
app = FastAPI()

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]


@app.get("/product/{product_id}")
async def get_product(product_id: int):
    for product in sample_products:
        if product["product_id"] == product_id:
            return product
        else:
            return {"message": f"Product with id {product_id} not found"}
        

@app.get("/products/search")
async def search_products(keyword: str, category: Optional[str] = None, limit: Optional[int] = 10):
    lst = []
    for product in sample_products:
        if keyword in product["name"] and (category is None or product["category"] == category):
            lst.append(product)
            if len(lst) == limit:
                return lst
    return lst




if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )