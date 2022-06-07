from sqlalchemy.orm import Session
from app.models.models import Section
from app.schemas.section_schemas import SectionSchema


def get_section(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Section).offset(skip).limit(limit).all()


def get_section_by_id(db: Session, section_id: int):
    return db.query(Section).filter( Section.id == section_id).first()


def create_section(db: Session, section: SectionSchema):
    _section =  Section(name=section.name)
    db.add(_section)
    db.commit()
    db.refresh(_section)
    return _section


def remove_section(db: Session, section_id: int):
    _section = get_section_by_id(db=db, section_id=section_id)
    db.delete(_section)
    db.commit()


def update_section(db: Session, section_id: int, name: str, description:str):
    _section = get_section_by_id(db=db, section_id=section_id)

    _section.name = name
    _section.price = price
    _section.description = description

    db.commit()
    db.refresh(_section)
    return _section
