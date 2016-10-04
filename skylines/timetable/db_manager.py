from .models import User, Airplane, Airport, Timetable, History
from  django.db import connection

def add_user(name, user_email, user_password):
    sql_string = "INSERT INTO User ('user_name', 'email', 'password', 'access_level') VALUES (%s, %s, %s, %s)"
    cursor = connection.cursor()
    cursor.execute(sql_string, (name, user_email, user_password, 0))
    

def add_airplane(coast, seats, free_seats):
    pass

def add_airport(airport_name, country):
    pass

def add_timetable(plane, departure_time, arrival_time, place_from, place_to, dep_data, arr_data):
    pass

def add_history(user, flight):
    pass
