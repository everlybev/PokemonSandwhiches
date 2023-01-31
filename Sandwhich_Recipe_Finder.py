import time
from datetime import datetime
import os
from os.path import exists
from sys import argv


def element_wise_addition(list_one, list_two):
##    print(list_one)
##    print(list_two)
    #both lists must be the same legnth
    resulting_list = []
    if len(list_one) == 1:
        for i in range(0, len(list_two)):
            resulting_list.append(list_one[0]+list_two[i])
    else:
        for i in range(len(list_one)-len(list_two), len(list_one)):
            resulting_list.append(list_one[i]+list_two[i])
    return resulting_list

def element_wise_multiplication(first, second):
    resulting_list = []
    if len(first) == 1:
        for i in range(0, len(second)):
            resulting_list.append(first[0]*second[i])
    else:
        for i in range(len(first)-len(second), len(first)):
            resulting_list.append(first[i]+second[i])
    return resulting_list

def build_sandwich(one, two, three, four, five, six, seven, eight, nine, ten):
    recipe_list_of_stuff = []
    if ((one.get('seasoning', 'not this') == 'null') or (one.get('ingredient', 'not this') == 'null') or (one.get('ingredient', 'not this') == 'Null')):
        pass
    else:
        recipe_list_of_stuff.append(one)
    if ((two.get('seasoning', 'not this') == 'null') or (two.get('ingredient', 'not this') == 'null') or (two.get('ingredient', 'not this') == 'Null')):
        pass
    else:
        recipe_list_of_stuff.append(two)
    if ((three.get('seasoning', 'not this') == 'null') or (three.get('ingredient', 'not this') == 'null') or (three.get('ingredient', 'not this') == 'Null')):
        pass
    else:
        recipe_list_of_stuff.append(three)
    if ((four.get('seasoning', 'not this') == 'null') or (four.get('ingredient', 'not this') == 'null') or (four.get('ingredient', 'not this') == 'Null')):
        pass
    else:
        recipe_list_of_stuff.append(four)
    if ((five.get('seasoning', 'not this') == 'null') or (five.get('ingredient', 'not this') == 'null') or (five.get('ingredient', 'not this') == 'Null')):
        pass
    else:
        recipe_list_of_stuff.append(five)
    if ((six.get('seasoning', 'not this') == 'null') or (six.get('ingredient', 'not this') == 'null') or (six.get('ingredient', 'not this') == 'Null')):
        pass
    else:
        recipe_list_of_stuff.append(six)
    if ((seven.get('seasoning', 'not this') == 'null') or (seven.get('ingredient', 'not this') == 'null') or (seven.get('ingredient', 'not this') == 'Null')):
        pass
    else:
        recipe_list_of_stuff.append(seven)
    if ((eight.get('seasoning', 'not this') == 'null') or (eight.get('ingredient', 'not this') == 'null') or (eight.get('ingredient', 'not this') == 'Null')):
        pass
    else:
        recipe_list_of_stuff.append(eight)
    if ((nine.get('seasoning', 'not this') == 'null') or (nine.get('ingredient', 'not this') == 'null') or (nine.get('ingredient', 'not this') == 'Null')):
        pass
    else:
        recipe_list_of_stuff.append(nine)
    if ((ten.get('seasoning', 'not this') == 'null') or (ten.get('ingredient', 'not this') == 'null') or (ten.get('ingredient', 'not this') == 'Null')):
        pass
    else:
        recipe_list_of_stuff.append(ten)
    #recipe_list_of_stuff.sort()
    #print(recipe_list_of_stuff)
##    print()
##    print()
    return recipe_list_of_stuff

number = 9
Sweet = 0
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
#print(herba_mistica_type_list)
#exit(0)

#lists of stuff
flavor_names_list = ['Sweet', 'Spicy', 'Bitter', 'Sour', 'Salty']
powers_names_list = ['egg', 'catching', 'exp', 'item', 'raid', 'title', 'sparkling', 'humungo', 'teensy', 'encounter']
types_names_list = ['fire', 'grass', 'water', 'electric', 'normal', 'ground', 'rock', 'psychic', 'ghost', 'flying', 'ice', 'bug', 'fighting', 'poison', 'dragon', 'dark', 'steel', 'fairy']

in_game_flavor_names_list_in_order = ['Sweet', 'Salty', 'Sour', 'Bitter', 'Spicy']
in_game_powers_names_list_in_order = ['egg', 'catching', 'item', 'humungo', 'teensy', 'raid', 'encounter', 'exp', 'title', 'sparkling']
in_game_types_names_list_in_order = ['normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy']


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
        'pieces': 3
        },
    {
        'ingredient': 'Tomato',
        'flavor': [2, Spicy, 1, 4, Salty],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, 6],
        'pieces': 3  
        },
    {
        'ingredient': 'Tofu',
        'flavor': [3, Spicy, Bitter, Sour, Salty],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, water, electric, 6, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': 3  
        },
    {
        'ingredient': 'Strawberry',
        'flavor': [4, Spicy, Bitter, 4, Salty],
        'powers': [4, -1, exp, 7, raid, title, sparkling, -5, teensy, encounter],
        'types': [fire, grass, water, electric, normal, ground, rock, 7, 7, flying, ice, bug, 7, poison, dragon, dark, steel, fairy],
        'pieces': 3  
        },
    {
        'ingredient': 'Smoked Fillet',
        'flavor': [1, Spicy, 3, 2, 3],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, 6, steel, fairy],
        'pieces': 3  
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
        'pieces': 3  
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
        'pieces': 3  
        },
    {
        'ingredient': 'Potato Tortilla',
        'flavor': [3, 1, 3, 1, 4],
        'powers': [egg, 21, exp, item, 12, title, sparkling, humungo, teensy, -3],
        'types': [20, 20, water, electric, normal, ground, 20, 20, 20, flying, ice, bug, 20, 20, 20, dark, steel, 20],
        'pieces': 1  
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
        'pieces': 3  
        },
    {
        'ingredient': 'Pickle',
        'flavor': [1, Spicy, 2, 4, Salty],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, 6, poison, dragon, dark, steel, fairy],
        'pieces': 3
        },
    {
        'ingredient': 'Onion',
        'flavor': [2, 3, 1, Sour, Salty],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [0, 0, 0, 0, 0, ground, rock, 6, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': 3  
        },
    {
        'ingredient': 'Noodles',
        'flavor': [Sweet, Spicy, Bitter, Sour, 4],
        'powers': [egg, catching, exp, item, raid, title, sparkling, 21, -1, 12],
        'types': [0, 0, 0, 30, 0, 30, 30, 30, 0, 0, 30, 0, 0, 30, 0, 0, 0, 0],
        'pieces': 1  
        },
    {
        'ingredient': 'Lettuce',
        'flavor': [1, Spicy, 2, Sour, Salty],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, 6, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': 3 
        },
    {
        'ingredient': 'Klawf Stick',
        'flavor': [4, Spicy, Bitter, Sour, 4],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, 6, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': 3
        },
    {
        'ingredient': 'Kiwi',
        'flavor': [2, 0, 1, 5, 0],
        'powers': [4, -1, exp, 7, raid, title, sparkling, -5, teensy, encounter],
        'types': [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0],
        'pieces': 3  
        },
    {
        'ingredient': 'Jalapeno',
        'flavor': [0, 5, 0, 2, 0],
        'powers': [4, -1, 0, 7, 0, 0, 0, -5, 0, 0],
        'types': [0, 7, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
        'pieces': 3  
        },
    {
        'ingredient': 'Hamburger',
        'flavor': [6, 0, 9, 0, 12],
        'powers': [0, 12, 0, 0, -3, 0, 0, 0, 0, 21],
        'types': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0],
        'pieces': 1  
        },
    {
        'ingredient': 'Herbed Sausage',
        'flavor': [1, 0, 4, 0, 4],
        'powers': [0, 0, 7, -1, 0, 0, 0, 0, 0, 4],
        'types': [0, 0, 12, 0, 0, 12, 0, 12, 12, 0, 0, 0, 12, 0, 0, 12, 0, 0],
        'pieces': 3 
        },
    {
        'ingredient': 'Ham',
        'flavor': [1, Spicy, Bitter, Sour, 5],
        'powers': [egg, 4, exp, item, -1, title, sparkling, humungo, teensy, 7],
        'types': [fire, grass, water, electric, normal, 6, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': 3
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
        'pieces': 1  
        },
    {
        'ingredient': 'Egg',
        'flavor': [1, 0, 1, 0, 2],
        'powers': [0, 0, 7, -1, 0, 0, 0, 0, 0, 4],
        'types': [0, 12, 0, 0, 0, 0, 12, 0, 0, 12, 12, 0, 0, 0, 0, 0, 12, 12],
        'pieces': 3  
        },
    {
        'ingredient': 'Cucumber',
        'flavor': [0, 0, 1, 1, 0],
        'powers': [0, 4, 0, 0, -1, 0, 0, 0, 0, 7],
        'types': [0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'pieces': 3  
        },
    {
        'ingredient': 'Chorizo',
        'flavor': [0, 4, 2, 0, 4],
        'powers': [0, 0, 7, -1, 0, 0, 0, 0, 0, 4],
        'types': [12, 0, 0, 12, 12, 0, 0, 0, 0, 0, 0, 12, 0, 12, 12, 0, 0, 0],
        'pieces': 3  
        },
    {
        'ingredient': 'Cherry Tomatoes',
        'flavor': [3, 0, 1, 5, 0],
        'powers': [0, 4, 0, 0, -1, 0, 0, 0, 0, 7],
        'types': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
        'pieces': 3  
        },
    {
        'ingredient': 'Cheese',
        'flavor': [1, Spicy, Bitter, Sour, 3],
        'powers': [egg, 2, 2, 2, raid, 0, 0, humungo, teensy, -6],
        'types': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        'pieces': 3  
        },
    {
        'ingredient': 'Basil',
        'flavor': [Sweet, Spicy, 4, 1, 1],
        'powers': [2, catching, exp, item, 2, 0, 0, humungo, teensy, 2],
        'types': [1, 1, 1, 1, normal, ground, rock, 1, ghost, flying, 1, bug, fighting, poison, 1, 1, steel, 1],
        'pieces': 4  
        },
    {
        'ingredient': 'Banana',
        'flavor': [4, Spicy, Bitter, 1, Salty],
        'powers': [4, -1, exp, 7, raid, 0, 0, -5, teensy, encounter],
        'types': [fire, grass, water, 7, 7, ground, rock, psychic, ghost, flying, ice, 7, fighting, poison, dragon, dark, steel, fairy],
        'pieces': 3
        },
    {
        'ingredient': 'Bacon',
        'flavor': [1, Spicy, 4, 1, 5],
        'powers': [egg, 4, exp, item, -1, 0, 0, humungo, teensy, 7],
        'types': [fire, grass, water, electric, normal, ground, 6, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
        'pieces': 3
        },
    {
        'ingredient': 'Avocado',
        'flavor': [3, Spicy, Bitter, 1, Salty],
        'powers': [egg, 4, exp, item, -1, 0, 0, humungo, teensy, 7],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, 6, dark, steel, fairy],
        'pieces': 3
        },
    {
        'ingredient': 'Apple',
        'flavor': [4, Spicy, 1, 3, Salty],
        'powers': [4, -1, exp, 7, raid, title, sparkling, -5, teensy, encounter],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, 7, 7, bug, fighting, poison, dragon, dark, 7, fairy],
        'pieces': 3  
        },
    ]
#exit(0)
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
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
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
        'powers': [egg, catching, exp, item, raid, 0, 0, -3, 21, 12],
        'types': [fire, grass, water, 2, normal, ground, rock, 2, ghost, flying, 2, bug, fighting, poison, 2, 2, steel, 2],
        },
    {
        'seasoning': 'Vinegar',
        'flavor': [4, Spicy, 4, 20, Salty],
        'powers': [5, catching, -3, 12, raid, 0, 0, humungo, -15, encounter],
        'types': [fire, grass, water, electric, normal, ground, rock, 4, ghost, flying, ice, bug, fighting, poison, 4, 0, 0, 4],
        },
    {
        'seasoning': 'Salt',
        'flavor': [Sweet, Spicy, 4, Sour, 20],
        'powers': [-3, catching, 12, item, 21, 0, 0, humungo, teensy, encounter],
        'types': [fire, grass, water, 2, normal, ground, rock, 2, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy],
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
        'flavor': [Sweet, Spicy, 4, 4, Salty],
        'powers': [5, catching, -3, 12, raid, 0, 0, humungo, -15, encounter],
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
        'powers': [egg, catching, exp, item, raid, 0, 0, -3, 21, 12],
        'types': [2, 2, 2, electric, normal, ground, rock, psychic, 2, flying, ice, 2, 0, 0, dragon, dark, 2, fairy]
        },
    {
        'seasoning': 'Cream Cheese',
        'flavor': [12, Spicy, Bitter, 12, 12],
        'powers': [5, catching, -3, 12, raid, 0, 0, humungo, -15, encounter],
        'types': [fire, grass, 4, electric, normal, ground, rock, psychic, ghost, flying, ice, 4, fighting, poison, dragon, dark, 4, fairy]
        },
    {
        'seasoning': 'Chili Sauce',
        'flavor': [8, 20, Bitter, 8, 12],
        'powers': [-3, catching, 12, item, 21, 0, 0, humungo, teensy, encounter],
        'types': [fire, 2, 2, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy]
        },
    {
        'seasoning': 'Butter',
        'flavor': [12, Spicy, Bitter, Sour, 12],
        'powers': [-3, catching, 12, item, 21, title, sparkling, humungo, teensy, encounter],
        'types': [fire, grass, water, electric, normal, ground, rock, psychic, 2, flying, ice, 2, fighting, poison, dragon, dark, steel, fairy]
        },
    ]


def get_item_type(something):
    #print(something)
    for dictionary in ingredients:
        if dictionary.get('ingredient') == something.get('ingredient'):
            return 'an ingredient'
    for dictionary in seasonings:
        if dictionary.get('seasoning') == something.get('seasoning'):
            return 'a seasoning'

def get_max_value(profile_list):
    if len(profile_list) == len(types_names_list):
        mapped_list = types_names_list
        mapped_in_game_list = in_game_types_names_list_in_order
    elif len(profile_list) == len(powers_names_list):
        mapped_list = powers_names_list
        mapped_in_game_list = in_game_powers_names_list_in_order
    elif len(profile_list) == len(flavor_names_list):
        mapped_list = flavor_names_list
        mapped_in_game_list = in_game_flavor_names_list_in_order
    else:
        print('profile = ' + str(profile_list))
        print('profile len does not match any name list len!')
    max_value = max(profile_list)
    list_of_max_profiles = []
    for i in range(0, len(profile_list)):
        if max_value == profile_list[i]:
            list_of_max_profiles.append(mapped_list[i])
    #Must fix. Ties are not handled alphabetically
    sorted_list = []
    for i in range(0, len(mapped_in_game_list)):
        for j in range(0, len(list_of_max_profiles)):
            if list_of_max_profiles[j] == mapped_in_game_list[i]:
                sorted_list.append(list_of_max_profiles[j])
    #print(sorted_list)
    return sorted_list[0], max_value
    
def top_value_removed(given_list, top_type):
    if top_type in types_names_list:
        liste = types_names_list
    elif top_type in powers_names_list:
        liste = powers_names_list
    elif top_type in flavor_names_list:
        liste = flavor_names_list
    else:
        print(str(top_type) + ' is not found in any profile lists')
        exit(0)
    the_index = liste.index(top_type)
    given_list[the_index] = -277353
    return given_list

def valTOlvl(valueT, valueS, valueTh):
    #It seems like the values to determine levels are the type values not the power values
##    print('powers:')
##    print(valueT, valueS, valueTh)
##    print('powers above')
    if valueT < 100:
        return 1, 1, 1
    elif(valueT >= 180) and (valueT <= 280):
        if (valueS >= 180) and (valueTh >= 180):
            return 2, 2, 1
        else:
            return 2, 1, 1
    elif (valueT > 280) and (valueT < 380):
        if valueTh >= 180:
            return 2, 2, 2
        else:
            return 2, 2, 1
    elif (valueT >= 380) and (valueT < 460):
        if (valueS >= 380) and (valueTh >= 380):
            return 3, 3, 3
        else:
            return 3, 3, 2
    elif valueT >= 460:
        return 3, 3, 3
    else:
        return 1, 1, 1

def get_the_final_types_and_values(top_t, top_tv, second_top_t, second_top_tv, third_top_t, third_top_tv):
    #print(top_t, top_tv, second_top_t, second_top_tv, third_top_t, third_top_tv)
    if top_tv > 480:
        return top_t, top_tv, top_t, top_tv, top_t, top_tv
    elif top_tv > 280:
        return top_t, top_tv, top_t, top_tv, third_top_t, third_top_tv
    else:
        final_types_and_values_list = top_t, top_tv, third_top_t, third_top_tv, second_top_t, second_top_tv
        weird_fucking_bullshit = False
        diff_or_whatever = top_tv - second_top_tv
        if (top_tv > 105) and ((top_tv - second_top_tv) > 105):
            final_types_and_values_list = top_t, top_tv, top_t, top_tv, third_top_t, third_top_tv
        elif (top_tv >= 100) and (top_tv <= 105):
            if (diff_or_whatever >= 80) and (second_top_tv <= 21):
                weird_fucking_bullshit = True
        elif (top_tv >= 90) and (top_tv < 100):
            if (diff_or_whatever >= 78) and (second_top_tv <= 16):
                weird_fucking_bullshit = True
        elif (top_tv >= 80) and (top_tv < 90):
            if (diff_or_whatever >= 74) and (second_top_tv <= 9):
                weird_fucking_bullshit = True
        elif (top_tv >= 74) and (top_tv < 80):
            if (diff_or_whatever >= 72) and (second_top_tv <= 5):
                weird_fucking_bullshit = True
        if weird_fucking_bullshit:
            return top_t, top_tv, third_top_t, third_top_tv, top_t, top_tv
        else:
            return final_types_and_values_list


def determine_powers(a_list):
    total_flavor = [Sweet, Spicy, Bitter, Sour, Salty]
    total_powers = [egg, catching, exp, item, raid, title, sparkling, humungo, teensy, encounter]
    total_types = [fire, grass, water, electric, normal, ground, rock, psychic, ghost, flying, ice, bug, fighting, poison, dragon, dark, steel, fairy]
    #print(a_list)
    for element in a_list:
        #print(element)
        item_type = get_item_type(element)
        #print(item_type)
        if item_type == 'an ingredient':
            for dictionary in ingredients:
                if dictionary.get('ingredient') == element.get('ingredient'):
                    flavor_profile = dictionary.get('flavor')
                    power_profile = dictionary.get('powers')
                    type_profile = dictionary.get('types')
                    pieces = [dictionary.get('pieces')]
                    #break
            
        elif item_type == 'a seasoning':
            pieces = [1]
            for dictionary in seasonings:
                if dictionary.get('seasoning') == element.get('seasoning'):
                    #print('in')
                    flavor_profile = dictionary.get('flavor')
                    power_profile = dictionary.get('powers')
                    type_profile = dictionary.get('types')
                    #break
                
        flavor_profile = element_wise_multiplication(pieces, flavor_profile)
        power_profile = element_wise_multiplication(pieces, power_profile)
        type_profile = element_wise_multiplication(pieces, type_profile)
        
        total_flavor = element_wise_addition(total_flavor, flavor_profile)
        total_powers = element_wise_addition(total_powers, power_profile)
        total_types = element_wise_addition(total_types, type_profile)

    top_flavor, top_flavor_value = get_max_value(total_flavor)
    total_flavor = top_value_removed(total_flavor, top_flavor)
    second_top_flavor, second_top_flavor_value = get_max_value(total_flavor)
    #Check for flavor bonuses
##    print(top_flavor)
##    print(second_top_flavor)
    if (([top_flavor, second_top_flavor] == ['Sweet', 'Sour']) or ([top_flavor, second_top_flavor] == ['Sour', 'Sweet'])):
        total_powers[1] = 100 + total_powers[1]
    elif (([top_flavor, second_top_flavor] == ['Salty', 'Bitter']) or ([top_flavor, second_top_flavor] == ['Bitter', 'Salty'])):
        total_powers[2] = 100 + total_powers[2]
    elif (([top_flavor, second_top_flavor] == ['Sweet', 'Spicy']) or ([top_flavor, second_top_flavor] == ['Spicy', 'Sweet'])):
        total_powers[4] = 100 + total_powers[4]
    elif (str(top_flavor) == "Sweet"):
        total_powers[0] = 100 + total_powers[0]
    elif (top_flavor == 'Spicy'):
        total_powers[7] = 100 + total_powers[7]
    elif (top_flavor == 'Bitter'):
        total_powers[3] = 100 + total_powers[3]
    elif (top_flavor == 'Sour'):
        total_powers[8] = 100 + total_powers[8]
    elif (top_flavor == 'Salty'):
        total_powers[9] = 100 + total_powers[9]
    else:
        print('something got fuked up')

    #print(total_powers)
    top_power, top_power_value = get_max_value(total_powers)
    total_powers = top_value_removed(total_powers, top_power)
    second_top_power, second_top_power_value = get_max_value(total_powers)
    total_powers = top_value_removed(total_powers, second_top_power)
    third_top_power, third_top_power_value = get_max_value(total_powers)
    total_powers = top_value_removed(total_powers, third_top_power)
    fourth_top_power, fourth_top_power_value = get_max_value(total_powers)
    #Deal with sparkle crap
    if (top_power == 'sparkling') and (top_power_value < 2000):
        #Sparkling Power can only be lvl 3 I think
        top_power, top_power_value = second_top_power, second_top_power_value
        second_top_power, second_top_power_value = third_top_power, third_top_power_value
        third_top_power, third_top_power_value = fourth_top_power, fourth_top_power_value
    if (second_top_power == 'sparkling') and (second_top_power_value < 2000):
        second_top_power, second_top_power_value = third_top_power, third_top_power_value
        third_top_power, third_top_power_value = fourth_top_power, fourth_top_power_value
##    print(top_power)
##    print(top_power_value)
##    print(second_top_power)
##    print(second_top_power_value)
##    print(third_top_power)
##    print(third_top_power_value)
##    print(fourth_top_power)
##    print(fourth_top_power_value)
##    print(total_types)
    top_type, top_type_value = get_max_value(total_types)
    total_types = top_value_removed(total_types, top_type)
    second_top_type, second_top_type_value = get_max_value(total_types)
    total_types = top_value_removed(total_types, second_top_type)
    third_top_type, third_top_type_value = get_max_value(total_types)
    total_types = top_value_removed(total_types, third_top_type)

    #print(top_type, top_type_value, second_top_type, second_top_type_value, third_top_type, third_top_type_value)
    top_type, top_type_value, second_top_type, second_top_type_value, third_top_type, third_top_type_value = get_the_final_types_and_values(top_type,
                                                                                                                                            top_type_value,
                                                                                                                                            second_top_type,
                                                                                                                                            second_top_type_value,
                                                                                                                                            third_top_type,
                                                                                                                                            third_top_type_value
                                                                                                                                            )
    #print(top_type, top_type_value, second_top_type, second_top_type_value, third_top_type, third_top_type_value)
    
    top_power_level, second_top_power_level, third_top_power_level = valTOlvl(top_type_value, second_top_type_value, third_top_type_value)
##    second_top_power_level = valTOlvl(second_top_power_value)
##    third_top_power_level = valTOlvl(third_top_power_value)
    
    if [top_power, second_top_power] == ['sparkling', 'title'] or [top_power, second_top_power] == ['title', 'sparkling']:
        if third_top_power == 'egg':
            the_list_of_things =  [
                [top_power, top_power_level, top_type],
                [second_top_power, second_top_power_level, second_top_type],
                [third_top_power, third_top_power_level, ' '] #this is egg
                ]
        else:
            the_list_of_things =  [
                [top_power, top_power_level, top_type],
                [second_top_power, second_top_power_level, second_top_type],
                [third_top_power, third_top_power_level, third_top_type] #none are eggs; title/sparkle are tops along with third
                ]
    elif [top_power] == ['title']:
        if second_top_power == 'egg':
            the_list_of_things =  [
                [top_power, top_power_level, top_type],
                [second_top_power, second_top_power_level, ' '],
                [third_top_power, third_top_power_level, third_top_type] #this is egg
                ]
        elif third_top_power == 'egg':
            the_list_of_things =  [
                [top_power, top_power_level, top_type],
                [second_top_power, second_top_power_level, second_top_type],
                [third_top_power, third_top_power_level, ' '] #this is egg
                ]
        else:
            the_list_of_things =  [
                [top_power, top_power_level, top_type],
                [second_top_power, second_top_power_level, second_top_type],
                [third_top_power, third_top_power_level, third_top_type] #none are eggs; title/sparkle are tops along with third
                ]
    else:
        the_list_of_things =  [
            [top_power, top_power_level, top_type],
            [second_top_power, second_top_power_level, second_top_type],
            [third_top_power, third_top_power_level, third_top_type]
            ]
        if top_power == 'egg':
            the_list_of_things =  [
                [top_power, top_power_level, ' '],
                [second_top_power, second_top_power_level, second_top_type],
                [third_top_power, third_top_power_level, third_top_type]
                ]
        elif second_top_power == 'egg':
            the_list_of_things =  [
                [top_power, top_power_level, top_type],
                [second_top_power, second_top_power_level, ' '],
                [third_top_power, third_top_power_level, third_top_type]
                ]
        elif third_top_power == 'egg':
            the_list_of_things =  [
                [top_power, top_power_level, top_type],
                [second_top_power, second_top_power_level, second_top_type],
                [third_top_power, third_top_power_level, ' ']
                ]
    for each in the_list_of_things:
        if each[0] == 'egg':
            each[2] = ' '
    return the_list_of_things
        
     


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
    ['Cheese', 'Marmalade'],
    ['Cheese', 'Marmalade', 'Butter'],
    ['Cheese', 'Marmalade', 'Butter', 'Cream Cheese'],
    ['Cheese', 'Marmalade', 'Butter', 'Cream Cheese', 'Salty Herba Mystica'],
    ['Herbed Sausage', 'Ketchup'],
    ['Herbed Sausage', 'Ketchup', 'Mustard'],
    ['Herbed Sausage', 'Lettuce', 'Ketchup', 'Mustard'],
    ['Herbed Sausage', 'Lettuce', 'Ketchup', 'Mustard', 'Bitter Herba Mystica'],
    ['Rice', 'Curry Powder', 'Mayonnaise'],
    ['Rice', 'Jalapeno', 'Curry Powder', 'Mayonnaise'],
    ['Rice', 'Jalapeno', 'Tomato', 'Curry Powder', 'Mayonnaise'],
    ['Rice', 'Jalapeno', 'Tomato', 'Curry Powder', 'Mayonnaise', 'Spicy Herba Mystica'],
    ['Apple', 'Apple', 'Whipped Cream', 'Yogurt'],
    ['Apple', 'Apple', 'Kiwi', 'Whipped Cream', 'Yogurt'],
    ['Apple', 'Apple', 'Kiwi', 'Strawberry', 'Whipped Cream', 'Yogurt'],
    ['Apple', 'Apple', 'Kiwi', 'Strawberry', 'Whipped Cream', 'Yogurt', 'Sweet Herba Mystica'],
    ['Klawf Stick', 'Avocado', 'Marmalade'],
    ['Klawf Stick', 'Avocado', 'Pineapple', 'Marmalade'],
    ['Klawf Stick', 'Avocado', 'Pineapple', 'Jalapeno', 'Marmalade'],
    ['Klawf Stick', 'Avocado', 'Pineapple', 'Jalapeno', 'Marmalade', 'Sour Herba Mystica'],
    ['Avocado', 'Smoked Fillet', 'Salt'],
    ['Avocado', 'Smoked Fillet', 'Tomato', 'Salt'],
    ['Avocado', 'Smoked Fillet', 'Tomato', 'Lettuce', 'Salt'],
    ['Avocado', 'Smoked Fillet', 'Tomato', 'Lettuce', 'Salt', 'Salty Herba Mystica'],
    ['Noodles', 'Olive Oil', 'Ketchup'],
    ['Noodles', 'Lettuce', 'Olive Oil', 'Ketchup'],
    ['Noodles', 'Lettuce', 'Chorizo', 'Olive Oil', 'Ketchup'],
    ['Noodles', 'Lettuce', 'Chorizo', 'Olive Oil', 'Ketchup', 'Bitter Herba Mystica'],
    ['Potato Salad', 'Cucumber', 'Red Bell Pepper', 'Mayonnaise'],
    ['Potato Salad', 'Cucumber', 'Red Bell Pepper', 'Avocado', 'Mayonnaise'],
    ['Potato Salad', 'Cucumber', 'Red Bell Pepper', 'Avocado', 'Red Onion', 'Mayonnaise'],
    ['Potato Salad', 'Cucumber', 'Red Bell Pepper', 'Avocado', 'Red Onion', 'Mayonnaise', 'Sweet Herba Mystica'],
    ['Jalapeno', 'Onion', 'Herbed Sausage', 'Chili Sauce'],
    ['Jalapeno', 'Onion', 'Herbed Sausage', 'Green Bell Pepper', 'Chili Sauce'],
    ['Jalapeno', 'Onion', 'Herbed Sausage', 'Green Bell Pepper', 'Watercress', 'Chili Sauce'],
    ['Jalapeno', 'Onion', 'Herbed Sausage', 'Green Bell Pepper', 'Watercress', 'Chili Sauce', 'Sour Herba Mystica'],
    ['Egg', 'Cucumber', 'Salt', 'Mayonnaise'],
    ['Egg', 'Cucumber', 'Red Onion', 'Salt', 'Mayonnaise'],
    ['Egg', 'Cucumber', 'Red Onion', 'Cheese', 'Salt', 'Mayonnaise'],
    ['Egg', 'Cucumber', 'Red Onion', 'Cheese', 'Salt', 'Mayonnaise', 'Salty Herba Mystica'],
    ['Prosciutto', 'Cheese', 'Potato Tortilla', 'Olive Oil'],
    ['Prosciutto', 'Cheese', 'Potato Tortilla', 'Olive Oil', 'Curry Powder'],
    ['Prosciutto', 'Cheese', 'Potato Tortilla', 'Avocado', 'Olive Oil', 'Curry Powder'],
    ['Prosciutto', 'Cheese', 'Potato Tortilla', 'Avocado', 'Olive Oil', 'Curry Powder', 'Bitter Herba Mystica'],
    ['Cherry Tomatoes', 'Avocado', 'Marmalade', 'Salt'],
    ['Cherry Tomatoes', 'Avocado', 'Kiwi', 'Marmalade', 'Salt'],
    ['Cherry Tomatoes', 'Avocado', 'Kiwi', 'Pickle', 'Marmalade', 'Salt'],
    ['Cherry Tomatoes', 'Avocado', 'Kiwi', 'Pickle', 'Marmalade', 'Salt', 'Salty Herba Mystica'],
    ['Bacon', 'Lettuce', 'Tomato', 'Mayonnaise', 'Mustard'],
    ['Bacon', 'Lettuce', 'Tomato', 'Basil', 'Mayonnaise', 'Mustard'],
    ['Bacon', 'Lettuce', 'Tomato', 'Basil', 'Cheese', 'Mayonnaise', 'Mustard'],
    ['Bacon', 'Lettuce', 'Tomato', 'Basil', 'Cheese', 'Mayonnaise', 'Mustard', 'Sweet Herba Mystica'],
    ['Fried Fillet', 'Potato Salad', 'Mayonnaise', 'Ketchup'],
    ['Fried Fillet', 'Potato Salad', 'Lettuce', 'Mayonnaise', 'Ketchup'],
    ['Fried Fillet', 'Potato Salad', 'Lettuce', 'Mayonnaise', 'Ketchup', 'Horseradish'],
    ['Fried Fillet', 'Potato Salad', 'Lettuce', 'Mayonnaise', 'Ketchup', 'Horseradish', 'Spicy Herba Mystica'],
    ['Pickle', 'Ham', 'Mayonnaise', 'Mustard'],
    ['Pickle', 'Ham', 'Prosciutto', 'Mayonnaise', 'Mustard'],
    ['Pickle', 'Ham', 'Prosciutto', 'Jalapeno', 'Mayonnaise', 'Mustard'],
    ['Pickle', 'Ham', 'Prosciutto', 'Jalapeno', 'Mayonnaise', 'Mustard', 'Salty Herba Mystica'],
    ['Cheese', 'Cream Cheese', 'Pepper', 'Salt'],
    ['Cheese', 'Avocado', 'Cream Cheese', 'Pepper', 'Salt'],
    ['Cheese', 'Avocado', 'Basil', 'Cream Cheese', 'Pepper', 'Salt'],
    ['Cheese', 'Avocado', 'Basil', 'Cream Cheese', 'Pepper', 'Salt', 'Salty Herba Mystica'],
    ['Hamburger', 'Onion', 'Vinegar', 'Pepper'],
    ['Hamburger', 'Onion', 'Vinegar', 'Pepper', 'Horseradish'],
    ['Hamburger', 'Onion', 'Watercress', 'Vinegar', 'Pepper', 'Horseradish'],
    ['Hamburger', 'Onion', 'Watercress', 'Vinegar', 'Pepper', 'Horseradish', 'Sweet Herba Mystica'],
    ['Smoked Fillet', 'Watercress', 'Vinegar', 'Pepper', 'Salt'],
    ['Smoked Fillet', 'Watercress', 'Red Onion', 'Vinegar', 'Pepper', 'Salt'],
    ['Smoked Fillet', 'Watercress', 'Red Onion', 'Basil', 'Vinegar', 'Pepper', 'Salt'],
    ['Smoked Fillet', 'Watercress', 'Red Onion', 'Basil', 'Vinegar', 'Pepper', 'Salt', 'Salty Herba Mystica'],
    ['Banana', 'Apple', 'Pineapple', 'Kiwi', 'Whipped Cream'],
    ['Banana', 'Apple', 'Pineapple', 'Kiwi', 'Whipped Cream', 'Marmalade'],
    ['Banana', 'Apple', 'Pineapple', 'Kiwi', 'Whipped Cream', 'Marmalade', 'Yogurt'],
    ['Banana', 'Apple', 'Pineapple', 'Kiwi', 'Whipped Cream', 'Marmalade', 'Yogurt', 'Sweet Herba Mystica'],
    ['Prosciutto', 'Cherry Tomatoes', 'Smoked Fillet', 'Salt', 'Vinegar'],
    ['Prosciutto', 'Cherry Tomatoes', 'Smoked Fillet', 'Potato Salad', 'Salt', 'Vinegar'],
    ['Prosciutto', 'Cherry Tomatoes', 'Smoked Fillet', 'Potato Salad', 'Hamburger', 'Salt', 'Vinegar'],
    ['Prosciutto', 'Cherry Tomatoes', 'Smoked Fillet', 'Potato Salad', 'Hamburger', 'Salt', 'Vinegar', 'Bitter Herba Mystica'],
    ['Klawf Stick', 'Tomato', 'Lettuce', 'Salt', 'Olive Oil'],
    ['Klawf Stick', 'Tomato', 'Lettuce', 'Salt', 'Olive Oil', 'Wasabi'],
    ['Klawf Stick', 'Tomato', 'Lettuce', 'Yellow Bell Pepper', 'Salt', 'Olive Oil', 'Wasabi'],
    ['Klawf Stick', 'Tomato', 'Lettuce', 'Yellow Bell Pepper', 'Salt', 'Olive Oil', 'Wasabi', 'Spicy Herba Mystica'],
    ['Banana', 'Apple', 'Cheese', 'Whipped Cream', 'Butter'],
    ['Banana', 'Apple', 'Cheese', 'Whipped Cream', 'Butter', 'Salt'],
    ['Banana', 'Apple', 'Cheese', 'Basil', 'Whipped Cream', 'Butter', 'Salt'],
    ['Banana', 'Apple', 'Cheese', 'Basil', 'Whipped Cream', 'Butter', 'Salt', 'Sour Herba Mystica'],
    ['Green Bell Pepper', 'Cherry Tomatoes', 'Cucumber', 'Salt', 'Olive Oil', 'Vinegar'],
    ['Green Bell Pepper', 'Cherry Tomatoes', 'Cucumber', 'Red Onion', 'Salt', 'Olive Oil', 'Vinegar'],
    ['Green Bell Pepper', 'Cherry Tomatoes', 'Cucumber', 'Red Onion', 'Watercress', 'Salt', 'Olive Oil', 'Vinegar'],
    ['Green Bell Pepper', 'Cherry Tomatoes', 'Cucumber', 'Red Onion', 'Watercress', 'Salt', 'Olive Oil', 'Vinegar', 'Salty Herba Mystica'],
    ['Potato Tortilla', 'Fried Fillet', 'Prosciutto', 'Potato Salad', 'Peanut Butter', 'Salt'],
    ['Potato Tortilla', 'Fried Fillet', 'Prosciutto', 'Potato Salad', 'Herbed Sausage', 'Peanut Butter', 'Salt'],
    ['Potato Tortilla', 'Fried Fillet', 'Prosciutto', 'Potato Salad', 'Herbed Sausage', 'Hamburger', 'Peanut Butter', 'Salt'],
    ['Potato Tortilla', 'Fried Fillet', 'Prosciutto', 'Potato Salad', 'Herbed Sausage', 'Hamburger', 'Peanut Butter', 'Salt', 'Sour Herba Mystica'],
    ['Chorizo', 'Onion', 'Green Bell Pepper', 'Mustard', 'Chili Sauce', 'Pepper'],
    ['Chorizo', 'Onion', 'Green Bell Pepper', 'Basil', 'Mustard', 'Chili Sauce', 'Pepper'],
    ['Chorizo', 'Onion', 'Green Bell Pepper', 'Jalapeno', 'Basil', 'Mustard', 'Chili Sauce', 'Pepper'],
    ['Chorizo', 'Onion', 'Green Bell Pepper', 'Jalapeno', 'Basil', 'Mustard', 'Chili Sauce', 'Pepper', 'Spicy Herba Mystica'],
    ['Watercress', 'Onion', 'Yellow Bell Pepper', 'Tomato', 'Olive Oil', 'Wasabi'],
    ['Watercress', 'Onion', 'Yellow Bell Pepper', 'Tomato', 'Cucumber', 'Olive Oil', 'Wasabi'],
    ['Watercress', 'Onion', 'Yellow Bell Pepper', 'Tomato', 'Cucumber', 'Olive Oil', 'Wasabi', 'Mayonnaise'],
    ['Watercress', 'Onion', 'Yellow Bell Pepper', 'Tomato', 'Cucumber', 'Olive Oil', 'Wasabi', 'Mayonnaise', 'Sweet Herba Mystica'],
    ['Hamburger', 'Tomato', 'Kiwi', 'Pineapple', 'Butter', 'Horseradish'],
    ['Hamburger', 'Tomato', 'Kiwi', 'Pineapple', 'Avocado', 'Butter', 'Horseradish'],
    ['Hamburger', 'Tomato', 'Kiwi', 'Pineapple', 'Avocado', 'Cheese', 'Butter', 'Horseradish'],
    ['Hamburger', 'Tomato', 'Kiwi', 'Pineapple', 'Avocado', 'Cheese', 'Butter', 'Horseradish', 'Bitter Herba Mystica'],
    ['Smoked Fillet', 'Klawf Stick', 'Watercress', 'Basil', 'Vinegar', 'Olive Oil', 'Salt'],
    ['Smoked Fillet', 'Klawf Stick', 'Watercress', 'Basil', 'Tofu', 'Vinegar', 'Olive Oil', 'Salt'],
    ['Smoked Fillet', 'Klawf Stick', 'Watercress', 'Basil', 'Tofu', 'Red Onion', 'Vinegar', 'Olive Oil', 'Salt'],
    ['Smoked Fillet', 'Klawf Stick', 'Watercress', 'Basil', 'Tofu', 'Red Onion', 'Vinegar', 'Olive Oil', 'Salt', 'Spicy Herba Mystica'],
    ['Tofu', 'Tofu', 'Rice', 'Lettuce', 'Avocado', 'Wasabi', 'Salt'],
    ['Tofu', 'Tofu', 'Rice', 'Lettuce', 'Avocado', 'Wasabi', 'Salt', 'Horseradish'],
    ['Tofu', 'Tofu', 'Rice', 'Lettuce', 'Avocado', 'Watercress', 'Wasabi', 'Salt', 'Horseradish'],
    ['Tofu', 'Tofu', 'Rice', 'Lettuce', 'Avocado', 'Watercress', 'Wasabi', 'Salt', 'Horseradish', 'Salty Herba Mystica'],
    ['Noodles', 'Red Bell Pepper', 'Bacon', 'Yellow Bell Pepper', 'Olive Oil', 'Curry Powder', 'Salt'],
    ['Noodles', 'Red Bell Pepper', 'Bacon', 'Yellow Bell Pepper', 'Jalapeno', 'Olive Oil', 'Curry Powder', 'Salt'],
    ['Noodles', 'Red Bell Pepper', 'Bacon', 'Yellow Bell Pepper', 'Jalapeno', 'Egg', 'Olive Oil', 'Curry Powder', 'Salt'],
    ['Noodles', 'Red Bell Pepper', 'Bacon', 'Yellow Bell Pepper', 'Jalapeno', 'Egg', 'Olive Oil', 'Curry Powder', 'Salt', 'Sweet Herba Mystica'],
    ['Hamburger', 'Noodles', 'Potato Salad', 'Rice', 'Olive Oil', 'Curry Powder', 'Salt'],
    ['Hamburger', 'Noodles', 'Potato Salad', 'Rice', 'Klawf Stick', 'Olive Oil', 'Curry Powder', 'Salt'],
    ['Hamburger', 'Noodles', 'Potato Salad', 'Rice', 'Klawf Stick', 'Tofu', 'Olive Oil', 'Curry Powder', 'Salt'],
    ['Hamburger', 'Noodles', 'Potato Salad', 'Rice', 'Klawf Stick', 'Tofu', 'Olive Oil', 'Curry Powder', 'Salt', 'Bitter Herba Mystica'],
    ['Rice', 'Smoked Fillet', 'Smoked Fillet', 'Klawf Stick', 'Vinegar', 'Wasabi', 'Salt'],
    ['Rice', 'Smoked Fillet', 'Smoked Fillet', 'Klawf Stick', 'Watercress', 'Vinegar', 'Wasabi', 'Salt'],
    ['Rice', 'Smoked Fillet', 'Smoked Fillet', 'Klawf Stick', 'Klawf Stick', 'Watercress', 'Vinegar', 'Wasabi', 'Salt'],
    ['Rice', 'Smoked Fillet', 'Smoked Fillet', 'Klawf Stick', 'Klawf Stick', 'Watercress', 'Vinegar', 'Wasabi', 'Salt', 'Sour Herba Mystica']
    ]

list_of_powers_found = [] #Might end up with combinations covered in the game.
                          #I don't give a fuck tho
list_of_found_recipes = []
for combo in in_game_sandwhiche_ingredient_combinations:
    recipe = combo
    recipe.sort()
    list_of_found_recipes.append(recipe)
def update_recipe_dex(dictionary):
    info = '\n' + str(dictionary)
    info = info.replace("' ', ' '", '')
    info = info.replace(",''", '')
    info = info.replace("'',", '')
    info = info.replace("''", '')
    info = info.replace(", ' '", '')
    info = info.replace("'", '')
    info = info.replace(", ]", ']')
    #, ' '
    filename = 'Recipe_List-Reduced_Set.txt'
    if exists(filename):
        pass
    else:
        txt_file = open(filename, 'w')
        txt_file.write("The Recipe Dex - {Meal Powers: [[Power, Level, Type], [Power, Level, Type], [Power, Level, Type]], Recipe: [Seasonings, Ingredients]}:")
        txt_file.close()
    txt_file = open(filename, 'a')
    txt_file.write(info)
    txt_file.close()

def valid_sandwich(test_recipe):
    #Yeah Im not a sandwhich making scrub
    #No 1/2 star sandwiches for me
    #Yeah I could account for them but do we even really want them
    #Each sandwich needs an ingredient and a seasoning
    ingredient_check = False
    seasoning_check = False
    number_of_herba = 0
    number_of_non_herba = 0
    while (not (ingredient_check and seasoning_check)):
        for some_shit in test_recipe:
            if some_shit.get('seasoning', '') == '':
                pass
            elif some_shit.get('seasoning', 'null') == 'null':
                pass
            else:
                #print('s check pass')
                if str(some_shit.get('seasoning')).__contains__('herba'):
                    number_of_herba = number_of_herba + 1
                    if number_of_herba > 2: #theres no real reason to waste 3 herba mystica on a sandwhich
                        return False
                else:
                    number_of_non_herba = number_of_non_herba + 1
                #I aint really verify this but I dont think any given powers really require two herba and a third condiment
                if number_of_non_herba + number_of_herba > 2: 
                    return False
                seasoning_check = True
            if some_shit.get('ingredient', 'null') == 'null':
                pass
            elif some_shit.get('ingredient', '') == '':
                pass
            else:
                #print('i check pass')
                ingredient_check = True
                #Max pieces of ingredient on sandwhich seems to be 12
                number_of_this_ingredient = test_recipe.count(some_shit) * some_shit.get('pieces')
                if number_of_this_ingredient > 12:
                    print('This sandwich has too much ' + str(some_shit.get('ingredient')) + '!  It has ' + str(number_of_this_ingredient) + ' pieces.')
                    return False
    
    return ingredient_check and seasoning_check
        
    

#pokemon checker
def Pokemon():
    #inputs
    power_one = ''
    level_one = ''
    type_one = ''
    power_two = ''
    level_two = ''
    type_two = ''
    power_three = ''
    level_three = ''
    type_three = ''
    try:
        file, power_one, level_one, type_one, power_two, level_two, type_two, power_three, level_three, type_three = argv
        #9+1
    except:
        try:
            file, power_one, level_one, type_one, power_two, level_two, type_two = argv
            #6+1
        except:
            try:
                file, power_one, level_one, type_one = argv
                #3+1
            except:
                #Egg does not get a type
                try:
                    #Egg specified first
                    file, power_one, level_one, power_two, level_two, type_two, power_three, level_three, type_three = argv
                    #8+1
                except:
                    try:
                        #Egg specified first
                        file, power_one, level_one, power_two, level_two, type_two = argv
                        #5+1
                    except:
                        try:
                            #Egg specified first
                            file, power_one, level_one = argv
                            if power_one == 'egg':
                                pass
                            else:
                                #print('That is not supported.  Please refresh yourself by reading the instructions.')
                                exit(0)
                            #2+1
                        except:
                            print('Thats not supported.  Please refresh yourself by reading the instructions.')
##                            ###testing###
##                            [power_one, level_one, type_one] = ['egg', 2, 'fire']
##                            [power_two, level_two, type_two] = ['encounter', 2, 'poison']
##                            [power_three, level_three, type_three] = ['exp', 2, 'electric']
                            exit(0)
    #title, 2, fairy
    file = 'Recipe_List-Reduced_Set-3S2I.txt'
    file_object = open(file, 'r')
    recipes = file_object.readlines()
    file_object.close()
    #print(str(recipes[14623]))
    level_one = str(level_one)
    level_two = str(level_two)
    level_three = str(level_three)
    if power_one == 'egg':
        p_one = power_one + ', ' + level_one
    else:
        p_one = power_one + ', ' + level_one + ', ' + type_one
    p_two = power_two + ', ' + level_two + ', ' + type_two
    if p_two == ', , ':
        p_two = ''
    p_three = power_three + ', ' + level_three + ', ' + type_three
    if p_three == ', , ':
        p_three = '' 
    if power_one == 'egg':
        ponon = power_one
        pontw = power_one
        ponth = power_one
    else:
        ponon = power_one + ', ' + '1' + ', ' + type_one
        pontw = power_one + ', ' + '2' + ', ' + type_one
        ponth = power_one + ', ' + '3' + ', ' + type_one
    ptwon = power_two + ', ' + '1' + ', ' + type_two
    ptwtw = power_two + ', ' + '2' + ', ' + type_two
    ptwth = power_two + ', ' + '3' + ', ' + type_two
    pthon = power_three + ', ' + '1' + ', ' + type_three
    pthtw = power_three + ', ' + '2' + ', ' + type_three
    pthth = power_three + ', ' + '3' + ', ' + type_three
    
    found_line = False
    for line in recipes:
        if str(line).__contains__(p_one):
            if str(line).__contains__(p_two):
                if str(line).__contains__(p_three):
                    print(line)
                    found_line = True
    if True:
        file = 'Recipe_List-Not_Full.txt'
        file_object = open(file, 'r')
        recipess = file_object.readlines()
        file_object.close()
        for line in recipess:
            if str(line).__contains__(p_one):
                if str(line).__contains__(p_two):
                    if str(line).__contains__(p_three):
                        print(line)
                        found_line = True
    if not found_line: #ok you aint getting exactly what you want but heres at least the same powers
        for line in recipes:
            if str(line).__contains__(ponon) or str(line).__contains__(pontw) or str(line).__contains__(ponth):
                if str(line).__contains__(ptwon) or str(line).__contains__(ptwtw) or str(line).__contains__(ptwth):
                    if str(line).__contains__(pthon) or str(line).__contains__(pthth) or str(line).__contains__(pthtw):
                        print(line)
        for line in recipess:
            if str(line).__contains__(ponon) or str(line).__contains__(pontw) or str(line).__contains__(ponth):
                if str(line).__contains__(ptwon) or str(line).__contains__(ptwtw) or str(line).__contains__(ptwth):
                    if str(line).__contains__(pthon) or str(line).__contains__(pthth) or str(line).__contains__(pthtw):
                        print(line)
    
    if not found_line:
        print('That power combo has not been logged in the recipe list.  Please remember tho that these are original recipes')
        print('Consult the ingame recipies list for it might have what you are looking for.')
    exit(0)
                
        
######    #######
    return 11037


        
if __name__ == '__main__':
    Pokemon()








