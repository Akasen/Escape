import string

def main():
    ##Initilization of variables.
    ##This is a test until I find a cleaner implementation
    
    ##Locations
    Bed =   Area("It is a nice bed with many soft pillows."
                 +" The blankets are are soft and inviting."
                 +" You try to get the thought of houw comfy"
                 +" the mattress was.", "Pillow")
    Desk =  Area("It's a desk. Not a good one.", "Pen")
    Door =  Area("The only door in this room. It is currently closed.")
    TV =    Area("It's a nice LSD TV. It's out of"
                 " this world man!", "Remote")
    ##Dictionary of locations
    ##Was originally set as Area.description.
    ##Realized flaw when items need to be picked up
    Areas = {"Bed"  :   Bed,
             "Desk" :   Desk,
             "Door" :   Door,
             "TV"   :   TV
             }
    ##Player initialization
    P = Player(["Keys", "Lemon", "The Monkey"],
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
        playerInput = ''
        while playerInput == '':
            playerInput = raw_input(">> ")
        check = string.split(playerInput)
        inputCheck = checkCmnd(check[0], commands)
        if inputCheck in commands:
            commands[inputCheck](P)
            
        goalComplete = checkGoal()

#Check to see if inputted commands exist


##Idea - Make all player input handled by function or functions
##the player input gets parsed. The first word is an action.
##The second word should call for something. I don't know
#--Understand "Use" and "Move".
def playerInputCheck(Player):
        playerInput = ''
        while playerInput == '':
            playerInput = raw_input(">> ")
        check = string.split(playerInput)
        inputCheck = checkCmnd(check[0], commands)

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
    
    print("Where do you want to go?")
    for keys in P.positions:
        keyList.append(keys)
    print keyList
    choice = str(raw_input(">> "))
    print choice
    if choice in P.positions:
        P.location = choice
        print "You move towards the " +P.location
    else:
        print "Location does not exist in this room"


def playerLook(Player):
    place = str(Player.location)
    if Player.location in Player.positions:
        print Player.positions[str(place)]
        
def playerUse(Player):
    pass

def checkInventory(Player):
    print Player.inventory

def addInventory(item):
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
    def __init__(self, inventory, location, positions):
        self.inventory = inventory
        self.location = location
        self.positions = positions


class Area:
    def __init__(self, description, interaction = None, items = None):
        self.description = description
        self.interaction = interaction
        self.items = items
    
main()
