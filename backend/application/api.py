from flask import current_app as app
from flask import request,render_template
from .models import db, User,Role
from flask_security import auth_required , roles_required
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login" , methods=["POST"])
def login():
    email = request.json.get("email")
    pwd = request.json.get("password")

    user = User.query.filter_by(email=email).first()
    if user:
        if user.password == pwd:
            return {"message" :"Login Successful" , "role" : user.roles[0].name ,"token" :user.get_auth_token() },200
        else: 
            return {"message" : "Incorrect Password"}, 401
    else:
        return {"message" : "Email doesn't exist"},404
    

@app.route("/register" , methods=["POST"])
def register():
    email = request.json.get("email")
    pwd = request.json.get("password")
    name = request.json.get("name")
    role = request.json.get("role")
    ds= app.security.datastore
    if role == "cust":
        if not ds.find_user(email=email):
            ds.create_user(email = email , name = name ,  password = pwd, roles =["customer"])
            db.session.commit()
            return {"message" : "Account Create Successfully" } , 200
        else: 
            return {"message" : "email Already Exist"} , 409 
    if role =="prof" :
        if not ds.find_user(email=email):
            ds.create_user(email = email , name = name ,  password = pwd, roles =["professional"])
            db.session.commit()
            return {"message" : "Account Create Successfully" } , 200
        else: 
            return {"message" : "email Already Exist"} , 409 

    else : 
        return {"message" : "Worng Selection, Please Choose Correct Role."} , 400


@app.route("/list-professionals" , methods=["GET" ]) 
@auth_required("token")
@roles_required("admin")
def admin_dashboard():
    prof_role = db.session.query(Role).filter_by(name = "professionl").first()
    profs = []
    for prof in prof_role.users:
        profs.append({"name" : prof.name , "email" : prof.email})

    return profs
    
     