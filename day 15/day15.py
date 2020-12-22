# https://adventofcode.com/2020/day/15
file = open('day15_data', 'r')
data = file.read().splitlines()
game = {}
starting_numbers = []
for x in data:
    starting_numbers = x.split(",")
for i, v in enumerate(starting_numbers):
    # i + 1 to synchronize it with the turns
    game[i + 1] = int(v)


def get_turn(n):
    # get the key for the corresponding value
    for y, z in game.items():
        if z == n:
            return y


# initializing the turn number depending on how many starting numbers there are
turn = len(starting_numbers)
while 2020 not in game.keys():
    # first time the number has been spoken
    if game[turn] not in list(game.values())[:-1]:
        game[turn + 1] = 0
    else:
        previous_turn = get_turn(game[turn])
        game[turn + 1] = turn - previous_turn
        # delete oldest value
        game.pop(previous_turn)
    turn += 1

print(game[2020])
file.close()
