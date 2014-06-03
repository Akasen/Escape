import string

##Current goal - Picking up items and using items

def main():
    ##Initilization of variables.

    ##Items
    
    ##Locations
    Bed =   Area("Bed", "It is a nice bed with many soft pillows."
                 " The blankets are are soft and inviting."
                 " You try to get the thought of how comfy"
                 " the mattress was.", "Pillow")
    Desk =  Area("Desk", "It's a desk. Not a good one.", "Screwdriver")
    Door =  Area("Door", "The only door in this room. It is currently closed.",
                 "Poster")
    TV =    Area("TV","It's a nice LSD TV. It's out of"
                 " this world man!", "Remote")
    
    AreaItem = {"Bed"  :   Bed.item,
             "Desk" :   Desk.item,
             "Door" :   Door.item,
             "TV"   :   TV.item
             }    
    
    
    ##Realized flaw when items need to be picked up
    AreaDesc = {"Bed"  :   Bed.description,
             "Desk" :   Desk.description,
             "Door" :   Door.description,
             "TV"   :   TV.description
             }
    Areas = (Bed, Desk, Door, TV),("Bed", "Desk", "Door", "TV"),(Bed.item, Desk.item, TV.item)
    print Areas[0][0].item
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
    
    print("Where do you want to go?")
    for keys in P.localDesc[1]:
        keyList.append(keys)
    print keyList
    choice = str(raw_input(">> "))
    print choice
    if choice in P.location[1]:
        print "You are already here"
    elif choice in P.localDesc[1]:
        P.location = choice
        print "You move towards the " +P.location
    else:
        print "Location does not exist in this room"
#
#Indexes room
#Player.localDesc[1].index(Player.location)
def playerLook(Player):
    #if Player.location in Player.localDesc[1]:
    print Player.localDesc[0][Player.localDesc[1].index(Player.location)].description
        
def playerUse(Player):
    pass

def checkInventory(Player):
    print Player.inventory

def addInventory(Player):
    print(Player.localDesc[1].index(Player.location))
    Player.inventory.append(Player.localDesc[0][(Player.localDesc[1].index(Player.location))].item)


###Classes###
class Item:
    def __init__(self, name, reagent):
        self.name = name
        self.reagant = reagent

    def Use(self, reagent):
        if self.reagant == reagent:
            return True


#Player Class
class Player:
    def __init__(self, inventory, location, localDesc):
        self.inventory = []
        self.location = location
        self.localDesc = localDesc


class Area:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item
    
main()
