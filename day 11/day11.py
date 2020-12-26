# https://adventofcode.com/2020/day/11
file = open("day11_data", "r")
data = file.read().splitlines()
seat_map = {(row, col): value for row, line in enumerate(data)
            for col, value in enumerate(line)}
col_length = len(data[0])
row_length = len(data)
seat_map_part_2 = seat_map


def rules(grid, seat, pos):
    surroundings = []
    val = seat
    # get the surrounding values
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            try:
                # gets the surrounding values
                surroundings.append(grid[(pos[0] + x, pos[1] + y)])
            # if the value is out of the range exits
            except KeyError:
                continue
    if seat == 'L':
        for el in surroundings:
            # if it finds an occupied seat it exits because the seat stays empty
            if el == '#':
                return val
        # if it gets to this point it means there were no occupied seats around it so we can change it
        val = '#'
        return val
    elif seat == '#':
        # if there's more than 4 occupied seats around it, changes the seat to empty
        if surroundings.count('#') >= 4:
            val = 'L'
            return val
    return val


while True:
    results = {}
    for index in seat_map:
        if seat_map[index] == '.':
            # doesn't do anything if the seat is a 'floor' seat
            results[index] = '.'
            continue
        results[index] = rules(seat_map, seat_map[index], index)
    # this means it repeated the pattern so it has to exit the loop
    if results == seat_map:
        break
    seat_map = results

occupied = 0
for a in range(row_length):
    for b in range(col_length):
        if seat_map[(a, b)] == '#':
            occupied += 1
print(occupied)


# part 2
def sight(grid, pos, coords):
    increment = 0
    while True:
        try:
            increment += 1
            # top-left diagonal
            if coords[0] == -1 and coords[1] == -1:
                if grid[(pos[0] - increment, pos[1] - increment)] != '.':
                    return grid[(pos[0] - increment, pos[1] - increment)]
            # left col
            elif coords[0] == 0 and coords[1] == -1:
                if grid[(pos[0], pos[1] - increment)] != '.':
                    return grid[(pos[0], pos[1] - increment)]
            # bottom-left diagonal
            elif coords[0] == 1 and coords[1] == -1:
                if grid[(pos[0] + increment, pos[1] - increment)] != '.':
                    return grid[(pos[0] + increment, pos[1] - increment)]
            # top
            elif coords[0] == -1 and coords[1] == 0:
                if grid[(pos[0] - increment, pos[1])] != '.':
                    return grid[(pos[0] - increment, pos[1])]
            # bottom
            elif coords[0] == 1 and coords[1] == 0:
                if grid[(pos[0] + increment, pos[1])] != '.':
                    return grid[(pos[0] + increment, pos[1])]
            # top-right diagonal
            elif coords[0] == -1 and coords[1] == 1:
                if grid[(pos[0] - increment, pos[1] + increment)] != '.':
                    return grid[(pos[0] - increment, pos[1] + increment)]
            # right col
            elif coords[0] == 0 and coords[1] == 1:
                if grid[(pos[0], pos[1] + increment)] != '.':
                    return grid[(pos[0], pos[1] + increment)]
            # bottom-right diagonal
            elif coords[0] == 1 and coords[1] == 1:
                if grid[(pos[0] + increment, pos[1] + increment)] != '.':
                    return grid[(pos[0] + increment, pos[1] + increment)]
        # out of map
        except KeyError:
            return


def compute(grid, seat, pos):
    surroundings = []
    val = seat
    # get the surrounding values
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            try:
                if grid[(pos[0] + x, pos[1] + y)] == '.':
                    ret = sight(grid, pos, (x, y))
                    if not ret:
                        continue
                    else:
                        surroundings.append(ret)
                # gets the surrounding values
                else:
                    surroundings.append(grid[(pos[0] + x, pos[1] + y)])
            # if the value is out of the range exits
            except KeyError:
                continue
    if seat == 'L':
        for el in surroundings:
            # if it finds an occupied seat it exits because the seat stays empty
            if el == '#':
                return val
        # if it gets to this point it means there were no occupied seats around it so we can change it
        val = '#'
        return val
    elif seat == '#':
        # if there's more than 4 occupied seats around it, changes the seat to empty
        if surroundings.count('#') >= 5:
            val = 'L'
            return val
    return val


while True:
    results = {}
    for index in seat_map_part_2:
        if seat_map_part_2[index] == '.':
            # doesn't do anything if the seat is a 'floor' seat
            results[index] = '.'
            continue
        results[index] = compute(seat_map_part_2, seat_map_part_2[index], index)
    # this means it repeated the pattern so it has to exit the loop
    if results == seat_map_part_2:
        break
    seat_map_part_2 = results

occupied_2 = 0
for a in range(row_length):
    for b in range(col_length):
        if seat_map_part_2[(a, b)] == '#':
            occupied_2 += 1
print(occupied_2)

file.close()
