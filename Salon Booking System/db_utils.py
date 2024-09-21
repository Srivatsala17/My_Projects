import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def _map_values(schedule):
    mapped = []
    for item in schedule:
        mapped.append({
            'name': item[0],
            '12-13': 'Not Available' if item[1] else 'Available',
            '13-14': 'Not Available' if item[2] else 'Available',
            '14-15': 'Not Available' if item[3] else 'Available',
            '15-16': 'Not Available' if item[4] else 'Available',
            '16-17': 'Not Available' if item[5] else 'Available',
            '17-18': 'Not Available' if item[6] else 'Available',
        })
    return mapped


# EXAMPLE 1
def get_all_booking_availability(_date):
    availability = []
    try:
        db_name = 'nano'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            SELECT  teamMember, `12-13`, `13-14`, `14-15`, `15-16`, `16-17`, `17-18`
            FROM salon_bookings 
            WHERE bookingDate = '{}'
            """.format(_date)

        cur.execute(query)

        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        availability = _map_values(result)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return availability


# EXAMPLE 1
def add_booking(_date, teamMember, time, customer):
    try:
        db_name = 'nano'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            UPDATE  salon_bookings
            SET 
                `{time}` = 1, 
                `{time_id}` = '{customer}' 
            WHERE bookingDate = '{date}' AND teamMember = '{teamMember}'
            """.format(time=time, time_id=time +'-booking-id', customer=customer, date=_date, teamMember=teamMember)

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


if __name__ == '__main__':
    get_all_booking_availability('2020-12-15')