from flask import Flask, jsonify, request     #importing libraries
from db_utils import get_all_booking_availability, add_bookings       #importing functions from the utils file

app = Flask(__name__)

@app.route('/about')
def about():
    with open("About.txt", 'r') as file:
        data = file.read()
        formatted_data = data.replace('\n', '<br>')

    return formatted_data

@app.route('/availability/<date>') #api for checking the slot availability with respect to date
def get_bookings(date):
    value = get_all_booking_availability(date)
    return jsonify(value)


@app.route('/booking', methods = ['PUT']) #api to chcek the bookings
def book_apt():
    booking = request.get_json()
    add_bookings(
                 _date=booking['_date'],
                 games= booking['games'],
                 time=booking['time'],
                 player=booking['player']
                 )
    return booking


if __name__ == '__main__':
    app.run(debug = True, port = 5001)
