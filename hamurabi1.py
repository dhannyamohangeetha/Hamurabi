# class Hamurabi(): abc
def play_game(self):
    print("Let's play!")

total_acres = 1000
bushels = 2800
acres_value = 19
population = 100



# hamurabi = Hamurabi()
# hamurabi.play_game()
def askhowmanyAcresToBuy(price:int,bushel:int):
    # asking the player how much land he wants to buy
    global total_acres
    buy_acres = int(input("How many acres do you want to buy?: "))

    if buy_acres * price < bushel:
        print("We have enough bushels to buy the land.")
        total_acres = total_acres + buy_acres
        bushel = bushel - (buy_acres * price)
        print(total_acres)
        print(bushel)


askhowmanyAcresToBuy(17 , 2800)

def askHowManyAcresToSell(price:int , bushels:int):
    # Asking the player how many acres he wants to sell
     global total_acres

     acres_sell = int(input("How many acres will you sell?: "))
     if acres_sell < total_acres:
         print("we have enough acres to sell")
     total_acres = total_acres - acres_sell
     bushels = bushels + (acres_sell * price)
     print(total_acres)
     print(bushels)

askHowManyAcresToSell(17 , 200)


def askHowMuchGrainToFeedPeople(bushels:int):


    pass

def askHowManyAcresToPlant(acresOwned:int, population:int,bushels:int):
    pass

def plagueDeaths(population:int):
    pass

def starvationDeaths(population:int,bushelsFedToPeople:int):
   pass

def uprising(population:int,howManyPeopleStarved:int): #return boolean
    pass

def immigrants(population:int,acresOwned:int,grainInStorage:int):
    pass

def harvest(acres:int,bushelsUsedAsSeed:int):
    pass

def grainEatenByRats(bushels:int):
    pass

def newCostOfLand():
    pass
def printSummary():
    pass

def final_Summary():
    pass


