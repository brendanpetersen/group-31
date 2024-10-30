class User:
    #Guest user information
    def __init__(self):
        self.user_type = 'guest'
        self.username = None
        self.password = None
        self.email = None
        self.first_name = None
        self.surname = None
        self.contact_number = None
        self.street_address = None
    #Add register option for user
    def register(self, username, password, email, fname, surname, number, address):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = fname
        self.surname = surname
        self.contact_number = number
        self.street_address = address

    #Displaying only user and email as to not disclose personal information
    def __repr__(self):
        str = f"Name: {self.username}, Email: {self.email}, User type: {self.user_type}"
        return str
    
class PremiumMember(User):

    def __init__(self):
        self.user_type = 'Premium Member'
        self.memberID = None

    def register(self, username, password, email, fname, surname, number, address, memberID):
        super().register(username ,password, email, fname, surname, number, address)
        self.memberID = memberID
    
    def __repr__(self):
        str = super().__repr__()
        str = str + f" Member ID: {self.memberID}"
        return str
