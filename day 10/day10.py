# https://adventofcode.com/2020/day/10
file = open("day10_data", "r")
data = file.read().splitlines()
jolts_list = [0]  # first input as per problem request
for x in data:
    jolts_list.append(int(x))

# sorting the list makes the iteration through it easier
jolts_list.sort()
# this is because we have to count the last jolt which is always + 3 from the last element of the list
jolts_list.append(jolts_list[-1] + 3)


def process_list(num_list):
    one_differences = 0
    three_differences = 0
    for index, val in enumerate(num_list):
        try:
            # we iterate through the list calculating the differences of 1 jolt and 3 jolts present scrolling through
            # the (ordered) list
            if val + 1 == num_list[index + 1]:
                one_differences += 1
            elif val + 2 == num_list[index + 1]:
                continue
            elif val + 3 == num_list[index + 1]:
                three_differences += 1
        except IndexError:
            # the IndexError exception tells us we have finished the list and index + 1 cannot be accessed
            break
    return one_differences, three_differences


differences = process_list(jolts_list)
print(differences)
print(differences[0] * differences[1])

# part 2
scores = {}
# going from the bottom to the top, reversing the list
jolts_list.reverse()
for key, number in enumerate(jolts_list):
    # gets the next 3 numbers for every key (the list was reversed)
    next_numbers = jolts_list[:key][-3:]

    # end of list
    if not next_numbers:
        scores[number] = 1
        continue

    scores[number] = 0
    for next_number in next_numbers:
        # assigns True if their difference is maximum 3
        is_valid = next_number - number <= 3
        # counts how many valid paths there can be for every element of the list and adds them together
        if is_valid:
            scores[number] += scores[next_number]


print(scores[0])
file.close()
