from collections import defaultdict
from itertools import combinations, permutations
from math import gcd
import os

filename = "input.txt"

cur_dir = os.path.dirname(__file__) 
with open(os.path.join(cur_dir, filename), "r") as in_file:
    lines = list(map(str.strip, in_file.readlines()))

size_x = len(lines[0])
size_y = len(lines)

antennas = defaultdict(list)

for x in range(size_x):
    for y in range(size_y):
        if lines[y][x] != '.':
            antennas[lines[y][x]].append((x,y))

def add_node(node):
    x,y = node
    if x >=0 and x < size_x and y >= 0 and y < size_y:
        antinodes.add(node)

antinodes = set()
for freq in antennas.keys():
    for pair in combinations(antennas[freq], 2):
        (x1,y1), (x2,y2) = pair
        anti_node1 = (x1-(x2-x1), y1-(y2-y1))
        anti_node2 = (x2+(x2-x1), y2+(y2-y1))
        print(freq, pair, "=>", anti_node1, anti_node2)
        add_node(anti_node1)
        add_node(anti_node2)

print("Part 1", len(antinodes))

# Part 2
antinodes = set()
for freq in antennas.keys():
    for pair in combinations(antennas[freq], 2):
        (x1,y1), (x2,y2) = pair
        dx, dy = x2 - x1, y2 - y1
        d = gcd (dx, dy)
        dx /= d
        dy /= d
        x,y = x1, y1
        an = set()       
        while x >= 0 and x < size_x and y >= 0 and y < size_y:
            an.add((x,y))
            x += dx
            y += dy
        x,y = x1, y1
        while x >= 0 and x < size_x and y >= 0 and y < size_y:
            an.add((x,y))
            x -= dx
            y -= dy
        print (f"{freq}:{pair} [{dx, dy}] => {an}")
        antinodes.update(an)

print (antinodes)
print ("Part 2: ", len(antinodes))