from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin , RoleMixin
db = SQLAlchemy()

class User(db.Model , UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String , nullable = False)
    email = db.Column(db.String , nullable = False , unique = True)
    password = db.Column(db.String , nullable = False)
    active = db.Column(db.String , nullable = False)
    mobile = db.Column(db.String , nullable = True)
    fs_uniquifier = db.Column(db.String, unique=True , nullable = False)
    roles = db.relationship("Role" ,secondary = "user_roles")


class Role(db.Model, RoleMixin ):
    id =db.Column(db.Integer , primary_key = True )
    name = db.Column(db.String , nullable = False)
    desc = db.Column(db.String , nullable = False)


class UserRoles(db.Model):
    __tablename__ = "user_roles"
    id = db.Column(db.Integer , primary_key = True )
    role_id = db.Column(db.String , db.ForeignKey("role.id"))
    user_id = db.Column(db.String , db.ForeignKey("user.id"))


class Package(db.Model):
    id = db.Column(db.Integer , primary_key = True )
    name = db.Column(db.String , nullable = False)
    price = db.Column(db.Integer , nullable= False)
    prof_id= db.Column(db.Integer ,db.ForeignKey("user.id"))
    bookings = db.relationship("Booking" )

class Booking(db.Model):
    id = db.Column(db.Integer , primary_key = True )
    date = db.Column(db.Date , nullable = False)
    time = db.Column(db.Time , nullable = False)
    price = db.Column(db.Integer , nullable= False)
    package_id = db.Column(db.Integer ,db.ForeignKey("package.id"))
    prof_id= db.Column(db.Integer ,db.ForeignKey("user.id"))
    customer_id = db.Column(db.Integer ,db.ForeignKey("user.id"))

