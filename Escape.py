import string

##Current goal - Picking up items and using items

def main():
    ##Initilization of variables.

    ##Items
    
    ##Locations
    PlayerZones = [Area("bed", "It is a nice bed with many soft pillows."
                 " The blankets are are soft and inviting."
                 " You try to get the thought of how comfy"
                 " the mattress was.", ["Pillow"]),
            Area("desk", "It's a desk. Not a good one.", ["Screwdriver"]), 
            Area("door", "The only door in this room. It is currently closed.",
                 ["Poster"]),
            Area("tv","It's a nice LSD TV. It's out of"
                 " this world man!", ["Remote"])]
    
   # print Areas[0][0].item
   
    ##Player initialization
    P = Player([],
               "bed", PlayerZones)
    ###INITIALIZATION END
    
    ##Commands
    commands = {"inventory" :   checkInventory,
                "pickup"    :   addInventory,
                "inspect"   :   playerLook,
                "look"      :   playerLook,
                "move"      :   playerMove,
                "use"       :   playerUse
                }
    print("You have waken up after a nice rest. But you don't"
          +" remember falling asleep. You don't remember this room."
          +" You get out of bed and find yourself in a normal room.\n")
    goalComplete = False
    while not goalComplete:
        cmd = playerInputCheck(commands)
        cmd(P)
        goalComplete = checkGoal()
#Check to see if inputted commands exist


##Idea - Make all player input handled by function or functions
##the player input gets parsed. The first word is an action.
##The second word should call for something. I don't know
#--Understand "Use" and "Move".
def playerInputCheck(commands):
    actionFound = False
    #Word list of player choice actions
    actions = ["pickup", "look", "inspect", "use", "move", "walk", "inventory"]
    playerInput = ''
    while actionFound != True:
        playerInput = raw_input(">> ").lower()
        if playerInput in commands:
            actionFound = True
    check = string.split(playerInput)
    inputCheck = checkCmnd(check[0], commands)
    if inputCheck in commands:
        return commands[inputCheck]

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
    for keys in P.localChoices:
        keyList.append(keys.name)
    print keyList
    choice = str(raw_input(">> ").lower())
    print choice
    
    if choice == P.location:
        print("You are already here")
        locationFound = True 

    ##Mental note for what code does
    ##Code checks if player is currently in room and if location is real
    if(locationFound == False):
        for x in P.localChoices:
            if choice == x.name:
                P.location = x.name
                P.movement(x.name)
                print "You move towards the " +P.location
                locationFound = True
                break
        if locationFound is False:
            print "That does not exist"

def playerLook(P):
    #if Player.location in Player.localChoices[1]:
    for x in P.localChoices:
        if x.name == P.location:
            print x.description
        
def playerUse(P):
    pass

def checkInventory(P):
    if P.inventory == []:
        print "You have nothing"
    else:
        print P.inventory

def addInventory(P):
    for x in P.localChoices:
        if x.name == P.location:
            if x.item == False:
                "You are reaching around like an idiot"
            print x.item
            P.pickup(x.item)
            x.itempickup()


###Classes###

# Reagent refers to the object being used
# Reagent refering to something that can be mixed or combined
# I wanted to use a specific term that didn't need to be a camelcased variable
class Item(object):
    def __init__(self, name, reagent):
        self.name = name
        self.reagant = reagent

    def Use(self, reagent):
        if self.reagant == reagent:
            return True

# Player Class
class Player(object):
    def __init__(self, inventory, location, localChoices):
        self.inventory = inventory
        self.location = location
        self.localChoices = localChoices
    
    def movement(self, newlocation):
        self.location = newlocation
    
    def look(self):
        self.localChoices.description    
    
    def pickup(self, item):
        self.inventory.append(item)

# Location Class
# I will punch myself four years ago for not commenting this
class Area(object):
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item
    
    def itempickup(self):
        self.item = False
    
main()
