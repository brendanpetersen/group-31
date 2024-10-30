class Event:
    #Defining details for a concert/event
    def __init__(self, title, description, venue, date, time):
        self.title = title
        self.description = description
        self.venue = venue
        self.date = date
        self.time = time
    #code for grabbing event details
    def get_event_details(self):
        return str(self)
    #code for what details are represented of an event when called by database
    def __repr__(self):
        str = f"Name: {self.title}, Desciption: {self.description}, Venue: {self.venue}, Date: {self.date}, Time: {self.time}\n"
        return str