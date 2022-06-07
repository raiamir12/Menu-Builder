from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from app.config.config import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.section_schemas import SectionSchema, Request, Response, RequestSection
import app.crud.section_crud as section_crud

section_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@section_router.post("/create")
async def create_section(request: RequestSection, db: Session = Depends(get_db)):
    section_crud.create_section(db, section=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="section created successfully").dict(exclude_none=True)

   
@section_router.get("/")
async def get_sections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _sections = section_crud.get_section(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_sections)

@section_router.get("/{id}")
async def get_section(id=int, db: Session = Depends(get_db)):
    _sections = section_crud.get_section_by_id(db, section_id=id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_sections)

@section_router.patch("/update")
async def update_section(request: RequestSection, db: Session = Depends(get_db)):
    _section = section_crud.update_section(db, section_id=request.parameter.id,
                             name=request.parameter.name,description=request.parameter.description
                            )
    return Response(status="Ok", code="200", message="Success update data", result=_section)


@section_router.delete("/{id}")
async def delete_section(id=int,  db: Session = Depends(get_db)):
    section_crud.remove_section(db, section_id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
