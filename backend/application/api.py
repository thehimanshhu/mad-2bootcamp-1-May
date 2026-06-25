from flask import current_app as app
from flask import request,render_template
from .models import db, User,Role,Package,Booking
from flask_security import auth_required , roles_required , current_user
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
def list_profs():
    prof_role = db.session.query(Role).filter_by(name = "professionl").first()
    print(current_user.name)
    print(current_user.email)
    profs = []
    for prof in prof_role.users:
        profs.append({"name" : prof.name , "email" : prof.email})
    print(profs)
    return profs , 200
    
@app.route("/list-customers" , methods=["GET" ]) 
@auth_required("token")
@roles_required("admin")
def list_custs():
    cust_role = db.session.query(Role).filter_by(name = "customer").first()
    custs = []
    for cust in cust_role.users:
        custs.append({"name" : cust.name , "email" : cust.email})
    print(custs)
    return custs , 200
    
@app.route("/list-packages" , methods=["GET" ]) 
@auth_required("token")
@roles_required("professionl")
def list_packs():
    packs = []
    print(current_user.name)
    print(current_user.email)
    for pack in current_user.packages:
        packs.append({ "id" : pack.id , "name" : pack.name , "price" : pack.price } )
    print(packs)
    return packs , 200


@app.route("/create-package" , methods=["POST"])
@auth_required("token")
@roles_required("professionl")
def create_pacage():
    name = request.json.get("name")
    price = request.json.get("price")
    if name and price : 
        pack = Package(name= name , price=price , prof_id = current_user.id )
        db.session.add(pack)
        db.session.commit()
        return {"message" : "Package Create Successfully"},200
    

    return {"message" : "Name and Price can't be empty"} ,400

@app.route("/delete-package" , methods=["DELETE"])
@auth_required("token")
@roles_required("professionl")
def delete_pacage():
    packageid = request.args.get("pack-id")
     
    pack = Package.query.filter_by(id = packageid).first()
    if pack : 
        if pack.prof_id == current_user.id:
            db.session.delete(pack)
            db.session.commit()
            return {"message" : "package deleted succesfully"} , 200
        else :
            return {"message" : "This package doesn't belong to You"} , 403
    else : 

        return {"message" : "Package not found"} ,404
    

