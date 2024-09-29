from fastapi import FastAPI
from admin import create_admin

from models import Art_type, Activity, User
from database import Session

app = FastAPI(title="AppName")
admin = create_admin(app)


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/art_type")
async def get_art_type(id: int):
    session = Session()
    art_type = session.query(Art_type).filter(Art_type.id == id).first()
    return {"Art Type": art_type.Name}


@app.get("/activity")
async def get_activity_by_artType(artType_id: int):
    session = Session()
    activity = session.query(Activity).filter(
        Activity.art_type_id == artType_id).all()
    return {"Activity": activity}
