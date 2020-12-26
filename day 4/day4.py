# https://adventofcode.com/2020/day/4


import re


allowed_fields_list = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
ecl_list = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def check(passport):
    # part 1
    for l in allowed_fields_list:
        if l not in passport.keys():
            return False
    # part 2
    if not re.match('\d{4}', passport['byr']):
        return False
    if int(passport['byr']) > 2002 or int(passport['byr']) < 1920:
        return False
    if not re.match('\d{4}', passport['iyr']):
        return False
    if int(passport['iyr']) > 2020 or int(passport['iyr']) < 2010:
        return False
    if not re.match('\d{4}', passport['eyr']):
        return False
    if int(passport['eyr']) > 2030 or int(passport['eyr']) < 2020:
        return False
    if not re.match('#{1}([0-9]|[a-f]){6}', passport['hcl']):
        return False
    if passport['ecl'] not in ecl_list:
        return False
    if not re.match('\d{9}$', passport['pid']):
        return False
    if re.match('(\d{3}cm)|(\d{2}in)', passport['hgt']):
        if 'cm' in passport['hgt']:
            if int(passport['hgt'][0:3]) > 193 or int(passport['hgt'][0:3]) < 150:
                return False
        else:
            if int(passport['hgt'][0:2]) > 76 or int(passport['hgt'][0:2]) < 59:
                return False
    elif not re.match('(\d{3}cm)|(\d{2}in)', passport['hgt']):
        return False
    return True


file = open("day4_data", "r")
data = file.read().split("\n\n")
passport_list = [element.replace("\n", " ") for element in data]
valid_count = 0
passport_fields_list = []
for element in passport_list:
    fields = {x.split(":")[0]: x.split(":")[1] for x in element.split(" ")}
    passport_fields_list.append(fields)

for element in passport_fields_list:
    if check(element):
        valid_count += 1

print(valid_count)
file.close()
