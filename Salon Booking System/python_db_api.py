from flask import Flask, jsonify, request
from db_utils import get_all_booking_availability, add_booking

app = Flask(__name__)


# GETTING INFORMATION ABOUT AVAILABILITY


@app.route('/availability/<date>')
def get_bookings(date):
    res = get_all_booking_availability(date)
    return jsonify(res)

# http://127.0.0.1:5001/availability/2020-12-16



#  ADDING A BOOKING

@app.route('/booking', methods=['PUT'])
def book_appt():
    booking = request.get_json()
    add_booking(
        _date=booking['_date'],
        teamMember=booking['teamMember'],
        time=booking['time'],
        customer=booking['customer'],
    )

    return booking


if __name__ == '__main__':
    app.run(debug=True, port=5001)