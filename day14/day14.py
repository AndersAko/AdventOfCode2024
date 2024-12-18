import os
import re

filename = "input.txt"
# size_x, size_y = (11,7)
size_x, size_y = (101, 103)

def move(r):
    x,y,vx,vy = r
    return ((x+vx) % size_x, (y+vy) % size_y, vx, vy)

def print_map(robots):
    for y in range(size_y):
        rs = [sum(map(lambda r: (x,y)==(r[0],r[1]), robots)) for x in range(size_x)]
        print("".join(map(lambda x: str(x) if x > 0 else ".", rs)))

def quadrant_score(robots):
    q1 = sum(1 for x,y,_,_ in robots if x < size_x // 2 and y < size_y // 2 )
    q2 = sum(1 for x,y,_,_ in robots if x < size_x // 2 and y > size_y // 2 )
    q3 = sum(1 for x,y,_,_ in robots if x > size_x // 2 and y < size_y // 2 )
    q4 = sum(1 for x,y,_,_ in robots if x > size_x // 2 and y > size_y // 2 )
    return q1 * q2 * q3 * q4

def ordered_score(robots):
    # Count direct neighbours, use as score of tree-like image
    rs = {(x,y) for x,y,_,_ in robots}
    score = sum(1 for x,y in rs if (x+1,y+1) in rs)
    return score

cur_dir = os.path.dirname(__file__) 
robots = []
with open(os.path.join(cur_dir, filename), "r") as in_file:
    for line in in_file:
        robot = re.match(r"p=([-\d]+),([-\d]+) v=([-\d]+),([-\d]+)", line).groups()
        robots.append(tuple(map(int, robot)))        

starting_robots = robots
print_map(robots)

for i in range(100):
    robots = list(map(move, robots))
    score = ordered_score(robots)
    # print (f"Step {i+1:3d}:")

print("100 seconds:")
print_map(robots)
print(f"Part 1: {quadrant_score(robots)}\n")

robots = starting_robots
seconds = 0
last_score = 0
while True:
    seconds += 1
    robots = list(map(move, robots))
    score = ordered_score(robots)
    # print(f"{seconds} => {score}")
    if score > 100: 
        print_map(robots)
        print(f"{seconds} => {score}")
    if score < last_score - 50: 
        print(f"{seconds} => {score}")
        break
    last_score = score
    # print (f"Step {i+1:3d}:")
