
##Notes for future
## Commands are not properly outputing at all
## I do not think the commands have to be in the class.
## Should be defined out of main

import string

def main():
    ##Initilization of variables.
    ##This is a test until I find a cleaner implementation
    Bed = Area("It is a nice bed. Don't sleep.")
    Desk = Area("It's a desk. Not a good one.")
    Areas = {"Bed"  :   Bed,
             "Desk" :   Desk
             }
    P = Player(["Keys", "Lemon", "The Monkey"],
               Areas["Bed"], Areas)
    ##Commands
    commands = {"Inventory" :   check_inventory,
                "Pickup"    :   add_inventory,
                "Inspect"   :   player_look,
                "Move"      :   player_move
                }
    print("You are in a room")
    goalComplete = False
    while not goalComplete:
        playerInput = ''
        #break
        #print P.positions
        while playerInput == '':
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
#Not actually doing anything yet
def checkGoal():
    pass

#Player movement around areas or something.
#This is up in the air how I will implement this
#But I will figure out what I will do with this
def player_move(P):
    choice = raw_input("Where do you want to go?")
    print choice
    for choice in P.positions:
        print P.location
        P.location = P.location

def player_look(Player):
    print Player.location

def check_inventory(Player):
    print Player.inventory

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
    def __init__(self, inventory, location = None, positions = None):
        self.inventory = inventory
        self.location = location
        self.positions = positions


class Area:
    def __init__(self, description):
        self.description = description
    

#P = Player(["Keys", "God", "Chuck"])
main()
