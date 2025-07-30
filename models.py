from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID, LargeBinary, text
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Orders(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True, autoincrement=True )
    customer_id = Column(Integer, primary_key=False )
    product_id = Column(Integer, primary_key=False )
    quantity = Column(Integer, primary_key=False )
    order_date = Column(Time, primary_key=False )


class Products(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, autoincrement=True )
    name = Column(String, primary_key=False )
    price = Column(String, primary_key=False )
    in_stock = Column(Integer, primary_key=False )


class Customers(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True, autoincrement=True )
    full_name = Column(String, primary_key=False )
    email = Column(String, primary_key=False )
    password = Column(String, primary_key=False )
    created_at = Column(Time, primary_key=False )


