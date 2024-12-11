from collections import defaultdict
from itertools import combinations, permutations
from math import gcd
import os

filename = "input.txt"

cur_dir = os.path.dirname(__file__) 
with open(os.path.join(cur_dir, filename), "r") as in_file:
    lines = list(map(str.strip, in_file.readlines()))

def score(x,y, level):
    if x<0 or x >= len(lines[0]): return set(), 0
    if y<0 or y >= len(lines): return set(), 0
    if int(lines[y][x]) != level: return set(), 0
    if level == 9: return {(x,y)}, 1

    sum_destinations = set()
    sum_trails = 0
    for dx,dy in [(0,-1), (1,0), (0,1), (-1,0)]:
        destinations, trails = score(x+dx, y+dy, level+1)
        sum_destinations |= destinations
        sum_trails += trails
    return sum_destinations, sum_trails

# total_score = sum(score(x,y,0) for x in range(len(lines[0])) for y in range(len (lines)))
print (lines)
total_score = 0
total_rating = 0
for x in range(len(lines[0])):
    for y in range(len (lines)):
        s, t = score(x,y,0)
        print(f"Trailhead at {x,y} leads to {s} in {t} distinct ways")
        total_score += len(s)
        total_rating += t

print(f"Part1: score : {total_score}")
print(f"Part2: rating : {total_rating}")