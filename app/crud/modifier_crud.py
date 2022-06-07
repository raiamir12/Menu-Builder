from sqlalchemy.orm import Session
from app.models.models import Modifiers
from app.schemas.modifier_schemas import ModifierSchema


def get_modifier(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Modifiers).offset(skip).limit(limit).all()


def get_modifier_by_id(db: Session, modifier_id: int):
    return db.query( Modifiers).filter( Modifiers.id == modifier_id).first()


def create_modifier(db: Session, modifier: ModifierSchema):
    _modifier =  Modifiers(description=modifier.description)
    db.add(_modifier)
    db.commit()
    db.refresh(_modifier)
    return _modifier


def remove_modifier(db: Session, modifier_id: int):
    _modifier = get_modifier_by_id(db=db, modifier_id=modifier_id)
    db.delete(_modifier)
    db.commit()


def update_modifier(db: Session, modifier_id: int, description:str):
    _modifier = get_modifier_by_id(db=db, modifier_id=modifier_id)

    _modifier.description = description
    db.commit()
    db.refresh(_modifier)
    return _modifier
