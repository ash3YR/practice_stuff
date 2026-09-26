# import fastapi
# print(fastapi.__version__)
from fastapi import FastAPI, Request, Response
from mockdata import products
from dtos import productdto


app = (
    FastAPI()
)  # FastAPI class hai , aur app object hai jo FastAPI class ka instance hai


@app.get("/")  # decorator hai jo function ko route ke sath bind karta hai
def home():
    return "Welcome to FastAPI beti"


@app.get("/greet/{name}")  # path parameter
def greeting(name: str):
    return f"Hello, {name}!"


# Path Parameter: /products/{id} - id is a path parameter
# route for getting a specific product
@app.get("/products/{id}")
def get_product(id: int):
    for product in products:
        if product["id"] == id:
            return product

    return {"error": "Product not found"}


# Query Parameter: /products?name=Product 1 - name is a query parameter

# @app.get("/greet")
# def greeting2(name: str = "World" , age: int = 0):
#     return f"Hello, {name}! You are {age} years old."


# @app.get("/greet")
# def greet(request: Request):
#    query_params = dict(request.query_params)
#    print(query_params)
#    return f"Hello, {query_params.get('name', 'World')}! You are {query_params.get('age', 0)} years old."


@app.post("/products")  # route for creating a new product
def create_product(
    product_data: productdto,
):  # product is a parameter of type productDTO
    print(product_data)  # product object ko print kar raha hai

    product_data = (
        product_data.model_dump()
    )  # product object ko dictionary me convert kar raha hai
    products.append(
        product_data
    )  # product object ko products list me append kar raha hai            =----- temporary measuse hai as so far hum koi database use nhi kr rhe na

    return {
        "status": "successfully created product",
        "product": products,
    }  # product object ko retrn kar raha hai


@app.put("/products/{id}")  # route for updating a product
def updata_product(id: int, product_data: productdto):
    for product in products:
        if product["id"] == id:
            product.update(product_data.model_dump())
            return {"status": "successfully updated product", "product": product}

    return {"error": "Product not found"}


@app.delete("/products/{id}")  # route for deleting a product
def delete_product(id: int):
    for product in products:
        if product["id"] == id:
            products.remove(product)
            return {"status": "successfully deleted product", "product": product}

    return {"error": "Product not found"}
