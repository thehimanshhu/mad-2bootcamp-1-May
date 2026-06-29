from celery import shared_task
import time
from .models import db, User, Booking
import csv
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

        

