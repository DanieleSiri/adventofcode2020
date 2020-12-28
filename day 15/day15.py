# https://adventofcode.com/2020/day/15
from array import array


file = open('day15_data', 'r')
data = file.read().splitlines()
for x in data:
    starting_numbers = array('b', (int(y) for y in x.split(",")))
# dict entries = {number: (turn, turn difference between current turn and previous turn when the number occurred)}
start_game = {v: (i + 1, 0) for i, v in enumerate(starting_numbers[:-1])}
# initializing the turn number depending on how many starting numbers there are
start_turn = len(starting_numbers)
next_value_start = starting_numbers[-1]


def solve(stop, turn, next_value, game):
    print(game)
    while True:
        if turn == stop:
            return next_value
        # number already spoken
        if next_value in game:
            # assigning the turn difference to the next value
            next_value = game[next_value][1]
            # if the value does not exist in game, it would raise a KeyError exception
            try:
                game[next_value] = (turn + 1, (turn + 1) - game[next_value][0])
            except KeyError:
                game[next_value] = (turn + 1, 0)
        # first time the number has been spoken
        else:
            # first iteration
            if turn == len(starting_numbers):
                game[next_value] = (turn, 0)
            next_value = 0
            # updating the entry for 0
            game[0] = (turn + 1, (turn + 1) - game[0][0])
        turn += 1


print(solve(2020, start_turn, next_value_start, start_game.copy()))  # part 1
print(solve(30000000, start_turn, next_value_start, start_game.copy()))  # part 2

file.close()
