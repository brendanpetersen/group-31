from datetime import datetime
from .user import User

class Booking:
    #Define Booking information
    def __init__(self, date, time, title, user, price):
        self.date = date
        self.time = time
        self.event = title
        self.user = user
        self.price = price
        self.num_guests = 1
    #Define info represented when called
    def __repr__(self):
        str = f"User: {self.user}\nEvent: {self.event}\nDate: {self.date}\nTime: {self.time}\nPrice: {self.price}\nNumber of Guests: {self.num_guests}"
        return str