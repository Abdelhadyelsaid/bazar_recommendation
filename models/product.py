from pydantic import BaseModel

class Product(BaseModel):
    id: str
    name: str
    description: str
    mainImage: str
    price: float