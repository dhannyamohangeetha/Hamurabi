# class Hamurabi(): abc

import random
import math

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

    grain_to_feed_people = int(input("How much grain do you need to feed people?: "))
    if bushels > grain_to_feed_people:
        print("We have enough grain to feed people ")
    bushels = bushels - grain_to_feed_people
    print(bushels)

askHowMuchGrainToFeedPeople(2000)




def askHowManyAcresToPlant(acresOwned:int, population:int,bushels:int):
    acres_to_plant = int(input("How many acres to plant with the grain?: "))
    if acres_to_plant > total_acres:
    elif acres_to_plant> population * 10
    else:acres_to_plant * 2 > bushels


def plagueDeaths(population:int):
    if random.random() < 0.15:
        plague_dead = math.ceil(population/2)
        return population - plague_dead
    else :
        return 0


def starvationDeaths(population:int,bushelsFedToPeople:int):


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


