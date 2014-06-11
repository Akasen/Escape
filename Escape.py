import string

##Current goal - Picking up items and using items

def main():
    ##Initilization of variables.

    ##Items
    
    ##Locations
    Areas = {Area("Bed", "It is a nice bed with many soft pillows."
                 " The blankets are are soft and inviting."
                 " You try to get the thought of how comfy"
                 " the mattress was.", "Pillow"),
            Area("Desk", "It's a desk. Not a good one.", "Screwdriver"), 
            Area("Door", "The only door in this room. It is currently closed.",
                 "Poster"),
            Area("TV","It's a nice LSD TV. It's out of"
                 " this world man!", "Remote")}
    
   # print Areas[0][0].item
    ##Player initialization
    P = Player(("Keys", "Lemon", "The Monkey"),
               "Bed", Areas)
    ##Commands
    commands = {"Inventory" :   checkInventory,
                "Pickup"    :   addInventory,
                "Inspect"   :   playerLook,
                "Move"      :   playerMove,
                "Use"       :   playerUse
                }
    print("You have waken up after a nice rest. But you don't"
          +" remember falling asleep. You don't remember this room."
          +" You get out of bed and find yourself in a normal room.\n")
    goalComplete = False
    while not goalComplete:
        playerInputCheck(P, commands)
        goalComplete = checkGoal()
#Check to see if inputted commands exist


##Idea - Make all player input handled by function or functions
##the player input gets parsed. The first word is an action.
##The second word should call for something. I don't know
#--Understand "Use" and "Move".
def playerInputCheck(Player, commands):
    #Word list of player choice actions
    actions = ["Pickup", "Look", "Inspect", "Use", "Move", "Walk, Inventory"]
    playerInput = ''
    while playerInput == '':
        playerInput = raw_input(">> ")
    check = string.split(playerInput)
    inputCheck = checkCmnd(check[0], commands)
    if inputCheck in commands:
        commands[inputCheck](Player)

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
def playerMove(P):
    keyList = []
    locationFound = False
    
    print("Where do you want to go?")
    for keys in P.localDesc:
        keyList.append(keys.name)
    print keyList
    choice = str(raw_input(">> "))
    print choice
    
    ##Mental note for what code does
    ##Code checks if player is currently in room and if location is real
    for x in P.localDesc:
        if choice is P.location:
            print "You are already here"
            locationFound = True 
        elif choice in x.name:
            P.location = x.name
            print "You move towards the " +P.location
            locationFound = True
    if locationFound is False:
        print "That does not exist"

def playerLook(Player):
    #if Player.location in Player.localDesc[1]:
    print Player.areas.description
        
def playerUse(Player):
    pass

def checkInventory(Player):
    print Player.inventory

def addInventory(Player):
    for x in Player.localDesc:
        if x.item == "Pillow":
            print "PILLOW TALK!"


###Classes###
class Item(object):
    def __init__(self, name, reagent):
        self.name = name
        self.reagant = reagent

    def Use(self, reagent):
        if self.reagant == reagent:
            return True


#Player Class
class Player(object):
    def __init__(self, inventory, location, localDesc):
        self.inventory = []
        self.location = location
        self.localDesc = localDesc


class Area(object):
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item
    
main()
