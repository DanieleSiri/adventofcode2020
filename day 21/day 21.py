# https://adventofcode.com/2020/day/21
file = open("day21_data", 'r')
all_food = []
allergents = {}


def check_food(food_set1, food_set2):
    # returns the intersection of the 2 sets, meaning the food that contains that allergent we are iterating
    food_in_both = food_set1 & food_set2
    return food_in_both


for line in file.read().splitlines():
    elements = line.split(" (contains ")
    # create a set of food
    foods = {i for i in elements[0].split(" ")}
    for i in foods:
        all_food.append(i)
    if "," in elements[1][:-1]:
        for el in elements[1][:-1].split(", "):
            if el in allergents:
                bad_food = check_food(foods, allergents[el])
                # create an entry with the food set we checked in the function
                allergents[el] = bad_food
            else:
                # first time we parsed the allergent
                allergents[el] = foods
    else:
        if elements[1][:-1] in allergents:
            # same process of above
            bad_food = check_food(foods, allergents[elements[1][:-1]])
            allergents[elements[1][:-1]] = bad_food
        else:
            allergents[elements[1][:-1]] = foods

# set of bad food for faster research
bad_food_set = set()
for entry in allergents:
    for food_set in allergents[entry]:
        bad_food_set.add(food_set)

count = 0
# counting the valid food
for food in all_food:
    if food not in bad_food_set:
        count += 1
print(count)

file.close()
