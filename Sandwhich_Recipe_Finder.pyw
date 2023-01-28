import time
import smtplib
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from datetime import datetime
import os
from os.path import exists
import secrets
from email.message import EmailMessage

################################################################################################################################################################################################################################################################################################################
##Rulez
##Add everything together -- all tastes, types, and powers of all ingredients and seasonings
##Note that ingredient pieces count, so three avocado is 18 dragon since it's 6 per piece.
##Calculate flavor bonuses for the top flavor or top two flavors in some situations
##Assign powers & levels -- if a power is less than 100 its level 1, if a power is less than 280 its level 2, otherwise its level 3. The top power is given the top type, the second power is given the third type, and the third power is given the second type. Idk why it was done this way, ask Game Freak.
##Sandwiches with herba mystica (HM) have some additional considerations: one HM always gets you title power. Two HMs always gets you title and sparling power.
##
##If there's a tie in types, powers, or flavors, they're sorted in in-game order not alphabetical, so Normal will take prioroty over Flying, for instance.
################################################################################################################################################################################################################################################################################################################


def element_wise_addition(list_one, list_two):
    #both lists must be the same legnth
    resulting_list = []
    if len(list_one) == 1:
        for i in range(0, len(list_two)):
            resulting_list.append(list_one[0]+list_two[i])
    else:
        for i in range(len(list_one)-len(list_two), len(list_one)):
            resulting_list.append(list_one[i]+list_two[i])
    return resulting_list

number = -99999
sweet = 0
Spicy = 0
Bitter = 0
Sour = 0
Salty = 0
egg = 0
catching = 0
exp = 0
item = 0
raid = 0
title = 0
sparkling = 0
humungo = 0
teensy = 0
encounter = 0
fire = 0
grass = 0
water = 0
electric = 0
ground = 0
normal = 0
rock = 0
psychic = 0
flying = 0
ice = 0
bug = 0
fighting = 0
poison = 0
dragon = 0
dark = 0
steel = 0
fairy = 0
ghost = 0

herba_mistica_type_list=element_wise_addition([250],[fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy])
print(herba_mistica_type_list)
exit(0)


#List of ingredients
ingredients = [
##    {
##        'ingredient': 'name',
##        'flavor': [Sweet, Spicy, Bitter, Sour, Salty],
##        'powers': [egg, catching, exp, item, raid, title, sparkling, humungo, teensy, encounter],
##        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
##        'pieces': number  
##        },
    {
        'ingredient': 'null',
        'flavor': [Sweet, Spicy, Bitter, Sour, Salty],
        'powers': [egg, catching, exp, item, raid, title, sparkling, humungo, teensy, encounter],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': 0  
        },
    {
        'ingredient': 'Yellow Bell Pepper',
        'flavor': [1, Spicy, 3, 1, Salty],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, water, 6, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': 3  
        },
    {
        'ingredient': 'Watercress',
        'flavor': [Sweet, 1, 5, 2, 1],
        'powers': [2, catching, exp, item, 2, title, sparkling, humungo, teensy, -2],
        'types': [fire, grass, water, electric, 1, 1, 1, psychic, 1, 1, ice, 1, 1, 1, dragon, dark, 1, fairy],
        'pieces': number  
        },
    {
        'ingredient': 'Tomato',
        'flavor': [2, Spicy, 1, 4, Salty],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, 6],
        'pieces': number  
        },
    {
        'ingredient': 'Tofu',
        'flavor': [3, Spicy, Bitter, Sour, Salty],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, water, electric, 6, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': number  
        },
    {
        'ingredient': 'Strawberry',
        'flavor': [4, Spicy, Bitter, 4, Salty],
        'powers': [4, -1, exp, 7, raid, title, sparkling, -5, teensy, encounter],
        'types': [fire, grass, water, electric, normal, ground, rock, 7, 7, flying, ice, bug, 7, poison, dragon, dark, steel, fairy],
        'pieces': number  
        },
    {
        'ingredient': 'Smoked Fillet',
        'flavor': [1, Spicy, 3, 2, 3],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, 6, steel, fairy],
        'pieces': number  
        },
    {
        'ingredient': 'Rice',
        'flavor': [3, Spicy, Bitter, 1, Salty],
        'powers': [egg, catching, exp, item, raid, title, sparkling, 21, -3, 12],
        'types': [30, 30, 30, electric, 30, ground, rock, psychic, ghost, 30, ice, bug, 30, poison, dragon, dark, steel, fairy],
        'pieces': 1  
        },
    {
        'ingredient': 'Red Onion',
        'flavor': [3, Spicy, 1, Sour, Salty],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, 6, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': number  
        },
    {
        'ingredient': 'Red Bell Pepper',
        'flavor': [1, Spicy, 3, 1, Salty],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [6, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': 3  
        },
    {
        'ingredient': 'Prosciutto',
        'flavor': [2, Spicy, Bitter, 1, 4],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, 6, ice, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': number  
        },
    {
        'ingredient': 'Potato Tortilla',
        'flavor': [3, 1, 3, 1, 4],
        'powers': [egg, 21, exp, item, 12, title, sparkling, humungo, teensy, -3],
        'types': [20, 20, water, electric, normal, ground, 20, 20, 20, flying, ice, bug, 20, 20, 20, dark, steel, 20],
        'pieces': number  
        },
    {
        'ingredient': 'Potato Salad',
        'flavor': [2, Spicy, 1, 4, 3],
        'powers': [egg, catching, exp, item, raid, title, sparkling, 21, -3, 12],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, 30, flying, ice, 30, fighting, poison, 30, 30, 30, 30],
        'pieces': 1  
        },
    {
        'ingredient': 'Pineapple',
        'flavor': [3, Spicy, 1, 5, Salty],
        'powers': [4, -1, exp, 7, raid, title, sparkling, -5, teensy, encounter],
        'types': [fire, grass, 7, electric, normal, 7, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, 7, steel, fairy],
        'pieces': number  
        },
    {
        'ingredient': 'Pickle',
        'flavor': [2, 3, 1, Sour, Salty],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, 7, electric, normal, 7, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, 7, steel, fairy],
        'pieces': number  
        },
    {
        'ingredient': 'Onion',
        'flavor': [2, 3, 1, 0, 0],
        'powers': [0, 4, 0, 0, -1, 0, 0, 0, 0, 7],
        'types': [0, 0, 0, 0, 0, ground, rock, 6, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': number  
        },
    {
        'ingredient': 'Noodles',
        'flavor': [0, 0, 0, 0, 4],
        'powers': [0, 0, 0, 0, 0, 0, 0, 21, -3, 12],
        'types': [0, 0, 0, 30, 0, 30, 30, 30, 0, 0, 30, 0, 0, 30, 0, 0, 0, 0],
        'pieces': 1  
        },
    {
        'ingredient': 'Lettuce',
        'flavor': [1, 0, 2, 0, 0],
        'powers': [0, 4, 0, 0, -1, 0, 0, 0, 0, 7],
        'types': [0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'pieces': number  
        },
    {
        'ingredient': 'Klawf Stick',
        'flavor': [4, 0, 0, 0, 4],
        'powers': [0, 4, 0, 0, -1, 0, 0, 0, 0, 7],
        'types': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
        'pieces': number  
        },
    {
        'ingredient': 'Kiwi',
        'flavor': [2, 0, 1, 5, 0],
        'powers': [4, -1, exp, 7, raid, title, sparkling, -5, teensy, encounter],
        'types': [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0],
        'pieces': number  
        },
    {
        'ingredient': 'Jalapeno',
        'flavor': [0, 5, 0, 2, 0],
        'powers': [4, -1, 0, 7, 0, 0, 0, -5, 0, 0],
        'types': [0, 7, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
        'pieces': number  
        },
    {
        'ingredient': 'Hamburger',
        'flavor': [6, 0, 9, 0, 12],
        'powers': [0, 12, 0, 0, -3, 0, 0, 0, 0, 21],
        'types': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0],
        'pieces': 1  
        },
    {
        'ingredient': 'Herbered Sausage',
        'flavor': [1, 0, 4, 0, 4],
        'powers': [0, 0, 7, -1, 0, 0, 0, 0, 0, 4],
        'types': [0, 0, 12, 0, 0, 12, 0, 12, 12, 0, 0, 0, 12, 0, 0, 12, 0, 0],
        'pieces': number 
        },
    {
        'ingredient': 'Ham',
        'flavor': [1, 0, 0, 0, 5],
        'powers': [0, 4, 0, 0, -1, 0, 0, 0, 0, 7],
        'types': [0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'pieces': number  
        },
    {
        'ingredient': 'Green Bell Pepper',
        'flavor': [1, 0, 5, 1, 0],
        'powers': [0, 4, 0, 0, -1, 0, 0, 0, 0, 7],
        'types': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
        'pieces': 3  
        },
    {
        'ingredient': 'Fried Fillet',
        'flavor': [2, 0, 3, 0, 3],
        'powers': [0, 21, 0, 0, 12, 0, 0, 0, 0, -3],
        'types': [0, 0, 20, 20, 20, 20, 0, 0, 0, 20, 20, 20, 0, 0, 0, 20, 20, 0],
        'pieces': number  
        },
    {
        'ingredient': 'Egg',
        'flavor': [1, 0, 1, 0, 2],
        'powers': [0, 0, 7, -1, 0, 0, 0, 0, 0, 4],
        'types': [0, 12, 0, 0, 0, 0, 12, 0, 0, 12, 12, 0, 0, 0, 0, 0, 12, 12],
        'pieces': number  
        },
    {
        'ingredient': 'Cucumber',
        'flavor': [0, 0, 1, 1, 0],
        'powers': [0, 4, 0, 0, -1, 0, 0, 0, 0, 7],
        'types': [0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'pieces': number  
        },
    {
        'ingredient': 'Chorizo',
        'flavor': [0, 4, 2, 0, 4],
        'powers': [0, 0, 7, -1, 0, 0, 0, 0, 0, 4],
        'types': [12, 0, 0, 12, 12, 0, 0, 0, 0, 0, 0, 12, 0, 12, 12, 0, 0, 0],
        'pieces': number  
        },
    {
        'ingredient': 'Cherry Tomatoes',
        'flavor': [3, 0, 1, 5, 0],
        'powers': [0, 4, 0, 0, -1, 0, 0, 0, 0, 7],
        'types': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
        'pieces': number  
        },
    {
        'ingredient': 'Cheese',
        'flavor': [1, 0, 0, 0, 3],
        'powers': [0, 2, 2, 2, 0, 0, 0, 0, 0, -2],
        'types': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        'pieces': 3  
        },
    {
        'ingredient': 'Basil',
        'flavor': [0, 0, 4, 1, 1],
        'powers': [2, 0, 0, 0, 2, 0, 0, 0, 0, -2],
        'types': [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        'pieces': 4  
        },
    {
        'ingredient': 'Banana',
        'flavor': [4, 0, 0, 1, 0],
        'powers': [4, -1, 0, 7, 0, 0, 0, -5, 0, 0],
        'types': [0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0],
        'pieces': 3
        },
    {
        'ingredient': 'Bacon',
        'flavor': [1, 0, 4, 1, 5],
        'powers': [0, 4, 0, 0, -1, 0, 0, 0, 0, 7],
        'types': [0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'pieces': number
        },
    {
        'ingredient': 'Avocado',
        'flavor': [3, 0, 1, 0, 0],
        'powers': [0, 4, 0, 0, -1, 0, 0, 0, 0, 7],
        'types': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0],
        'pieces': number
        },
    {
        'ingredient': 'Apple',
        'flavor': [4, 0, 1, 3, 0],
        'powers': [4, -1, 0, 7, 0, 0, 0, -5, 0, 0],
        'types': [0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 7, 0],
        'pieces': 3
        },
    ]
exit(0)
#List of ingredients
seasonings = [
##    {
##        'seasoning': 'name',
##        'flavor': [Sweet, Spicy, Bitter, Sour, Salty],
##        'powers': [egg, catching, exp, item, raid, title, sparkling, humungo, teensy, encounter],
##        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy]
##        },
    {
        'seasoning': 'null',
        'flavor': [Sweet, Spicy, Bitter, Sour, Salty],
        'powers': [egg, catching, exp, item, raid, 0, 0, humungo, teensy, encounter],
        'types': herba_mistica_type_list
        },
    {
        'seasoning': 'Sweet Herba Mystica',
        'flavor': [500, Spicy, Bitter, Sour, Salty],
        'powers': [egg, catching, exp, item, raid, 1000, 1000, humungo, teensy, encounter],
        'types': herba_mistica_type_list
        },
    {
        'seasoning': 'Sour Herba Mystica',
        'flavor': [Sweet, Spicy, Bitter, 500, Salty],
        'powers': [egg, catching, exp, item, raid, 1000, 1000, humungo, teensy, encounter],
        'types': herba_mistica_type_list
        },
    {
        'seasoning': 'Salty Herba Mystica',
        'flavor': [Sweet, 0, Bitter, Sour, 500],
        'powers': [egg, catching, exp, item, raid, 1000, 1000, humungo, teensy, encounter],
        'types': herba_mistica_type_list
        },
    {
        'seasoning': 'Spicy Herba Mystica',
        'flavor': [Sweet, 500, Bitter, Sour, Salty],
        'powers': [egg, catching, exp, item, raid, 1000, 1000, humungo, teensy, encounter],
        'types': herba_mistica_type_list
        },
    {
        'seasoning': 'Bitter Herba Mystica',
        'flavor': [Sweet, Spicy, 500, Sour, Salty],
        'powers': [egg, catching, exp, item, raid, 1000, 1000, humungo, teensy, encounter],
        'types': herba_mistica_type_list
        },
    {
        'seasoning': 'Yogurt',
        'flavor': [16, Spicy, Bitter, 16, Salty],
        'powers': [-3, catching, 12, item, 21, title, sparkling, humungo, teensy, encounter],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, 2, steel, 2]
        },
    {
        'seasoning': 'Wasabi',
        'flavor': [4, 20, Bitter, Sour, 4],
        'powers': [egg, catching, exp, item, raid, title, sparkling, -3, 21, 12],
        'types': [fire, grass, water, 2, normal, ground, rock, 2, ghost, flying, 2, bug, fighting, poison, 2, 2, steel, 2]
        },
    {
        'seasoning': 'Vinegar',
        'flavor': [4, Spicy, 4, 20, Salty],
        'powers': [5, catching, -3, 12, raid, title, sparkling, humungo, -15, encounter],
        'types': [fire, grass, water, electric, normal, ground, rock, 4, ghost, flying, ice, bug, fighting, poison, 4, dark, steel, 4]
        },
    {
        'seasoning': 'Salt',
        'flavor': [Sweet, Spicy, 4, Sour, 20],
        'powers': [-3, catching, 12, item, 21, title, sparkling, humungo, teensy, encounter],
        'types': [fire, grass, water, 2, normal, ground, rock, 2, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy]
        },
    {
        'seasoning': 'Pepper',
        'flavor': [Sweet, 16, 8, Sour, 4],
        'powers': [-3, catching, 12, item, 21, title, sparkling, humungo, teensy, encounter],
        'types': [fire, grass, water, 0, normal, ground, rock, 0, ghost, flying, 2, bug, fighting, poison, 2, dark, steel, fairy]
        },
    {
        'seasoning': 'Peanut Butter',
        'flavor': [16, Spicy, Bitter, Sour, 12],
        'powers': [-3, catching, 12, item, 21, title, sparkling, humungo, teensy, encounter],
        'types': [2, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, 2, fairy]
        },
    {
        'seasoning': 'Olive Oil',
        'flavor': [Sweet, 4, Bitter, 4, Salty],
        'powers': [5, catching, -3, 12, raid, title, sparkling, humungo, -15, encounter],
        'types': [4, 4, water, electric, normal, ground, rock, psychic, 4, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy]
        },
    {
        'seasoning': 'Mustard',
        'flavor': [4, 16, 8, 8, 8],
        'powers': [-3, catching, 12, item, 21, title, sparkling, humungo, teensy, encounter],
        'types': [fire, grass, water, electric, normal, 2, 2, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy]
        },
    {
        'seasoning': 'Mayonnaise',
        'flavor': [Sweet, Spicy, Bitter, 20, 8],
        'powers': [-3, catching, 12, item, 21, title, sparkling, humungo, teensy, encounter],
        'types': [fire, grass, water, electric, 2, ground, rock, psychic, ghost, flying, ice, bug, 2, poison, dragon, dark, steel, fairy]
        },
    {
        'seasoning': 'Marmalade',
        'flavor': [12, Spicy, 20, 16, 4],
        'powers': [5, catching, -3, 12, raid, title, sparkling, humungo, -15, encounter],
        'types': [fire, grass, water, electric, normal, ground, 4, psychic, ghost, flying, ice, bug, 4, 4, dragon, dark, steel, fairy]
        },
    {
        'seasoning': 'Ketchup',
        'flavor': [8, Spicy, Bitter, 16, 16],
        'powers': [-3, catching, 12, item, 21, title, sparkling, humungo, teensy, encounter],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, 2, ice, bug, fighting, 2, dragon, dark, steel, fairy]
        },
    {
        'seasoning': 'Jam',
        'flavor': [16, Spicy, Bitter, 16, 4],
        'powers': [5, catching, -3, 12, raid, title, sparkling, humungo, -15, encounter],
        'types': [fire, grass, water, 4, normal, ground, rock, psychic, ghost, flying, 4, bug, fighting, poison, dragon, 4, steel, fairy]
        },
    {
        'seasoning': 'Horseradish',
        'flavor': [4, 16, Bitter, Sour, Salty],
        'powers': [egg, catching, exp, item, raid, title, sparkling, -3, 21, 12],
        'types': [fire, grass, water, electric, 2, 2, 2, psychic, ghost, 2, ice, bug, 2, 2, dragon, dark, steel, fairy]
        },
    {
        'seasoning': 'Curry Powder',
        'flavor': [4, 30, 12, 4, 4],
        'powers': [egg, catching, exp, item, raid, title, sparkling, -3, 21, 12],
        'types': [2, 2, 2, electric, normal, ground, rock, psychic, 2, flying, ice, 2, 0, 0, dragon, dark, 2, fairy]
        },
    {
        'seasoning': 'Cream Cheese',
        'flavor': [12, Spicy, Bitter, 12, 12],
        'powers': [5, catching, -3, 12, raid, title, sparkling, humungo, -15, encounter],
        'types': [fire, grass, 4, electric, normal, ground, rock, psychic, ghost, flying, ice, 4, fighting, poison, dragon, dark, 4, fairy]
        },
    {
        'seasoning': 'Chili Sauce',
        'flavor': [8, 20, Bitter, 8, 12],
        'powers': [-3, catching, 12, item, 21, title, sparkling, humungo, teensy, encounter],
        'types': [fire, 2, 2, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy]
        },
    {
        'seasoning': 'Butter',
        'flavor': [12, Spicy, Bitter, Sour, 12],
        'powers': [-3, catching, 12, item, 21, title, sparkling, humungo, teensy, encounter],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, 2, flying, ice, 2, fighting, poison, dragon, dark, steel, fairy]
        },
    ]

in_game_sandwhiche_ingredient_combinations = [
    ['Ham', 'Butter'],
    ['Ham', 'Butter', 'Bitter Herba Mystica'],
    ['Ham', 'Butter', 'Sweet Herba Mystica'],
    ['Ham', 'Butter', 'Salty Herba Mystica'],
    ['Ham', 'Butter', 'Sour Herba Mystica'],
    ['Ham', 'Butter', 'Spicy Herba Mystica'],
    ['Lettuce', 'Bacon', 'Pepper', 'Bitter Herba Mystica'],
    ['Lettuce', 'Bacon', 'Pepper', 'Salty Herba Mystica'],
    ['Lettuce', 'Bacon', 'Pepper', 'Sweet Herba Mystica'],
    ['Lettuce', 'Bacon', 'Pepper', 'Sour Herba Mystica'],
    ['Lettuce', 'Bacon', 'Pepper', 'Spicy Herba Mystica'],
    ['Strawberry', 'Jam'],
    ['Strawberry', 'Jam', 'Yogurt'],
    ['Strawberry', 'Pineapple', 'Jam', 'Yogurt'],
    ['Strawberry', 'Pineapple', 'Jam', 'Yogurt', 'Sweet Herba Mystica'],
    ['Banana', 'Peanut Butter'],
    ['Banana', 'Peanut Butter', 'Butter'],
    ['Banana', 'Peanut Butter', 'Butter', 'Jam'],
    ['Banana', 'Peanut Butter', 'Butter', 'Jam', 'Spicy Herba Mystica'],
    ['Pickle', 'Olive Oil'],
    ['Pickle', 'Watercress', 'Olive Oil'],
    ['Pickle', 'Watercress', 'Basil', 'Olive Oil'],
    ['Pickle', 'Watercress', 'Basil', 'Olive Oil', 'Sour Herba Mystica'],
    
    ]



def remove_stuff(string):
    string = str(string)
    print(string)
    string = string.replace(">Butter<",'')
    string = string.replace(">Pepper<",'')
    string = string.replace(">Jam<",'')
    string = string.replace(">Yogurt<",'')
    string = string.replace(">Peanut Butter<",'')
    string = string.replace(">Olive Oil<",'')
    string = string.replace(">Wasabi<",'')
    string = string.replace(">Marmalade<",'')
    string = string.replace(">Cream Cheese<",'')
    string = string.replace(">Ketchup<",'')
    string = string.replace(">Mustard<",'')
    string = string.replace(">Curry Powder<",'')
    string = string.replace(">Mayonnaise<",'')
    string = string.replace(">Whipped Cream<",'')
    string = string.replace(">Salt<",'')
    string = string.replace(">Chili Sauce<",'')
    string = string.replace(">Horseradish<",'')
    string = string.replace(">Vinegar<",'')
    string = string.replace(">Bitter Herba Mystica<",'')
    string = string.replace(">Sweet Herba Mystica<",'')
    string = string.replace(">Sour Herba Mystica<",'')
    string = string.replace(">Salty Herba Mystica<",'')
    string = string.replace(">Spicy Herba Mystica<",'')
    string = string.replace('/a>','')
    string = string.replace('<','')
    string = string.replace('PageElement','')
    string = string.replace('get_text of','')
    string = string.replace('>','')
    string = string.replace('td class="fooinfo" rowspan="2"','')
    string = string.replace('table','')
    string = string.replace('tr','')
    string = string.replace('td','')
    string = string.replace('a href=','')
    string = string.replace('"','')
    string = string.replace('item','')
    string = string.replace('dex','')
    string = string.replace('butter','')
    string = string.replace('.','')
    string = string.replace('alt','')
    string = string.replace('height','')
    string = string.replace('=','')
    string = string.replace('0','')
    string = string.replace('1','')
    string = string.replace('2','')
    string = string.replace('3','')
    string = string.replace('4','')
    string = string.replace('5','')
    string = string.replace('6','')
    string = string.replace('7','')
    string = string.replace('8','')
    string = string.replace('9','')
    string = string.replace('loading','')
    string = string.replace('lazy','')
    string = string.replace('//','')
    string = string.replace('sprites','')
    string = string.replace('sprite','')
    string = string.replace('png','')
    string = string.replace('bitterherbamystica','')
    string = string.replace('shtml','')
    string = string.replace('img','')
    string = string.replace('png','')
    string = string.replace('bound','')
    string = string.replace('method','')
    string = string.replace('src','')
    string = string.replace('//Butter','')
    string = string.replace('//Bitter Herba Mystica','')
    string = string.replace("/",'')
    string = string.replace("/Butter",'')
    string = string.replace("/Bitter Herba Mystica",'')
    string = string.replace("    ",',')
    string = string.strip()
    return string

#pokemon checker
def Pokemon():
    for ingredient_one_index in range(0, len(ingredients)):
        for seasoning_one_index in range(0, len(seasonings)):
            for seasoning_two_index in range(0, len(seasonings)):
                for seasoning_three_index in range(0, len(seasonings)):
                    for seasoning_four_index in range(1, len(seasonings)):
                        for ingredient_two_index in range(0, len(ingredients)):
                            for ingredient_three_index in range(0, len(ingredients)):
                                for ingredient_four_index in range(0, len(ingredients)):
                                    for ingredient_five_index in range(0, len(ingredients)):
                                        for ingredient_six_index in range(0, len(ingredients)):
                                            pass
    return 11037


        
if __name__ == '__main__':
    Pokemon()








