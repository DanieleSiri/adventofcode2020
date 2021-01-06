# https://adventofcode.com/2020/day/25
file = open("day25_data", 'r')
card, door = file.read().splitlines()
card = int(card)
door = int(door)


def find_loop_size(num_to_find):
    value = 1
    loop_size = 0
    # bruteforcing but avoiding calculating all the values of previous loops, just need the most recent one
    while True:
        if value == num_to_find:
            return loop_size
        loop_size += 1
        value *= 7
        value %= 20201227


def find_key(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value %= 20201227
    return value


card_loop = find_loop_size(card)
door_loop = find_loop_size(door)
print(find_key(card, door_loop))
print(find_key(door, card_loop))
file.close()
