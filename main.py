from fastapi import FastAPI
from admin import create_admin

from models import Art_type, Activity, User
from database import Session

app = FastAPI(title="AppName")
admin = create_admin(app)


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.post("/art_type")
async def get_art_type(id: int):
    session = Session()
    art_type = session.query(Art_type).filter(Art_type.id == id).first()
    return art_type


@app.post("/activity")
async def get_activity_by_artType(artType_id: int):
    session = Session()
    activity = session.query(Activity).filter(
        Activity.art_type_id == artType_id).all()
    return activity


@app.post("/all_activities")
async def get_all_activities():
    session = Session()
    activities = session.query(
        Activity, Art_type).filter(Activity.art_type_id == Art_type.id).all()
    return [{
        "id": activity.id,
        "name": activity.Name,
        "TimeDescription": activity.TimeDescription,
        "Location": activity.Location,
        "WorkHours": activity.WorkHours,
        "WorkForce": activity.WorkForce,
        "WorkForceBalance": activity.WorkForceBalance,
        "Description": activity.Description,
        "art_type": {
            "id": art_type.id,
            "name": art_type.Name
        }
    } for activity, art_type in activities]
