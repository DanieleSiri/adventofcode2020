# https://adventofcode.com/2020/day/9
file = open("day9_data", "r")
data = file.read().splitlines()

# preamble (as per problem request)
values = [int(x) for x in data[0:25]]


# create a set of valid values, meaning they are the possible values derived from the sum of any 2 numbers
def compute(num_list):
    # numbers can't be equal
    valid_values = {int(i) + int(j) for i in num_list
                    for j in num_list if i != j}
    return valid_values


# check if the next number on the list is present in the set (meaning it's the sum of any 2 values in the list)
def is_valid(valid_set, num_to_check):
    if num_to_check in valid_set:
        return True
    return False


# update the list by popping the oldest value and appending the new value
def update_list(num_list, num):
    num_list.pop(0)
    num_list.append(num)
    return num_list


wrong_value = 0
for el in data[25:]:
    # create the set of possible valid values
    valid = compute(values)
    # check if the value is valid
    if not is_valid(valid, int(el)):
        wrong_value = int(el)
        break
    # update the list with the latest value
    values = update_list(values, int(el))

print(wrong_value)


# part 2
def wrong_value_find(num_list, wrong):
    elements_set = set()
    elements_sum = 0
    for z in num_list:
        # creates a set of the possible correct values, so we can return it and scan it later for its values
        elements_set.add(z)
        elements_sum += z
        # if the sum exceeds our value to scan it means we can exit
        if elements_sum > wrong:
            return
        # if we find the correct value we can return the set of elements that sum up to that value
        if elements_sum == wrong:
            return elements_set


# create a full list
full_list = [int(x) for x in data if int(x) != wrong_value]

while True:
    found = wrong_value_find(full_list, wrong_value)
    if found is not None:
        break
    # removes each time the first element of the list because the values have to be contiguous so we can just move
    # forward for scanning
    full_list.pop(0)

print(min(found) + max(found))
file.close()
