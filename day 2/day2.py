# https://adventofcode.com/2020/day/2

pw_list = open("day2_data", "r")
# part 1 and part 2 together
pw_counter = 0
pw_counter_2 = 0

for line in pw_list.read().splitlines():
    # parsing the file
    x = line.split(" ")
    min = x[0].split("-")[0]
    max = x[0].split("-")[1]
    letter = x[1].split(":")[0]
    pw = x[2]
    # part 1: if letter is present in the password minimum "min" times and maximum "max" times
    if int(min) <= pw.count(letter) <= int(max):
        pw_counter += 1

    # part 2: letter has to be at index "min" or at index "max" and not both
    indices = [i+1 for i, val in enumerate(pw) if val == letter]  # creates a list of indexes where the letter appears
    if (int(min) in indices and int(max) not in indices) or (int(max) in indices and int(min) not in indices):
        pw_counter_2 += 1

print(pw_counter)
print(pw_counter_2)
pw_list.close()
