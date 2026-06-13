from sqlalchemy import Column, Integer, String
from backend.core.database import Base

class Candidates(Base):
    __tablename__ = 'candidates'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    post = Column(String)
    YOE = Column(Integer)

