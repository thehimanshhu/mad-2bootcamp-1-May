from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.models import db,User,Role
from flask_security import Security, SQLAlchemyUserDatastore
from flask_cors import CORS
from application.celery_init import celery_init_app
def create_app():
    app = Flask(__name__ )
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.sqlite3"
    app.config["SECRET_KEY"] = "mysecretkey"
    # app.config["SECURITY_PASSWORD_HASH"] = "argon2"
    # app.config["SECURITY_PASSWORD_SALT"] = "mysecretsalt"
    app.config["SECURITY_TOKEN_AUTHENTICATION_HEADER"] = "Authentication-Token"  
    db.init_app(app)
    ds= SQLAlchemyUserDatastore(db,User,Role)
    app.security= Security(app, datastore = ds,register_blueprint=False)
    @app.security.unauthn_handler
    def unauthn_handler(mechanisms , headers):
        print(mechanisms)
        print(headers)
        return {"message" : f"Please Provide correct {mechanisms[0]}"},401
    
    @app.security.unauthz_handler
    def unauthz_handler(func_name , params):
        print(func_name)
        print(params)

        return {"message" : f"You don't have access to view the {params[0]} resource"},403
    CORS(app)
    app.app_context().push()
    return app

app  = create_app()

celery = celery_init_app(app)

from application.api import *
from application.inital_data import *

if __name__ =="__main__":
    app.run(debug=True)