from enum import Enum

filename = "input.txt"

class Dir(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3

with open(filename, "r") as in_file:
    lines = in_file.readlines()

y_guard = list(map(lambda x: '^' in x, lines)).index(True)
x_guard = lines[y_guard].index('^')

guard = (x_guard, y_guard, Dir.Up)

def walk (pos):
    (x,y,d) = pos
    dx, dy = 0, 0
    if d == Dir.Up: dy = -1
    elif d == Dir.Right: dx = 1
    elif d == Dir.Down: dy = 1
    elif d == Dir.Left: dx = -1
    if 0 > y+dy or y+dy >= len(lines) or 0 > x+dx or x+dx >= len(lines[0]):
        return None
    if lines[y+dy][x+dx] == "#":
        d = Dir((d.value + 1) % 4)
    else:
        y = y+dy
        x = x+dx
    return (x,y,d)

visited = set()
while guard:
    print (guard)
    x,y, _ = guard
    visited.add((x,y))
    guard = walk(guard)

print (f"The guard visited {len(visited)} locations")
print (visited)