from datetime import datetime
from concert.user import User
from concert.user import PremiumMember
from concert.booking import Booking
from concert.event import Event

print('Creating a user named Matt')
user = User()
user.register('matt','abc123','mattymckern@hotmail.com', 'matt', 'mckern', '0400000000', '1 cooked st')
print(user)

print('################')

print('Creating a premium member named Brendan')
prem_member = PremiumMember()
prem_member.register('brendan','123abc', 'brendan@gmail.com', 'brendan', 'peterson', '0401000000', '2 cooked st', 1)
print(prem_member)

print('###############')

date = datetime(2024,10,20)

print('Creating an Event for Travis Scoot')
travis = Event('Travis Scoot', 'Performing live in Queensland', 'Suncorp Stadium', date, '18:00')
print(travis)


print('###############')

print('Creating a booking for user')
booking = Booking(date, "18:00", travis, user, 100)
print('#################')
print(booking)

print('#################')
print("Access Event description of Booking: ", booking.event.description)