from flask import current_app as app
from flask import request,render_template
from .models import db, User,Role,Package,Booking
from flask_security import auth_required , roles_required , current_user
from datetime import datetime
from .task import add_together , download_csv
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
        profs.append({"id":prof.id ,  "name" : prof.name , "email" : prof.email})
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
@roles_required("professionl" )
def list_packs():
    packs = []
    
    for pack in current_user.packages:
        packs.append({ "id" : pack.id , "name" : pack.name , "price" : pack.price } )
    print(packs)
    return packs , 200

@app.route("/get-packages" , methods=["GET" ]) 
@auth_required("token")
@roles_required("customer" )
def get_packs():
    packs = []
    packages = Package.query.all()
    for pack in packages:
        packs.append({ "id" : pack.id , "name" : pack.name , "price" : pack.price } )
    
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
    

@app.route("/get-package" , methods=["GET"])
def get_package():
    id  = request.args.get("pack_id")
    pack =  Package.query.filter_by(id = id).first()
    p = {}
    if pack :
        p["id"] = pack.id
        p["name"] = pack.name
        p["price"] = pack.price
        p["bookings"] = []
        for booking in pack.bookings:
            p["bookings"].append({"id" : booking.id , "date" : datetime.strftime(booking.date ,"%d-%m-%Y") , "time" :booking.time.strftime("%H:%M") , 
                                  "customer_id" : booking.customer_id , "customer_name" : booking.customer.name ,
                                  "customer_email" : booking.customer.email, "status":booking.status })
            
        print(p)
        return p ,200   
    else:
        return {"message" : "package not found"} , 404
    

@app.route("/get-professional" , methods=["GET"])
def get_professional():
    prof_id= request.args.get("prof_id")
    prof = User.query.filter_by(id = prof_id).first()
    p = {}
    if prof : 
        p["id"] = prof.id,
        p["name"] = prof.name
        p["email"] = prof.email
        p["packages"] = []
        for pack in prof.packages:
            p["packages"].append({"id" : pack.id , "name" : pack.name , "price" :pack.price})

        return p , 200
    else:
        return {"message" : "professional Not found"}, 404
    

@app.route("/book",methods=["POST"])
@auth_required("token")
@roles_required("customer")
def book():
    pack_id = request.args.get("pack_id")
    date = request.json.get("date")
    time = request.json.get("time")
    print("d : " , date)
    print("t : " , time)
    pack = Package.query.filter_by(id= pack_id).first()
    if pack:
        new_booking = Booking(date = datetime.strptime(date , "%Y-%m-%d").date(),
                              time= datetime.strptime(time, "%H:%M").time() ,
                              customer_id = current_user.id , package_id = pack_id ,
                              prof_id=pack.user.id , status="Booked")
        db.session.add(new_booking)
        db.session.commit()
        return {"message" : "Package Booked Successfully"} , 200
    else : 
        return {"message" : "Package Doesn't Exist"} , 404


@app.route("/get-bookings" , methods=["GET"])
@auth_required("token")
@roles_required("customer")
def get_bookings():
    bookings = []
    for booking in current_user.created_bookings:
            bookings.append({"id" : booking.id , "date" : datetime.strftime(booking.date ,"%d-%m-%Y") , "time" :booking.time.strftime("%H:%M") , 
                                  "professional_id" : booking.prof_id , "professional_name" : booking.professional.name ,
                                  "professional_email" : booking.professional.email, "status":booking.status , "package_name" : booking.package.name })
    return bookings


@app.route("/search" , methods=["POST"])
@auth_required("token")
@roles_required("admin")
def search():
    query_type = request.json.get("query_type")
    query = request.json.get("query")

    if query_type=="cust": 
        cust_role = db.session.query(Role).filter_by(name = "customer").first()
        custs = []
        for cust in cust_role.users:
            if query in cust.name.lower() or cust.email.lower():
                custs.append({"name" : cust.name , "email" : cust.email})
        return custs , 200
    elif query_type == "prof":
        prof_role = db.session.query(Role).filter_by(name = "professionl").first()
        profs = []
        for prof in prof_role.users:
            if query in prof.name or query in prof.email :
                profs.append({"id":prof.id ,  "name" : prof.name , "email" : prof.email})
        print(profs)
        return profs , 200
    elif query_type=="pack":
        packs = []
        packages = Package.query.all()
        for pack in packages:
            if query in pack.name :
                packs.append({ "id" : pack.id , "name" : pack.name , "price" : pack.price } )
        
        return packs , 200
    else:
        return {"message" : "Wrong query type"} , 400
    

@app.route("/addnumber" , methods=["GET"])
def addnumber():
    a = request.args.get("a")
    b = request.args.get("b")
    result = add_together.delay(int(a) ,int( b))
    print(result.id)
    return {"message" : "task started" , "task_id" : result.id}


from celery.result import AsyncResult

@app.get("/result/<id>")
def task_result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    return {
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }


@app.route("/downloadcsv" , methods=["GET"])
@auth_required("token")
@roles_required("customer")
def customercsv():
    task = download_csv.delay(current_user.id)
    return {"message" : "csv export started" , "task_id" : task.id}