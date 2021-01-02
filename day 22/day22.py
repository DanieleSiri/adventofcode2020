# https://adventofcode.com/2020/day/22
from array import array
file = open('day22_data', 'r')
file_split = file.read().split("\n\n")
player_1 = array('i', (int(x) for x in file_split[0].split("\n")[1:]))
player_2 = array('i', (int(x) for x in file_split[1].split("\n")[1:]))

turn = 0
while True:
    if len(player_1) == 0 or len(player_2) == 0:
        break
    if player_1[0] > player_2[0]:
        card = player_1[0]
        player_1.pop(0)
        # appending winning card and then the won card from the other player
        player_1.extend((card, player_2[0]))
        player_2.pop(0)
    elif player_2[0] > player_1[0]:
        card = player_2[0]
        player_2.pop(0)
        player_2.extend((card, player_1[0]))
        player_1.pop(0)
    turn += 1

winning_team = (player_1 if len(player_2) == 0 else player_2)
winning_team.reverse()
result = 0
for i, val in enumerate(winning_team):
    result += (i + 1) * val
print(result)

file.close()
