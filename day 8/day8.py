file = open("day8_data", "r")
data = file.read().splitlines()
operations = []
for el in data:
    tmp = el.split(" ")
    var = (tmp[0], int(tmp[1]))
    operations.append(var)


def execute(ops_list, completed_ops_list, index, register_value):
    completed_ops_list.add(index)
    if ops_list[index][0] == 'nop':
        index += 1
    elif ops_list[index][0] == 'acc':
        register_value += ops_list[index][1]
        index += 1
    elif ops_list[index][0] == 'jmp':
        # jumps to the index indicated in the jmp value
        index += ops_list[index][1]
    return index, register_value


def replace(op):
    if op == "nop":
        return "jmp"
    elif op == "jmp":
        return "nop"
    else:
        return "acc"


completed_ops = set()
current_index = 0
register = 0

while True:
    # checks if the index is already registered in the completed_ops_list (means we have done it already and don't
    # want to enter the infinite loop)
    if current_index in completed_ops:
        break
    result = execute(operations, completed_ops, current_index, register)
    current_index = result[0]
    register = result[1]

print("part 1 value before loop" + ' ' + str(register))

# part 2
exited = False
# iterate through the set of completed operations (because we know we are going to get through those)
for x in completed_ops:
    completed_ops_2 = set()
    # checks if the program arrived at the last entry of the list, which means it terminated
    if exited:
        break
    # skips replacement if 'acc'
    if operations[x][0] == 'acc':
        continue
    # resetting index and register
    current_index = 0
    register = 0
    # saving current value in order to replace only 1 value at a time
    save_value = operations[x]
    num_tmp = operations[x][1]
    # replacing nop with jmp and vice versa
    operations[x] = (replace(operations[x][0]), num_tmp)
    while True:
        # checks if index is out of scope (means the program terminated)
        if current_index >= len(operations):
            exited = True
            break
        if current_index in completed_ops_2:
            break
        result = execute(operations, completed_ops_2, current_index, register)
        current_index = result[0]
        register = result[1]
    # resets value in case the loop is still present in the program
    operations[x] = save_value

print("program exited with value" + ' ' + str(register))
file.close()
