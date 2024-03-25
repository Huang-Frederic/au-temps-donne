from flask import jsonify
from flask_restful import Api
from dotenv import load_dotenv, find_dotenv
import os

from database.db import db, create_database

# Import Controllers
from controller.user import *
from controller.event import *
from controller.type import *
from controller.role import *
from controller.auth import *
from controller.location import *
from controller.category import *
from controller.food import *
from controller.package import *


# Import Models
from model.user import User
from model.event import Event
from model.role import Role
from model.type import Type
from model.location import Location
from model.category import Category
from model.food import Food
from model.package import Package

from app import app


# API Routes

api = Api(app)
prefix = "/api"
api.add_resource(UserListController, f'{prefix}/user')
api.add_resource(UserPageController, f'{prefix}/user/page/<int:page>')
api.add_resource(UserSearchController, f'{prefix}/user/page/<int:page>/search/<string:search>')
api.add_resource(UserController, f'{prefix}/user/<int:user_id>')

api.add_resource(UserIsRoleController, f'{prefix}/user/<int:user_id>/role/<int:role_id>')
api.add_resource(UserParticipatesEventController, f'{prefix}/user/<int:user_id>/event/<int:event_id>')

api.add_resource(EventController, f'{prefix}/event/<int:event_id>')
api.add_resource(EventListController, f'{prefix}/event')
api.add_resource(EventPageController, f'{prefix}/event/page/<int:page>')

api.add_resource(TypeListController, f'{prefix}/type')
api.add_resource(TypeController, f'{prefix}/type/<int:type_id>')

api.add_resource(RoleListController, f'{prefix}/role')
api.add_resource(RoleController, f'{prefix}/role/<int:role_id>')

api.add_resource(LocationListController, f'{prefix}/location')
api.add_resource(LocationController, f'{prefix}/location/<int:location_id>')

api.add_resource(CategoryListController, f'{prefix}/category')
api.add_resource(CategoryController, f'{prefix}/category/<int:category_id>')

api.add_resource(FoodController, f'{prefix}/food/<int:food_id>')
api.add_resource(FoodListController, f'{prefix}/food')
api.add_resource(FoodPageController, f'{prefix}/food/page/<int:page>')

api.add_resource(PackageController, f'{prefix}/package/<int:package_id>')
api.add_resource(PackageListController, f'{prefix}/package')
api.add_resource(PackagePageController, f'{prefix}/package/page/<int:page>')

api.add_resource(RegisterController, f'{prefix}/register')
api.add_resource(LoginController, f'{prefix}/login')
api.add_resource(ProtectedController, f'{prefix}/protected')
api.add_resource(RefreshTokenController, f'{prefix}/token/refresh')


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    create_database()
    db.init_app(app)
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run(debug=True)
