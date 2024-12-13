import os

filename = "input.txt"

cur_dir = os.path.dirname(__file__) 
with open(os.path.join(cur_dir, filename), "r") as in_file:
    garden = list(map(str.strip, in_file.readlines()))

def plot_size(plant: str, x, y, sides_checked:set) -> tuple[int, int]:
    assert not (x,y) in visited

    visited.add((x,y))
    size, perimeter, sides = 1,0,0
    for dx, dy in [(0,-1), (1,0), (0,1), (-1,0)]:
        if (x+dx<0 or x+dx >= len(garden[0]) or
            y+dy<0 or y+dy >= len(garden) or
            garden[y+dy][x+dx] != plant):
            perimeter += 1
            if (x,y,dx,dy) not in sides_checked:
                sides += 1
                for sdx, sdy in [(-1,0), (1,0)] if dx == 0 else [(0,-1), (0,1)]:
                    x1 = x
                    y1 = y
                    while (x1 >= 0 and x1 < len(garden[0]) and 
                           y1 >= 0 and y1 < len(garden) and garden[y1][x1] == plant):
                        if (x1+dx<0 or x1+dx >= len(garden[0]) or
                            y1+dy<0 or y1+dy >= len(garden) or
                            garden[y1+dy][x1+dx] != plant):
                            sides_checked.add((x1,y1,dx,dy))
                        else:
                            break
                        x1 += sdx
                        y1 += sdy
        elif (x+dx,y+dy) not in visited:
            s,p,ss = plot_size(plant, x+dx, y+dy, sides_checked)
            size += s
            perimeter += p
            sides += ss
    return size,perimeter,sides

visited = set()
plots = []

price1 = 0
price2 = 0
for y,g in enumerate(garden):
    for x,_ in enumerate(g):
        if (x,y) not in visited:
            plant = garden[y][x]
            size, perimeter, sides = plot_size(plant, x, y, set())
            price1 += size * perimeter
            price2 += size * sides
            plots.append((plant, size,perimeter, sides))
print(plots)

print (f"Part1: Garden plot price {price1}")
print (f"Part2: Garden plot price {price2}")
