#!/usr/bin/python3

def waterfall():
    print("You reached a magnificent waterfall. How long do you stay?")

    choice = input("-> ")
    try:
        how_long = int(choice)
    except ValueError:
        dead("You decided not to stay here. A dropbear comes and eats you!")

    if how_long < 10:
        print("The meditative effect fails on you. Let's keep going.")
        walk_3()
    elif 10 <= how_long < 30:
        print("You really enjoy the waterfall. But now it is time to  move on")
        walk_2()
    else:
        dead("You can't resist the temptation to try the water. Waterfallsharks\
 eat you.")


def dead(reason):
    print(reason, "See you later!")
    exit(0)

def walk_1():
    print("You walk along the track and see the path splitting in two \
directions. Which one do you take? ")

    choice = input("-> ")
    if choice.lower() == "left":
        waterfall()
    elif choice.lower() == "right":
        gorge()
    else:
        dead("Your indecision attracted brownsnakes. They said you tasted \
great!")

def walk_2():
    dead("You keep walking and walking further into the park. You don't find \
anything to eat and starve to death.")

def walk_3():
    print("You detect a path that leads back to the carpark. You got out \
unharmed.")
    exit(0)

def carpark():
    print("You are at the carpark of the Gregor National Park in Old East \
England.")
    print("Where do you want to go?")

    choice = input("-> ")
    if choice.lower() == "toilet":
        toilet()
    elif choice.lower() == "park":
        walk_1()
    elif choice.lower() == "home":
        dead("You car explodes on the way home.")

    else:
        print("You have to make a decision.")
        carpark()

def toilet():
    dead("You find an unused, clean cabin. Sadly you are not alone. A redback \
bites you. You don't suffer for long.")


def gorge():
    print("What a wonderful gorge. You see something sparkle in the bottom. Do \
you want to check it out?")

    choice = input("-> ")
    if choice.lower() == "yes":
        dead("You climb down and realise it is a trap. Three aboriginals come \
and eat you.")
    elif choice.lower() == "no":
        print("Really?")
        gorge()
    else:
        walk_3()

carpark()
