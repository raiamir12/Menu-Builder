from sqlalchemy import  Column, Integer, String,ForeignKey
from app.config.config import Base

class Section(Base):
    __tablename__ ="Section"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description=Column(String)
    # item_id = Column(Integer, ForeignKey('Item.id'))

class Item(Base):

    __tablename__ ="Item"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description=Column(String)
    price=Column(String)
    #One to One
    #One to Many  
    #Many to One
    # modifier_id = Column(Integer, ForeignKey('Modifiers.id'))  

class Modifiers(Base):

    __tablename__ ="Modifiers"

    id = Column(Integer, primary_key=True, index=True)
    description=Column(String)