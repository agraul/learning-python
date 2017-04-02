#!/usr/bin/python3

guests = ['R_laC', 'J_Law', 'Bismarck']
for guest in guests:
    print("Would you like to join me for dinner, {}?".format(guest))
loser = guests.pop(2)
print("OH NO! {} can't make it.".format(loser))
guests.append('D.H.')
for guest in guests:
    print("Are you still coming, {}?".format(guest))
print("I found a bigger location!")
guests.insert(0, "Donna")
guests.insert(3, "Anyes")
guests.append('DD')
for guest in guests:
    print("We shoudl all party together, don't you think {}?".format(guest))
print("OH NO! The new location was double-booked. "
      "I can only invite two of you.")

for i in range(len(guests) - 2):
    bye = guests.pop(0)
    print("Sorry, I can't have you {}".format(bye))
for guest in guests:
    print("You are still coming, right {}?".format(guest))
del guests[0]
del guests[0]
print(guests)
