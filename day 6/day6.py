# https://adventofcode.com/2020/day/6

file = open("day6_data", "r")
data = file.read().split("\n\n")
formatted_data = []
# removes newlines in the groups
for i in data:
    formatted_data.append(i.replace("\n", ""))

# part 1
yes = 0
for element in formatted_data:
    # creates a set with all the letters (sets only show unique values when you evaluate them)
    answers = set()
    for letter in element:
        answers.add(letter)
    # counts the number of answers
    for i, val in enumerate(answers):
        yes += 1
print(yes)

# part 2
yes_2 = 0
for i in data:
    data_sets_list = {}  # dictionary with key = group number, value = set of letters
    common = set()
    groups = i.split("\n")
    for l, element in enumerate(groups):
        answers_2 = set()
        # creating the set of letters
        for letter in element:
            answers_2.add(letter)
        # creating the dictionary entries
        data_sets_list[l] = answers_2
    for x in data_sets_list:
        if x == 0:  # initializing the common set with the first value in data_sets_list
            common = data_sets_list[x]
        else:  # finding the values present in all group sets
            common = (common & data_sets_list[x])
    # counting how many elements are in common between all group sets
    for m, element in enumerate(common):
        yes_2 += 1
print(yes_2)
file.close()
