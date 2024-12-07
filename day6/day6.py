from enum import Enum
import os

filename = "input.txt"

class Dir(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3

cur_dir = os.path.dirname(__file__) 
with open(os.path.join(cur_dir, filename), "r") as in_file:
    lines = in_file.readlines()

y_guard = list(map(lambda x: '^' in x, lines)).index(True)
x_guard = lines[y_guard].index('^')

guard = (x_guard, y_guard, Dir.Up)

def walk (pos, block=None):
    if pos in visited: return False
    visited.add(pos)
    (x,y,d) = pos
    dx, dy = 0, 0
    if d == Dir.Up: dy = -1
    elif d == Dir.Right: dx = 1
    elif d == Dir.Down: dy = 1
    elif d == Dir.Left: dx = -1
    if 0 > y+dy or y+dy >= len(lines) or 0 > x+dx or x+dx >= len(lines[0]):
        return None
    if lines[y+dy][x+dx] == "#" or (x+dx, y+dy) == block:
        d = Dir((d.value + 1) % 4)
    else:
        y = y+dy
        x = x+dx
    return (x,y,d)

visited = set()
while guard:
    print (guard)
    guard = walk(guard)

visited_loc = {(x,y) for (x,y,_) in visited}
print (f"Part1: The guard visited {len(visited_loc)} locations")

# Part2
possible_blocks = 0
for block in ((x,y) for (x,y) in visited_loc if x !=x_guard or y != y_guard):
    guard = (x_guard, y_guard, Dir.Up)
    visited = set()
    while guard:
        guard = walk(guard, block)
    if guard == False:
        print (f"Blocked by block at {block}")
        possible_blocks += 1
    
print (f"Part2: Number of locations that causes a loop:{possible_blocks}")