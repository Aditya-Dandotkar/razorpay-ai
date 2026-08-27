from sqlalchemy import Column, Integer, Float, String
from backend.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    amount = Column(Float)
    transaction_type = Column(String)