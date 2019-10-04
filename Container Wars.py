import random, time

CW = ("   _____            _        _                  __          __             \n  / ____|          | |      (_)                 \ \        / /             \n | |     ___  _ __ | |_ __ _ _ _ __   ___ _ __   \ \  /\  / /_ _ _ __ ___  \n | |    / _ \| '_ \| __/ _` | | '_ \ / _ \ '__|   \ \/  \/ / _` | '__/ __| \n | |___| (_) | | | | || (_| | | | | |  __/ |       \  /\  / (_| | |  \__ \ \n  \_____\___/|_| |_|\__\__,_|_|_| |_|\___|_|        \/  \/ \__,_|_|  |___/ \n")
namelist = ["Liam", "Will", "John", "Jack", "Michael", "Al", "Samuel", "Dave", "Mike", "Hudson", "Dominic", "Marc", "Evan", "Chase", "Leonardo", "Ella", "Aubrey", "Alice", "Naomi", "Piper", "Ruby", "Kaylee", "Clara", "Peyton", "Sara"]
adjectives = ["Antique", "Weathered", "New", "Brand New", "Perfect", "Red", "Blue", "Yellow", "Black", "Pink", "Crusty", "Musty", "Dusty", "Gold Encrusted", "Gucci"]
items = ["Tooth Brush", "CD Player", "TV", "Laptop", "Pencil", "Mattress", "Playing Cards", "Watch", "Model Car", "Piano", "Jewlry", "Board Game", "Hat", "Shoes", "Egg Beater"]
npcs = []
npcs2 = []
players = []

class NPC:
    def __init__(self, money, aggression, name):
        self.money = money
        self.aggression = aggression
        self.inventory = []
        self.name = name
        self.spent = 0
    def bid(self, containervalue):
        if self.money > containervalue * self.aggression:
            self.spent = random.randint(10, 25) + random.randint(25, 100)
        else:
            self.spent = 0
            

class Player:
    def __init__(self, money):
        self.money = money
        self.inventory = []
        self.name = playername

class loot:
    def __init__(self, value, name):
        self.value = value
        self.name = name

def mainmenu():
    while 1:
        print("\n"*100)
        print(CW)
        for x in players:
          print (x.money)
        answer = input("1)Play\n2)Exit\n")
        if answer == "1":
            break
        if answer == "2":
          while 1:
            print("\n"*100)
        
def initialize():
    global playername
    print("\n"*100)
    playername = input("What would you like to be known by?\n")
    player = Player(random.randint(1500, 2000))
    players.append(player)
    for x in range(0, 5):
        rando = random.SystemRandom()
        name = rando.choice(namelist)
        npc = NPC((random.randint(1200, 1500)), round((random.random()+1), 1), name)
        namelist.remove(name)
        npcs.append(npc)

def tutorial():
    while 1:
        print("\n"*100)
        answer = input("Would you like a brief tutorial " + players[0].name + "?(Y or N)")
        if answer == "Y":
            print("\n"*100)
            print("Tutorial:\n")
            print("In this game you will be competing for storage units against 5 other players.\n While auctioning is optional, it is also recommended so that you can make profit.\n After the storage unit is sold, its owner can sell its contents for profit or sometimes, at a loss.\n") 
            input("Press Enter to continue...")
            break
        if answer == "N":
            break

def lore():
    while 1:
        print("\n"*100)
        print("You and 5 other individuals have gathered to bid on storage units that are being auctioned off, with careful management and some luck, you could hit it rich.\n")
        print("The other 5 bidders are named:")
        for x in npcs:
            print(x.name)
        input("Press Enter to continue...")
        tutorial()
        break

def initializeauction():
    global container
    container = []
    name = random.choice(namelist)
    while 1:
        number = random.randint(1, 6)
        if number == 1 or number == 2 or number == 3:
            containervalue = 1
        if number == 4 or number == 5:
            containervalue = 2
        if number == 6:
            containervalue = 3
        for x in range(0, (containervalue * (random.randint(2, 4)))):
            adj = random.choice(adjectives)
            dathing = random.choice(items)
            item = loot(containervalue * (random.randint(50, 200)), (str(adj) + " " + str(dathing)))
            container.append(item)
        break
    
def auction():
    for x in npcs:
        npcs2.append(x)
    playerbidded = 1
    containervalue = 250
    print("\n"*100)
    print("Auction\n")
    print("Auction participants:")
    for x in players:
        print(x.name)
    for x in npcs:
        print(x.name)
    initializeauction()
    input("Press Enter to continue...")
    while 1:
        if len(npcs) <= 1:
          if playerbidded != 1:
              for x in npcs:
                  winner = x
              print("\n"*100)
              print(str(winner.name) + " has won the bid")
              input("Press Enter to continue...")
              for x in container:
                winner.money += x.value
              break
          if playerbidded == 1:
            if len(npcs) <= 0:
              for x in players:
                winner = x
                for i in container:
                  x.inventory.append(i)
              print("\n"*100)
              print(str(winner.name) + " has won the bid")
              input("Press Enter to continue...")
              break
        print("\n"*100)
        print("Auction\n")
        print("Container current value: " + str(containervalue))
        print("Your current balance: " + str(players[0].money))
        answer = input("How much would you like to bid?(Please enter PASS to not bid)\n")
        if answer == "PASS":
            print("\n"*100)
            playerbidded -= 1
            for x in npcs:
                x.bid(containervalue)
                containervalue += x.spent
            for x in npcs:
                if x.spent != 0:
                    print(str(x.name) + " raised the bid and has spent " + str(x.spent) + ", they are now left with " + str(x.money))
                if x.spent == 0:
                    print(str(x.name) + " has passed the bid")
                    npcs.remove(x)
            input("Press Enter to continue...")
        else:
            try:
                if int(answer) < 1:
                    print(0 / 0)
                test = int(answer) + 1
            except ValueError:
                print("\n"*100)
                print("Please only enter valid input!")
                input("Press Enter to continue...")
            except ZeroDivisionError:
                print("\n"*100)
                print("Please only enter valid input!")
                input("Press Enter to continue...")
            else:
                if (containervalue + int(answer)) > players[0].money:
                    print("\n"*100)
                    print(" You're going over bud")
                    input("Press Enter to continue...")
                else:
                    print("Success")
                    containervalue += int(answer)
                    print("\n"*100)
                    for x in npcs:
                        x.bid(containervalue)
                        containervalue += x.spent
                    for x in npcs:
                        if x.spent != 0:
                            print(str(x.name) + " raised the bid and has spent " + str(x.spent) + ", they are now left with " + str(x.money))
                        if x.spent == 0:
                            print(str(x.name) + " has passed the bid")
                            npcs.remove(x)   
                    input("Press Enter to continue...")
    for x in npcs2:
        npcs.append(x)
                    
def inventory():
    print("\n"*100)
    print("Inventory:")
    for x in players[0].inventory:
        print(str(x.name) + " Value: " + str(x.value))
    input("\nPress Enter to continue...")

def sell():
    print("\n"*100)
    print("Sell")
    total = 0
    for x in players:
      for i in x.inventory:
        total += i.value
    while 1:
        print("\n"*100)
        answer = input("Are you sure you want to sell all of this? If so, you would make " + str(total) + " dollars. (YES or NO)")
        if answer == "NO":
          break
        if answer == "YES":
          for x in players:
            x.money += total
            x.inventory.clear()
          print("Everything has been sold off.")
          input("\nPress Enter to continue...")
          break


def options():
    print("\n"*100)
    print("Options")
    um = input("Enter UMMM to increase balance. or don't\n")
    if um == "UMMM":
      for x in players:
        x.money += 1
        print("\n"*100)
        print("Balance increased")
        input("Press Enter to continue...")


def maingamemenu():
    while 1:
        print("\n"*100)
        print(CW)
        answer = input("What would you like to do next?\n1)Participate in the next auction\n2)Check inventory\n3)Sell from inventory\n4)Options\n")
        if answer == "1":
            auction()
        if answer == "2":
            inventory()
        if answer == "3":
            sell()
        if answer == "4":
            options()



mainmenu()
initialize()
lore()
maingamemenu()
