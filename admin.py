from sqladmin import Admin, ModelView
from database import engine, Session
from models import User, Activity, Art_type
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request


#This page will implement the authentication for your admin pannel
class AdminAuth(AuthenticationBackend):

    async def login(self, request: Request) -> bool:
        form = await request.form()
        studentID = form.get("username")
        password = form.get("password")
        session = Session()
        if not studentID or not password:
            return False
        query = session.query(User).filter(User.StudentID == studentID)
        if query.count() == 0:
            return False

        user = query.first()
        if user and password == user.Password:
            if user.is_admin:
                request.session.update({"token": user.StudentID})
                return True
        else:
            False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        return token is not None


# create a view for your models
class UsersAdmin(ModelView, model=User):
    column_list = ['id', 'StudentID', 'Name', 'is_admin']


class ActivityAdmin(ModelView, model=Activity):
    column_list = [
        'id', 'Name', 'TimeDescription', 'Location', 'WorkHours', 'WorkForce',
        'WorkForceBalance', 'Description', 'art_type_id'
    ]


class ArtTypeAdmin(ModelView, model=Art_type):
    column_list = ['id', 'Name']


# add the views to admin
def create_admin(app):
    authentication_backend = AdminAuth(secret_key="supersecretkey")
    admin = Admin(app=app,
                  engine=engine,
                  authentication_backend=authentication_backend)
    admin.add_view(UsersAdmin)
    admin.add_view(ActivityAdmin)
    admin.add_view(ArtTypeAdmin)

    return admin
