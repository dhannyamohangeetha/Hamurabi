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
        print("You dont have enough acres to plant")
    # population * 10 = each person can plant 10 acres.
    elif  population * 10 < acres_to_plant :
        print("You don't have enough population to plant.")
    #acres_to_plant * 2 = 2 bushels per acres
    elif bushels < acres_to_plant * 2:
        print("You dont have enough bushels to plant.")

    else: total_acres > acres_to_plant and population *10 > acres_to_plant and bushels > acres_to_plant * 2
    print("You have enough population , acres and bushels to plant.")
    bushels = bushels - acres_to_plant * 2
    print(bushels)



askHowManyAcresToPlant(1000 , 100, 1000)



def plagueDeaths(population:int):
    if random.random() < 0.15:
        plague_dead = math.ceil(population/2)
        return population - plague_dead
    else :
        return 0


def starvationDeaths(population:int,bushelsFedToPeople:int):
    starved_deaths = 0
    population = population - starved_deaths
    if starved_deaths > 0:
        print("You did not feed well to your people.")
    else:
        starved_death = 0
        print("You fed your people well.")

starvationDeaths(100 , 2000)



def uprising(population:int,howManyPeopleStarved:int):
    if starvationDeaths() > 0.45:
        return true
    print("You ruled poorly. Game Over ")

uprising(100 , 0)

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


