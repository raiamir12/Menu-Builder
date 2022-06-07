from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from app.config.config import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.item_schemas import ItemSchema, Request, Response, RequestItem
import app.crud.item_crud as item_crud

item_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@item_router.post("/create")
async def create_Item(request: RequestItem, db: Session = Depends(get_db)):
    item_crud.create_item(db, item=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="item created successfully").dict(exclude_none=True)

   
@item_router.get("/")
async def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _items = item_crud.get_item(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_items)

@item_router.get("/{id}")
async def get_item(id=int, db: Session = Depends(get_db)):
    _items = item_crud.get_item_by_id(db, item_id=id)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_items)

@item_router.patch("/update")
async def update_item(request: RequestItem, db: Session = Depends(get_db)):
    _item = item_crud.update_item(db, item_id=request.parameter.id,
                             name=request.parameter.name,description=request.parameter.description,
                             price=request.parameter.price
                            )
    return Response(status="Ok", code="200", message="Success update data", result=_item)


@item_router.delete("/{id}")
async def delete_item(id=int,  db: Session = Depends(get_db)):
    item_crud.remove_item(db, item_id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
