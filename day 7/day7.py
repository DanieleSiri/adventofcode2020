# https://adventofcode.com/2020/day/7
import re


file = open("day7_data", "r")
data = file.read().splitlines()
graph = {}
for line in data:
    if re.search('contain\sno\sother\sbags', line):
        continue
    # building the graph backwards, with the keys being the bags contained by their values
    # this simplifies the research of the bags that need to contain our target
    contained = re.findall('^\w*\s\w*', line)[0]
    to_parse = re.findall('\d\s\w*\s\w*', line)
    for el in to_parse:
        key = el[2:]
        if key not in graph.keys():
            graph[key] = [contained]
        else:
            graph[key].append(contained)


def find_contained(bag, found):
    """
    searches through the graph adding the values found in a set
    """
    for x in graph[bag]:
        found.add(x)
        if x in graph:
            find_contained(x, found)
    return found


values = find_contained('shiny gold', set())
print(len(values))


# part 2
# rebuilding the graph topdown this time, because we need to search from shiny gold to bottom
graph = {}
for line in data:
    if re.search('contain\sno\sother\sbags', line):
        continue
    key = re.findall('^\w*\s\w*', line)[0]
    parsed = re.findall('\d\s\w*\s\w*', line)
    nodes = []
    for element in parsed:
        nodes.append(element)
    graph[key] = nodes
results = []


def hasNumbers(string):
    """
    checks if string has a number in it
    """
    return any(char.isdigit() for char in string)


# performing a DFS search
def DFSutil(g, n, c, visited):
    if hasNumbers(n):
        # parsing the values, splitting the bag count and the name of the bag
        c *= int(n[0])
        n = n[2:]
    visited.add(n)
    results.append((c, n))
    try:
        for neighbour in g[n]:
            if neighbour not in visited:
                DFSutil(g, neighbour, c, visited)
    except KeyError:
        pass


def DFS(g, n):
    visited = set()
    DFSutil(g, n, 1, visited)


DFS(graph, 'shiny gold')
final = 0
results.pop(0)
for bag in results:
    final += bag[0]
print(final)

file.close()
