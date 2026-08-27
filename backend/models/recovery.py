from sqlalchemy import Column, Integer, String
from backend.database import Base

class Recovery(Base):
    __tablename__ = "recoveries"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    action = Column(String)
    result = Column(String)