
##Notes for future
## Commands are not properly outputing at all
## I do not think the commands have to be in the class.
## Should be defined out of main

import string

def main():
    Room = Area("It is a nice place")
    Place = Area("It's a place. Not a thing.")
    Areas = [Room, Place]
    P = Player(["Keys", "Lemon", "The Monkey"], Room.description, Areas)
    commands = {"Inventory" :   check_inventory,
                "Pickup"    :   add_inventory,
                "Inspect"   :   player_look,
                "Move"      :   player_move
                }
    print("You are in a room")
    goalComplete = False
    while not goalComplete:
        #break
        playerInput = raw_input(">> ")
        #check = checkCmnd(playerInput, commands)
        check = string.split(playerInput)
        inputCheck = checkCmnd(check[0], commands)
        if inputCheck in commands:
            commands[inputCheck](P)
            
        goalComplete = checkGoal()

#Check to see if inputted commands exist
def checkCmnd(x, commands):
    if x in commands:
        return x
    if x not in commands:
        print "You have become confused"

#Check if player has completed goal
def checkGoal():
    pass

def player_move(P):
    choice = raw_input("Where do you want to go?")
    for choice in P.areas:
        print P.areas[1]
        P.location = P.areas[1]

def player_look(Room):
    print Room.location

def check_inventory(self):
    print self.inventory

def add_inventory(item):
    self.inventory.append(item)


###Classes###
class Item:
    def __init__(self, name):
        self.name = name

    def Use(self):
        pass

    def Combine(self, combination):
        pass

#Player Class
class Player:
    def __init__(self, inventory, location, areas):
        self.inventory = inventory
        self.location = location
        self.areas = areas


class Area:
    def __init__(self, description):
        self.description = description
    

#P = Player(["Keys", "God", "Chuck"])
main()
