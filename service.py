from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def post_login(db: Session, raw_data: schemas.PostLogin):
    email: str = raw_data.email
    password: str = raw_data.password

    query = db.query(models.Customers)
    query = query.filter(
        and_(models.Customers.email == email, models.Customers.password == password)
    )

    login_customer = query.first()

    login_customer = (
        (
            login_customer.to_dict()
            if hasattr(login_customer, "to_dict")
            else vars(login_customer)
        )
        if login_customer
        else login_customer
    )

    try:
        is_exist_login = bool(login_customer)
        is_true = True
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    is_As: bool = is_true

    if is_true == is_exist_login:

        bs_jwt_payload = {
            "exp": int(
                (
                    datetime.datetime.utcnow() + datetime.timedelta(seconds=100000)
                ).timestamp()
            ),
            "data": login_customer,
        }

        jwt_secret_keys_login = jwt.encode(
            bs_jwt_payload,
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
            algorithm="HS256",
        )

    else:

        raise HTTPException(status_code=401, detail="user does not exist.")
    res = {
        "login_record": login_record,
    }
    return res


async def get_orders_order_id(db: Session, order_id: int):

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.order_id == order_id))

    orders_one = query.first()

    orders_one = (
        (orders_one.to_dict() if hasattr(orders_one, "to_dict") else vars(orders_one))
        if orders_one
        else orders_one
    )

    res = {
        "orders_one": orders_one,
    }
    return res


async def put_orders_order_id(db: Session, raw_data: schemas.PutOrdersOrderId):
    order_id: int = raw_data.order_id
    customer_id: int = raw_data.customer_id
    product_id: int = raw_data.product_id
    quantity: int = raw_data.quantity
    order_date: datetime.datetime = raw_data.order_date

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.order_id == order_id))
    orders_edited_record = query.first()

    if orders_edited_record:
        for key, value in {
            "order_id": order_id,
            "quantity": quantity,
            "order_date": order_date,
            "product_id": product_id,
            "customer_id": customer_id,
        }.items():
            setattr(orders_edited_record, key, value)

        db.commit()
        db.refresh(orders_edited_record)

        orders_edited_record = (
            orders_edited_record.to_dict()
            if hasattr(orders_edited_record, "to_dict")
            else vars(orders_edited_record)
        )
    res = {
        "orders_edited_record": orders_edited_record,
    }
    return res


async def delete_orders_order_id(db: Session, order_id: int):

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.order_id == order_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        orders_deleted = record_to_delete.to_dict()
    else:
        orders_deleted = record_to_delete
    res = {
        "orders_deleted": orders_deleted,
    }
    return res


async def get_orders(db: Session):

    query = db.query(models.Orders)

    orders_all = query.all()
    orders_all = (
        [new_data.to_dict() for new_data in orders_all] if orders_all else orders_all
    )
    res = {
        "orders_all": orders_all,
    }
    return res


async def get_products(db: Session):

    query = db.query(models.Products)

    products_all = query.all()
    products_all = (
        [new_data.to_dict() for new_data in products_all]
        if products_all
        else products_all
    )
    res = {
        "products_all": products_all,
    }
    return res


async def get_products_product_id(db: Session, product_id: int):

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.product_id == product_id))

    products_one = query.first()

    products_one = (
        (
            products_one.to_dict()
            if hasattr(products_one, "to_dict")
            else vars(products_one)
        )
        if products_one
        else products_one
    )

    res = {
        "products_one": products_one,
    }
    return res


async def post_products(db: Session, raw_data: schemas.PostProducts):
    name: str = raw_data.name
    price: str = raw_data.price
    in_stock: int = raw_data.in_stock

    record_to_be_added = {"name": name, "price": price, "in_stock": in_stock}
    new_products = models.Products(**record_to_be_added)
    db.add(new_products)
    db.commit()
    db.refresh(new_products)
    products_inserted_record = new_products.to_dict()

    res = {
        "products_inserted_record": products_inserted_record,
    }
    return res


async def put_products_product_id(db: Session, raw_data: schemas.PutProductsProductId):
    product_id: int = raw_data.product_id
    name: str = raw_data.name
    price: str = raw_data.price
    in_stock: int = raw_data.in_stock

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.product_id == product_id))
    products_edited_record = query.first()

    if products_edited_record:
        for key, value in {
            "name": name,
            "price": price,
            "in_stock": in_stock,
            "product_id": product_id,
        }.items():
            setattr(products_edited_record, key, value)

        db.commit()
        db.refresh(products_edited_record)

        products_edited_record = (
            products_edited_record.to_dict()
            if hasattr(products_edited_record, "to_dict")
            else vars(products_edited_record)
        )
    res = {
        "products_edited_record": products_edited_record,
    }
    return res


async def delete_products_product_id(db: Session, product_id: int):

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.product_id == product_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        products_deleted = record_to_delete.to_dict()
    else:
        products_deleted = record_to_delete
    res = {
        "products_deleted": products_deleted,
    }
    return res


async def get_customers(db: Session):

    query = db.query(models.Customers)

    customers_all = query.all()
    customers_all = (
        [new_data.to_dict() for new_data in customers_all]
        if customers_all
        else customers_all
    )
    res = {
        "customers_all": customers_all,
    }
    return res


async def get_customers_customer_id(db: Session, customer_id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.customer_id == customer_id))

    customers_one = query.first()

    customers_one = (
        (
            customers_one.to_dict()
            if hasattr(customers_one, "to_dict")
            else vars(customers_one)
        )
        if customers_one
        else customers_one
    )

    res = {
        "customers_one": customers_one,
    }
    return res


async def post_customers(db: Session, raw_data: schemas.PostCustomers):
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    password: str = raw_data.password
    created_at: datetime.datetime = raw_data.created_at

    record_to_be_added = {
        "email": email,
        "password": password,
        "full_name": full_name,
        "created_at": created_at,
    }
    new_customers = models.Customers(**record_to_be_added)
    db.add(new_customers)
    db.commit()
    db.refresh(new_customers)
    customers_inserted_record = new_customers.to_dict()

    res = {
        "customers_inserted_record": customers_inserted_record,
    }
    return res


async def put_customers_customer_id(
    db: Session, raw_data: schemas.PutCustomersCustomerId
):
    customer_id: int = raw_data.customer_id
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    password: str = raw_data.password
    created_at: datetime.datetime = raw_data.created_at

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.customer_id == customer_id))
    customers_edited_record = query.first()

    if customers_edited_record:
        for key, value in {
            "email": email,
            "password": password,
            "full_name": full_name,
            "created_at": created_at,
            "customer_id": customer_id,
        }.items():
            setattr(customers_edited_record, key, value)

        db.commit()
        db.refresh(customers_edited_record)

        customers_edited_record = (
            customers_edited_record.to_dict()
            if hasattr(customers_edited_record, "to_dict")
            else vars(customers_edited_record)
        )
    res = {
        "customers_edited_record": customers_edited_record,
    }
    return res


async def delete_customers_customer_id(db: Session, customer_id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.customer_id == customer_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        customers_deleted = record_to_delete.to_dict()
    else:
        customers_deleted = record_to_delete
    res = {
        "customers_deleted": customers_deleted,
    }
    return res


async def post_orders(db: Session, raw_data: schemas.PostOrders):
    customer_id: int = raw_data.customer_id
    product_id: int = raw_data.product_id
    quantity: int = raw_data.quantity
    order_date: str = raw_data.order_date

    record_to_be_added = {
        "quantity": quantity,
        "order_date": order_date,
        "product_id": product_id,
        "customer_id": customer_id,
    }
    new_orders = models.Orders(**record_to_be_added)
    db.add(new_orders)
    db.commit()
    db.refresh(new_orders)
    orders_inserted_record = new_orders.to_dict()

    res = {
        "orders_inserted_record": orders_inserted_record,
    }
    return res
