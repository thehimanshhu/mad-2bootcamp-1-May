from celery import shared_task
import time
from .models import db, User, Booking
import csv
from datetime import datetime

@shared_task(name = "add" , ignore_result=False)
def add_together(a, b) -> int:
    time.sleep(20)
    return int(a) + int(b)


@shared_task(name="download_csv" , ignore_result = False)
def download_csv(id):
    time.sleep(10)
    bookings = db.session.query(Booking).filter_by(customer_id = id).all()
    filename = f"customer-{id}.csv"
    with open(f"./static/{filename}" , "w") as csvfile : 
        csv_obj = csv.writer(csvfile, delimiter=",")
        csv_obj.writerow(["No." , "Package Name" , "Professional Name" , "Professional Email" , "Date" ,"Time"])
        for index , booking in enumerate(bookings):
            csv_obj.writerow( [  index + 1 , booking.package.name , booking.professional.name , booking.professional.email,
                               booking.date , booking.time])
    return filename

        
from .utils import prepare_template
from .mail import send_email
@shared_task(name="admin-monthly-report" , ignore_result=True)
def admin_report():
    start_date = datetime.strptime("01-06-2026", "%d-%m-%Y").date()
    end_date = datetime.strptime("30-06-2026", "%d-%m-%Y").date()
    bookings= Booking.query.filter(Booking.date.between(start_date,end_date)).all()
    data = { "username" : "Admin" , "bookings" : bookings}
    output  = prepare_template("./templates/admin-mail.html" ,data )
    send_email("admin@gmail.com" ,"Monthely Activity Report for Jun 2026" , output )
    return "Done"

