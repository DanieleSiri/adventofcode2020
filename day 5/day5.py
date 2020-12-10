# https://adventofcode.com/2020/day/5

file = open("day5_data", "r")
ticket_list = file.read().splitlines()


def parse(ticket, row_min, row_max, col_min, col_max):
    row = None
    column = None
    for letter in ticket[0:8]:  # parse the first 7 characters
        if letter == "F":
            row_max = row_min + ((row_max - row_min) // 2)
        elif letter == "B":
            row_min += (row_max - row_min) // 2 + ((row_max - row_min) % 2 > 0)  # round UP
        if row_max == row_min:  # means we have our row
            row = row_max
    for letter in ticket[7:]:
        if letter == "L":
            col_max = col_min + ((col_max - col_min) // 2)
        elif letter == "R":
            col_min += (col_max - col_min) // 2 + ((col_max - col_min) % 2 > 0)  # round UP
        if col_max == col_min:  # means we have our column
            column = col_max
    return row, column


# part 1 and 2 meshed
highest_seat = 0
seats = set()
for element in ticket_list:
    row_start = 0
    row_finish = 127
    column_start = 0
    column_finish = 7
    position = parse(element, row_start, row_finish, column_start, column_finish)
    # create a set with all the seats ID
    seats.add(position[0] * 8 + position[1])
    if (position[0] * 8 + position[1]) > highest_seat:
        highest_seat = position[0] * 8 + position[1]

# part 2: need to find the missing seat ID knowing that the +1 element and the -1 element are present in the set
for element in seats:
    if (element + 1 not in seats) and (element + 2 in seats):
        print(element + 1)
        break

print(highest_seat)
file.close()
