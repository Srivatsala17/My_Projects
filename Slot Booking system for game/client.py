import requests #importing the libraries
import json
#this is a function to display the availability by date
def get_availability_by_date(date):
    endpoint = 'http://127.0.0.1:5001/availability/{}'.format(date)
    headers = {'content type':'application/json'}
    result = requests.get(endpoint, headers =headers)
    return result.json()

#this function is to add any new booking done by the client or the user
def add_new_booking(date, games, time, player):
    endpoint = 'http://127.0.0.1:5001/booking'
    headers = {'Content-Type': 'application/json'}
    booking = {
        '_date': date,
        'games': games,
        'time': time,
        'player': player
    }
    result = requests.put(endpoint, headers=headers, data=json.dumps(booking))
    return result.json()

#this function is to display the availability of teh slot
def display_availability(records):
    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format('GAMES', 'SLOT1', 'SLOT2', 'SLOT3', 'SLOT4', 'SLOT5','SLOT6'))
    for item in records:
        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(item['name'], item['slot1'], item['slot2'], item['slot3'], item['slot4'], item['slot5'], item['slot6']))
#this runs and prints all the data
def run():
    print('-' * 200)
    print('\n Welcome to game haven \n')
    print('-' * 200)
    date = input('\n When do you want to play or book the slot for playing \n')
    slots = get_availability_by_date(date)
    print('-' * 200)
    print('\n Our availabilities \n')
    print('-' * 200)
    print()
    display_availability(slots)
    print()
    print('-' * 200)
    place_booking = input('\n Would you like to book the appointment y/n \n').lower().strip()

    book = place_booking == 'y'

    if book:
        player = input('\n What is your name? \n')
        gamename = input('\n Which game do you want to play? \n')
        time = input('\n Choose any slots - slot1, slot2, slot3, slot4, slot5, slot6 \n').strip().lower()
        print('-' * 200)
        add_new_booking(date, gamename, time, player)
        print('\n Your slot is booked \n')
        print('-' * 200)
        slots = get_availability_by_date(date)
        display_availability(slots)



    print()
    print('*' * 200)
    print('Thank you!!!!')
    print('*' * 200)

run()





