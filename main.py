from fastapi import FastAPI
from app.routes.item_routes import item_router
from app.routes.section_routes import section_router
from app.routes.modifier_routes import modifier_router
from app.config.config import engine
from app.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(section_router, prefix="/section", tags=["Section"])
app.include_router(item_router, prefix="/item", tags=["Items"])
app.include_router(modifier_router, prefix="/modifer", tags=["Modifier"])


