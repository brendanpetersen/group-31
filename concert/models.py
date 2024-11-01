class Concert:

    def __init__(self, name, description, venue, date, time, image, price):
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.venue = venue
        self.date = date
        self.time = time
        self.comments = list()

    def set_comments(self, comment):
        self.comments.append(comment)

    def __repr__(self):
        return f"Name: {self.name}, Venue: {self.venue}, Date: {self.date, self.time}, Price: {self.price}"

class Comment:
    def __init__(self,user, text, created_at):
        self.user = user
        self.text = text
        self.created_at = created_at

    def __repr__(self):
        return f"User {self.user}, \n Text {self.text}"