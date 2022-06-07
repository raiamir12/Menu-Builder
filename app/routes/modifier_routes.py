from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from app.config.config import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.modifier_schemas import ModifierSchema, Request, Response, RequestModifier
import app.crud.modifier_crud as modifier_crud 

modifier_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@modifier_router.post("/create")
async def create_modifier(request: RequestModifier, db: Session = Depends(get_db)):
    modifier_crud.create_modifier(db, modifier=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="modifier created successfully").dict(exclude_none=True)

   
@modifier_router.get("/")
async def get_modifiers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _modifiers = modifier_crud.get_modifier(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_modifiers)

@modifier_router.get("/{id}")
async def get_modifier(id=int, db: Session = Depends(get_db)):
    _modifiers = modifier_crud.get_modifier_by_id(db, modifier_id=id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_modifiers)

@modifier_router.patch("/update")
async def update_modifier(request: RequestModifier, db: Session = Depends(get_db)):
    _modifier = modifier_crud.update_modifier(db, modifier_id=request.parameter.id,
                             description=request.parameter.description
                            )
    return Response(status="Ok", code="200", message="Success update data", result=_modifier)


@modifier_router.delete("/{id}")
async def delete_modifier(id=int,  db: Session = Depends(get_db)):
    modifier_crud.remove_modifier(db, modifier_id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
