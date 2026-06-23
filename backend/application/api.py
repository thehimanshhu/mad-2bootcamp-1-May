from flask import current_app as app
from flask import request
from .models import db, User
from flask_security import auth_required , roles_required
@app.route("/")
def home():
    return "Hello"


@app.route("/login" , methods=["POST"])
def login():
    email = request.json.get("email")
    pwd = request.json.get("pass")

    user = User.query.filter_by(email=email).first()
    if user:
        if user.password == pwd:
            return {"message" :"Login Successful" , "role" : user.roles[0].name ,"token" :user.get_auth_token() }
        else: 
            return {"message" : "Incorrect Password"}
    else:
        return {"message" : "Email doesn't exist"}
    
@app.route("/admin/dashboard" , methods=["GET" ]) 
@auth_required("token")
@roles_required("admin")
def admin_dashboard():
    return {"message" : "welcome to admin dashboard"}