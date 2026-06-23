from flask import current_app as app
from .models import db , User , Role , UserRoles

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
