from sqlalchemy.orm import Session
from app.models.models import Item
from app.schemas.item_schemas import ItemSchema


def get_item(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def get_item_by_id(db: Session, item_id: int):
    return db.query( Item).filter( Item.id == item_id).first()


def create_item(db: Session, item: ItemSchema):
    _item =  Item(name=item.name, description=item.description,price=item.price)
    db.add(_item)
    db.commit()
    db.refresh(_item)
    return _item


def remove_item(db: Session, item_id: int):
    _item = get_item_by_id(db=db, item_id=item_id)
    db.delete(_item)
    db.commit()


def update_item(db: Session, item_id: int, name: str, description:str,price :str):
    _item = get_item_by_id(db=db, item_id=item_id)

    _item.name = name
    _item.price = price
    _item.description = description

    db.commit()
    db.refresh(_item)
    return _item
