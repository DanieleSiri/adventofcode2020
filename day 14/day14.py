# https://adventofcode.com/2020/day/14
import re
import numpy as np


file = open("day14_data", 'r')
data = file.read().splitlines()
data_number = []
memory = {}
mask = ''
for line in data:
    split_input = line.split(" = ")
    if split_input[0] == 'mask':
        mask = split_input[1]
        continue
    else:
        address = int(re.findall('(?<=\[)\d*', split_input[0])[0])
        data_number = list(np.binary_repr(int(split_input[1]), width=36))
    if address not in memory.keys():
        # creating an empty list at the address (converted in binary)
        memory[bin(address)] = []
    for i, v in enumerate(mask):
        if v == 'X':
            # if the bit is X, take the bit from the number in data
            memory[bin(address)].append(data_number[i])
        else:
            # else take the bit from the mask
            memory[bin(address)].append(v)

sum = 0
for n, m in enumerate(memory):
    # converting it to string so we can convert from binary to int
    memory[m] = ''.join(memory[m])
    sum += int(memory[m], 2)
print(sum)
file.close()
