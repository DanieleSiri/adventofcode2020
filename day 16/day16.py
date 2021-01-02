# https://adventofcode.com/2020/day/16
file = open("day16_data", 'r')
data = file.read().split("\n\n")

# parsing allowed values
allowed_values = set()
# for part 2
fields = {}
for x in data[0].split("\n"):
    num_range = x.split(": ")[1]
    key = x.split(": ")[0]
    values = set()
    min_max = (int(num_range.split(" or ")[0].split("-")[0]), int(num_range.split(" or ")[0].split("-")[1]))
    for num in range(min_max[0], min_max[1] + 1):
        allowed_values.add(num)
        values.add(num)
    min_max = (int(num_range.split(" or ")[1].split("-")[0]), int(num_range.split(" or ")[1].split("-")[1]))
    for num in range(min_max[0], min_max[1] + 1):
        allowed_values.add(num)
        values.add(num)
    fields[key] = values

# parsing tickets
ticket_list = []
for x in data[2].split("\n"):
    if x == 'nearby tickets:':
        continue
    ticket_values = [int(i) for i in x.split(",")]
    ticket_list.append(ticket_values)

invalid_values = []
# for part 2, making a deep copy of the list so we can remove its elements without removing them from the ticket_list
valid_ticket_list = ticket_list.copy()
for ticket in ticket_list:
    # if the ticket values are included in allowed values set the ticket is valid
    if set(ticket) < allowed_values:
        continue
    else:
        # adding the values in ticket that are not included in allowed values to a list
        for j in set(ticket) - allowed_values:
            invalid_values.append(j)
        # for part 2, getting all the valid tickets
        valid_ticket_list.remove(ticket)

print(sum(invalid_values))
# part 2
columns_dict = {}
# initialize empty sets for each dictionary key (our column numbers)
for e in range(len(ticket_list[0])):
    columns_dict[e] = set()
# creating a dictionary with column number: set of values of each column for valid tickets
for ticket in valid_ticket_list:
    for index, val in enumerate(ticket):
        columns_dict[index].add(val)

# parsing ticket
my_ticket = []
for i in data[1].split("\n"):
    if i == "your ticket:":
        continue
    for j in i.split(","):
        my_ticket.append(int(j))

# creating a dictionary of valid fields for each column
possible_fields = {}
for i in range(len(columns_dict.keys())):
    possible_fields[i] = set()
for field in fields:
    for column in columns_dict:
        if len(columns_dict[column] - fields[field]) == 0:
            possible_fields[column].add(field)

results = {}
while len(set(results.keys())) != len(set(columns_dict.keys())):
    # scanning the valid fields
    for field in possible_fields:
        # getting the column which has only 1 valid field
        if len(possible_fields[field]) == 1:
            results[field] = list(possible_fields[field])[0]
            for element in possible_fields:
                # removing from the possible fields the value that we found before which can only be applied to 1 col
                if element == field:
                    continue
                if list(possible_fields[field])[0] in possible_fields[element]:
                    possible_fields[element].remove(list(possible_fields[field])[0])

result = 1
for s in results:
    if "departure" in results[s]:
        result *= my_ticket[s]

print(result)
file.close()
