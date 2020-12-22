# https://adventofcode.com/2020/day/16
file = open("day16_data", 'r')
data = file.read().split("\n\n")

# parsing allowed values
allowed_values = set()
# needed for part 2
fields = {}
for x in data[0].split("\n"):
    key = x.split(":")[0]
    values = set()
    try:
        for num in range(int(x.split(" ")[1].split("-")[0]), int(x.split(" ")[1].split("-")[1]) + 1):
            allowed_values.add(num)
            values.add(num)
    except ValueError:
        for num in range(int(x.split(" ")[2].split("-")[0]), int(x.split(" ")[2].split("-")[1]) + 1):
            allowed_values.add(num)
            values.add(num)
    try:
        for num in range(int(x.split(" ")[3].split("-")[0]), int(x.split(" ")[3].split("-")[1]) + 1):
            allowed_values.add(num)
            values.add(num)
    except ValueError:
        for num in range(int(x.split(" ")[4].split("-")[0]), int(x.split(" ")[4].split("-")[1]) + 1):
            allowed_values.add(num)
            values.add(num)
    # for part 2
    fields[key] = values

# parsing tickets
ticket_list = []
for x in data[2].split("\n"):
    if x == 'nearby tickets:':
        continue
    ticket_values = set()
    for i in x.split(","):
        ticket_values.add(int(i))
    ticket_list.append(ticket_values)

invalid_values = []
for ticket in ticket_list:
    # if the ticket values are included in allowed values set the ticket is valid
    if ticket < allowed_values:
        continue
    else:
        # adding the values in ticket that are not included in allowed values to a list
        for j in ticket - allowed_values:
            invalid_values.append(j)

print(sum(invalid_values))

# part 2
file.close()
