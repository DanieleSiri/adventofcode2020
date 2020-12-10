# https://adventofcode.com/2020/day/1

num_list = open("day1_data", "r")
numbers = set()
for x in num_list.read().splitlines():
    numbers.add(x)

# part 1
# finds the 2 numbers that add up to 2020
for x in numbers:
    if str(2020 - int(x)) in numbers:
        print(int(x) * (2020 - int(x)))
        break

# part 2
# finds the 3 numbers that add up to 2020
result = 0
for x in numbers:
    sam = 2020 - int(x)
    for j in numbers:
        if str(sam - int(j)) in numbers:
            result = int(j) * int(x) * (sam - int(j))
            print(result)
            break
    if result != 0:
        break

num_list.close()
