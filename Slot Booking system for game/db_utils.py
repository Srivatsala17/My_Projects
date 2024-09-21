import mysql.connector
from config import HOST, PASSWORD, USER
#importing the libraries and the config file

db_name = 'game_haven' #this is our database name
#this is a default class to catch the exceptions will connecting to the database
class DbConnectionError(Exception):
    pass
#this function helps to connect to the database
def _connect_to_db():
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return mydb
#this is to format the result from the get_availability_by_date() function.
#the result is in the form of the tuples but we need the result to be in the form of a dictionary with values and keys so formatting accordingly
def map_value(schedule):
    mapped=[]
    for item in schedule:
        mapped.append(
            {
                'name': item[0],
                'slot1':'Booked' if item[1] else 'Not Booked',
                'slot2': 'Booked' if item[2] else 'Not Booked',
                'slot3': 'Booked' if item[3] else 'Not Booked',
                'slot4': 'Booked' if item[4] else 'Not Booked',
                'slot5': 'Booked' if item[5] else 'Not Booked',
                'slot6': 'Booked' if item[6] else 'Not Booked'

            }
        )
    return mapped
#this prints the availability according to the dates
def get_all_booking_availability(_date):
    availability=[]
    try:
        db_connection = _connect_to_db()
        mycursor = db_connection.cursor()
        print('connected to db')
        query = """
        SELECT games, slot1, slot2, slot3, slot4, slot5, slot6
        FROM game_room_bookings
        WHERE bookingdate = '{}'
        """.format(_date)

        mycursor.execute(query)
        result = mycursor.fetchall()
        availability = map_value(result)

    except Exception:
        raise DbConnectionError('Failed to connect')
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection closed')
    return availability
#when a slot is booked this adds the booking to the table and displays
def add_bookings(_date, games, time, player):
    try:
        db_connection = _connect_to_db()
        mycursor = db_connection.cursor()
        print('connected to db')
        query = """
           UPDATE game_room_bookings
           SET {time} = 1, {time}_booking_id = '{player}'
           WHERE bookingDate = '{date}' AND games = '{games}' """.format(time=time, player=player,date=_date, games=games)

        mycursor.execute(query)
        db_connection.commit()
        mycursor.close()

    except Exception:
        raise DbConnectionError('Failed to connect')
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection closed')



if __name__ == '__main__':
    pass
    #add_bookings('2024-07-08', 'Chess', 'slot4', 'Ram')

    #print(_connect_to_db())
    #print(get_all_booking_availability('2024-07-08'))

#calling different functions and passing arguments to check the working of teh function