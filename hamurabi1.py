
import random
import math


def play_game(self):
    print("Let's play!")

year = 1
total_acres = 1000
bushels = 2800
acres_value = 19
population = 100
starved_deaths = 0
grain_to_feed_people = 0
num_immigrants = 0
acres_to_plant = 0
bushels_harvested = 0
rat_ate = 0


def ask_how_many_acres_to_buy():
    # asking the player how much land he wants to buy
    global total_acres, bushels, acres_value
    buy_acres = int(input("How many acres do you want to buy?: "))

    if buy_acres * acres_value < bushels:
        print("We have enough bushels to buy the land.")
        total_acres = total_acres + buy_acres
        bushels = bushels - (buy_acres * acres_value)
        # print(total_acres)
        # print(bushel)

def ask_how_many_acres_to_sell():
    # Asking the player how many acres he wants to sell
    global total_acres
    global bushels
    acres_sell = int(input("How many acres will you sell?: "))
    if acres_sell < total_acres:
        print("we have enough acres to sell")
    total_acres = total_acres - acres_sell
    bushels = bushels + (acres_sell * acres_value)

def ask_how_much_grain_to_feed_people():
    global starved_deaths, bushels
    global grain_to_feed_people
    grain_to_feed_people = int(input("How much grain do you need to feed people?: "))
    if bushels > grain_to_feed_people:
        print("We have enough grain to feed people ")
        bushels = bushels - grain_to_feed_people
        starved_deaths = population - grain_to_feed_people // 20
    # print(bushels)

def ask_how_many_acres_to_plant():
    global acres_to_plant
    acres_to_plant = int(input("How many acres to plant with the grain?: "))
    global bushels
    if acres_to_plant > total_acres:
        print("You dont have enough acres to plant")
    # population * 10 = each person can plant 10 acres.
    elif population * 10 < acres_to_plant:
        print("You don't have enough population to plant.")
    # acres_to_plant * 2 = 2 bushels per acres
    elif bushels < acres_to_plant * 2:
        print("You dont have enough bushels to plant.")

    else:
        total_acres > acres_to_plant and population * 10 > acres_to_plant and bushels > acres_to_plant * 2
    print("You have enough population , acres and bushels to plant.")
    bushels = bushels - acres_to_plant * 2
    # print(bushels)

def plague_deaths():
    global population
    if random.random() < 0.15:
        plague_dead = math.ceil(population/2)
        return population - plague_dead
    else :
        return 0


def starvation_deaths():
    global starved_deaths
    global population;
    starved_deaths = population - grain_to_feed_people // 20
    population = population - starved_deaths
    if starved_deaths > 0:
        print("You did not feed well to your people.")
    else:
        starved_deaths = 0
        print("You fed your people well.")


def uprising():
    global starved_deaths
    if starved_deaths > 0.45:
        print("You ruled poorly. Game Over ")
        return True
    else:
        return False


def immigrants():
    global starved_deaths, num_immigrants, population
    if starved_deaths > 0:
        num_immigrants = 0
    else:
        num_immigrants = (20 * total_acres + bushels) // (100 * population) + 1
        #  // is used for rounding up the float number.
        population = population + num_immigrants



def harvest():
    global acres_to_plant
    global bushels_harvested
    bushels_used_as_seed = random.randrange(1, 6)
    bushels_harvested = acres_to_plant * bushels_used_as_seed
    return bushels_harvested

def grain_eaten_by_rats():
    global rat_ate
    global bushels_harvested
    global bushels

    rat_infestation_chance = random.randint(1, 100)
    if rat_infestation_chance <= 40:
        percentage_rat_ate = random.uniform(0.1, 0.3)
        rat_ate = round(percentage_rat_ate * bushels_harvested)
        print('rat_ate: ', rat_ate)
        bushels = bushels - rat_ate
    else:
        print("not affected by rat")





def new_cost_of_land():
    global acres_value
    acres_value = random.randint(17, 23)
    print("The price of land will be", acres_value, "bushels per acre next year***")


def printtest():
    print('total_acres: ', total_acres)
    print('bushels: ', bushels)
    print('starved_deaths: ', starved_deaths)
    print('population: ', population)
    print('bushels_harvested: ', bushels_harvested)




def print_summary():
    print(f"O great Hammurabi!\n"
            f"You are in year {year} of your ten year rule.\n"
            f"In the previous year {starved_deaths} people starved to death.\n"
            f"In the previous year {num_immigrants} people entered the kingdom.\n"
            f"The population is now {population}.\n"
            f"We harvested {bushels_harvested} bushels at 3 bushels per acre."
            f"Rats destroyed {rat_ate} bushels, leaving {bushels} bushels in storage.\n"
            f"The city owns {total_acres} acres of land.\n"
            f"Land is currently worth {acres_value} bushels per acre.")


def final_summary():
    print("CONGRATULATION \n YOU SURVIVED 10 YEARS ")


for i in range(10):
    ask_how_many_acres_to_buy()
    ask_how_many_acres_to_sell()
    ask_how_much_grain_to_feed_people()
    printtest()
    ask_how_many_acres_to_plant()
    printtest()
    plague_deaths()
    printtest()
    starvation_deaths()
    printtest()
    uprising()
    immigrants()
    harvest()
    grain_eaten_by_rats()
    printtest()
    print_summary()

final_summary()








