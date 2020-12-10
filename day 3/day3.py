# https://adventofcode.com/2020/day/3


def movement(right, down, tree_map, depth, length):
    position = (0, 1)  # 1 because i started the line_count with 1 and not 0
    tree_count = 0
    y_position_count = 1  # starting line 1
    while y_position_count < depth:
        position = (((position[0] + right) % length), position[1] + down)
        # % length because the pattern repeats from left to right, so the module gives me the tree no matter how far
        # right
        if position in tree_map:
            tree_count += 1
        y_position_count += 1
    return tree_count


file = open("day3_data", "r")
data = file.read().splitlines()
trees = set()  # (x_coord, y_coord)
line_count = 0
line_length = 0
for line in data:
    line_length = len(line)
    line_count += 1
    # creates a set of trees coordinates
    for i, letter in enumerate(line):
        if letter == "#":
            trees.add((i, line_count))

# part 1
print(movement(3, 1, trees, line_count, line_length))
# part 2
print(movement(1, 1, trees, line_count, line_length) *
      movement(3, 1, trees, line_count, line_length) *
      movement(5, 1, trees, line_count, line_length) *
      movement(7, 1, trees, line_count, line_length) *
      movement(1, 2, trees, line_count, line_length))

file.close()
