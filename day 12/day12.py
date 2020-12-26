# https://adventofcode.com/2020/day/12
file = open("day12_data", "r")
data = file.read().splitlines()
directions = [(el[0], int(el[1:])) for el in data]

# initialize the ship coordinates
# east and north if negative mean that we are respectively west and south
ship_coords = {'face': 'east', 'east': 0, 'north': 0}
# create a circular graph for the polar coordinates. List in order for the clockwise circle, list in reverse for the
# counter-clockwise circle
coords_graph = {'east': ['south', 'west', 'north'],
                'south': ['west', 'north', 'east'],
                'west': ['north', 'east', 'south'],
                'north': ['east', 'south', 'west']}


def check_face(direction, index):
    new_direction = None
    if direction == 'R':
        # turns the ship by getting the index of the coordinates graph
        new_direction = coords_graph[ship_coords['face']][index - 1]
    elif direction == 'L':
        # if direction is counter clockwise, need to invert the list
        new_direction = coords_graph[ship_coords['face']][-index]
    return new_direction


def navigate(action, value):
    if action == 'N':
        ship_coords['north'] += value
    elif action == 'S':
        ship_coords['north'] -= value
    elif action == 'E':
        ship_coords['east'] += value
    elif action == 'W':
        ship_coords['east'] -= value
    elif action == 'L' or action == 'R':
        # calculates the degree of the turn
        remainder = value // 90
        ship_coords['face'] = check_face(action, remainder)
    elif action == 'F':
        # checking which direction the ship is facing and increasing/decreasing its coordinates accordingly
        if ship_coords['face'] == 'north':
            ship_coords['north'] += value
        elif ship_coords['face'] == 'south':
            ship_coords['north'] -= value
        elif ship_coords['face'] == 'east':
            ship_coords['east'] += value
        elif ship_coords['face'] == 'west':
            ship_coords['east'] -= value
    return


for el in directions:
    navigate(el[0], el[1])
manhattan_distance = abs(ship_coords['east']) + abs(ship_coords['north'])
print(manhattan_distance)

# part 2
# initialize the waypoint
ship_coords_part2 = {'face': 'east', 'east': 0, 'north': 0}
waypoint = {'east': 10, 'north': 1}


def update_waypoint(new_wp):
    waypoint['east'] = new_wp['east']
    waypoint['north'] = new_wp['north']
    return


def create_new_waypoint(wp, key, val):
    # using absolute values based on the location
    if key == 'east':
        # if east -> positive
        wp['east'] = abs(val)
    elif key == 'west':
        # if west -> negative
        wp['east'] = -abs(val)
    elif key == 'north':
        # if north -> positive
        wp['north'] = abs(val)
    elif key == 'south':
        # if south -> negative
        wp['north'] = -abs(val)
    return wp


def check_waypoint(direction, index):
    new_waypoint = {}
    new_key = None
    if direction == 'R':
        # means waypoint is east
        if waypoint['east'] > 0:
            new_key = coords_graph['east'][index - 1]
        # means waypoint is west
        elif waypoint['east'] < 0:
            new_key = coords_graph['west'][index - 1]
        elif waypoint['east'] == 0:
            new_key = 'east'
        new_waypoint = create_new_waypoint(new_waypoint, new_key, waypoint['east'])
        # means waypoint is north
        if waypoint['north'] > 0:
            new_key = coords_graph['north'][index - 1]
        # means waypoint is south
        elif waypoint['north'] < 0:
            new_key = coords_graph['south'][index - 1]
        elif waypoint['north'] == 0:
            new_key = 'north'
        new_waypoint = create_new_waypoint(new_waypoint, new_key, waypoint['north'])
    elif direction == 'L':
        # means waypoint is east
        if waypoint['east'] > 0:
            new_key = coords_graph['east'][-index]
        # means waypoint is west
        elif waypoint['east'] < 0:
            new_key = coords_graph['west'][-index]
        elif waypoint['east'] == 0:
            new_key = 'east'
        new_waypoint = create_new_waypoint(new_waypoint, new_key, waypoint['east'])
        # means waypoint is north
        if waypoint['north'] > 0:
            new_key = coords_graph['north'][-index]
        # means waypoint is south
        elif waypoint['north'] < 0:
            new_key = coords_graph['south'][-index]
        elif waypoint['north'] == 0:
            new_key = 'north'
        new_waypoint = create_new_waypoint(new_waypoint, new_key, waypoint['north'])
    update_waypoint(new_waypoint)
    return


def navigate_waypoints(action, value):
    if action == 'N':
        waypoint['north'] += value
    elif action == 'S':
        waypoint['north'] -= value
    elif action == 'E':
        waypoint['east'] += value
    elif action == 'W':
        waypoint['east'] -= value
    elif action == 'L' or action == 'R':
        # calculates the degree of the turn
        remainder = value // 90
        check_waypoint(action, remainder)
    elif action == 'F':
        east_increase = waypoint['east'] * value
        north_increase = waypoint['north'] * value
        ship_coords_part2['east'] += east_increase
        ship_coords_part2['north'] += north_increase
    return


for el in directions:
    navigate_waypoints(el[0], el[1])
manhattan_distance_2 = abs(ship_coords_part2['east']) + abs(ship_coords_part2['north'])
print(manhattan_distance_2)

file.close()
