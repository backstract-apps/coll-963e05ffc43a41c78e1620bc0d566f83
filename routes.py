from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/login')
async def post_login(raw_data: schemas.PostLogin, db: Session = Depends(get_db)):
    try:
        return await service.post_login(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/orders/order_id')
async def get_orders_order_id(order_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_orders_order_id(db, order_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/orders/order_id/')
async def put_orders_order_id(raw_data: schemas.PutOrdersOrderId, db: Session = Depends(get_db)):
    try:
        return await service.put_orders_order_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/orders/order_id')
async def delete_orders_order_id(order_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_orders_order_id(db, order_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/orders/')
async def get_orders(db: Session = Depends(get_db)):
    try:
        return await service.get_orders(db)
    except ValueError as e:
        raise HTTPException(status_code=400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/products/')
async def get_products(db: Session = Depends(get_db)):
    try:
        return await service.get_products(db)
    except ValueError as e:
        raise HTTPException(status_code=400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/products/product_id')
async def get_products_product_id(product_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_products_product_id(db, product_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/products/')
async def post_products(raw_data: schemas.PostProducts, db: Session = Depends(get_db)):
    try:
        return await service.post_products(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/products/product_id/')
async def put_products_product_id(raw_data: schemas.PutProductsProductId, db: Session = Depends(get_db)):
    try:
        return await service.put_products_product_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/products/product_id')
async def delete_products_product_id(product_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_products_product_id(db, product_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/')
async def get_customers(db: Session = Depends(get_db)):
    try:
        return await service.get_customers(db)
    except ValueError as e:
        raise HTTPException(status_code=400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/customer_id')
async def get_customers_customer_id(customer_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_customers_customer_id(db, customer_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/customers/')
async def post_customers(raw_data: schemas.PostCustomers, db: Session = Depends(get_db)):
    try:
        return await service.post_customers(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/customers/customer_id/')
async def put_customers_customer_id(raw_data: schemas.PutCustomersCustomerId, db: Session = Depends(get_db)):
    try:
        return await service.put_customers_customer_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/customers/customer_id')
async def delete_customers_customer_id(customer_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_customers_customer_id(db, customer_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/orders/')
async def post_orders(raw_data: schemas.PostOrders, db: Session = Depends(get_db)):
    try:
        return await service.post_orders(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

