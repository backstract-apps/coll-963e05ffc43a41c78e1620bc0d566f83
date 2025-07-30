from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Orders(BaseModel):
    customer_id: Optional[int]=None
    product_id: Optional[int]=None
    quantity: int
    order_date: Optional[datetime.time]=None


class ReadOrders(BaseModel):
    customer_id: Optional[int]=None
    product_id: Optional[int]=None
    quantity: int
    order_date: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class Products(BaseModel):
    name: str
    price: Any
    in_stock: Optional[int]=None


class ReadProducts(BaseModel):
    name: str
    price: Any
    in_stock: Optional[int]=None
    class Config:
        from_attributes = True


class Customers(BaseModel):
    full_name: str
    email: str
    password: str
    created_at: Optional[datetime.time]=None


class ReadCustomers(BaseModel):
    full_name: str
    email: str
    password: str
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True




class PostLogin(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PutOrdersOrderId(BaseModel):
    order_id: Optional[int]=None
    customer_id: Optional[int]=None
    product_id: Optional[int]=None
    quantity: Optional[int]=None
    order_date: Optional[Any]=None

    class Config:
        from_attributes = True



class PostProducts(BaseModel):
    name: Optional[str]=None
    price: Optional[str]=None
    in_stock: Optional[int]=None

    class Config:
        from_attributes = True



class PutProductsProductId(BaseModel):
    product_id: Optional[int]=None
    name: Optional[str]=None
    price: Optional[str]=None
    in_stock: Optional[int]=None

    class Config:
        from_attributes = True



class PostCustomers(BaseModel):
    full_name: Optional[str]=None
    email: Optional[str]=None
    password: Optional[str]=None
    created_at: Optional[Any]=None

    class Config:
        from_attributes = True



class PutCustomersCustomerId(BaseModel):
    customer_id: Optional[int]=None
    full_name: Optional[str]=None
    email: Optional[str]=None
    password: Optional[str]=None
    created_at: Optional[Any]=None

    class Config:
        from_attributes = True



class PostOrders(BaseModel):
    customer_id: Optional[int]=None
    product_id: Optional[int]=None
    quantity: Optional[int]=None
    order_date: Optional[str]=None

    class Config:
        from_attributes = True

