from flask import current_app as app
from .models import db , User , Role , UserRoles,Package,Booking
from datetime import datetime

with app.app_context():
    db.create_all()

    ds = app.security.datastore

    ds.find_or_create_role(name = "admin" , desc = "superuser")
    ds.find_or_create_role(name="professionl" , desc="serviceprofessional")
    ds.find_or_create_role(name="customer" , desc="user")
    db.session.commit()

    if not ds.find_user(email="admin@gmail.com") : 
        ds.create_user(email="admin@gmail.com" , name="admin" , password="pass" ,active="active", roles=["admin"])
    if not ds.find_user(email="prof1@gmail.com") : 
        ds.create_user(email="prof1@gmail.com" , name="prof1" , password="pass" ,active="active", roles=["professionl"])
    if not ds.find_user(email="prof2@gmail.com") : 
        ds.create_user(email="prof2@gmail.com" , name="prof2" , password="pass" ,active="active", roles=["professionl"])
    if not ds.find_user(email="user1@gmail.com") : 
        ds.create_user(email="user1@gmail.com" , name="user1" , password="pass" ,active="active", roles=["customer"])
    if not ds.find_user(email="user2@gmail.com") : 
        ds.create_user(email="user2@gmail.com" , name="user2" , password="pass" ,active="active", roles=["customer"])
    
    
    db.session.commit()

    if Package.query.count() ==0 :
        pack1= Package(name="Past Control" , price = 500 , prof_id=2)
        pack2= Package(name="Sofa Cleaning" , price = 200 , prof_id=2)
        pack3= Package(name="Gardening" , price = 600 , prof_id=3)
        pack4= Package(name="Weed Removal" , price = 700 , prof_id=3) 
        db.session.add_all([pack1,pack2,pack3,pack4])
        db.session.commit()
    
    if Booking.query.count() == 0: 
        book1 = Booking(date = datetime.strptime("25-06-2026" ,"%d-%m-%Y" ).date() ,
                        time = datetime.strptime("11:30" ,"%H:%M" ).time() , package_id = 1 , prof_id=2 , status="Booked"
                        , customer_id = 4 )
        book2 = Booking(date = datetime.strptime("26-06-2026" ,"%d-%m-%Y" ).date() ,
                        time = datetime.strptime("10:30" ,"%H:%M" ).time() , package_id = 3 , prof_id=3 , status="Booked"
                        , customer_id = 4 )
        book3 = Booking(date = datetime.strptime("27-06-2026" ,"%d-%m-%Y" ).date() ,
                        time = datetime.strptime("11:30" ,"%H:%M" ).time() , package_id = 2 , prof_id=2 ,status="Booked"
                        , customer_id = 5 )
        book4 = Booking(date = datetime.strptime("26-06-2026" ,"%d-%m-%Y" ).date() ,
                        time = datetime.strptime("10:30" ,"%H:%M" ).time() , package_id = 4 , prof_id=3 , status="Booked"
                        , customer_id = 5 )
        db.session.add_all([book1,book2,book3,book4])
        db.session.commit()
    ################
    # pack= Package.query.filter_by(id=1).first()
    # print(pack.bookings[0].customer_id)

    booking= Booking.query.filter_by(id=1).first()
    print(booking.customer.name)

    # cust1 = User.query.filter_by(id =4).first()
    # print(cust1.name)
    # print(cust1.created_bookings)