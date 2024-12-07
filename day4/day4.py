import os

filename = "input.txt"

cur_dir = os.path.dirname(__file__) 
with open(os.path.join(cur_dir, filename), "r") as in_file:
    lines = list(map(str.strip, in_file.readlines()))

def find_xmas(lines, x, y):
    if lines[y][x] != 'X': return 0
    matches = 0
    for dx,dy in [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1)]:
        if find_word(lines, 'XMAS', x, y, dx, dy):
            print(f"Match at {x,y} ({dx,dy})")
            matches += 1
    return matches

def find_word(lines, word, x, y, dx, dy):
    if lines[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True
    if x+dx < 0 or x+dx >= len(lines[0]):
        return False
    if y+dy < 0 or y+dy >= len(lines):
        return False

    return find_word(lines, word[1:], x+dx, y+dy, dx, dy)

num_matches = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        num_matches += find_xmas(lines, x, y)
print (f"Part1: Total number of matches: {num_matches}")

def is_x_mas(lines, x,y):
    if lines[y][x] != 'A':
        return False
    if ((lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S' or lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M') and
        (lines[y-1][x+1] == 'S' and lines[y+1][x-1] == 'M' or lines[y-1][x+1] == 'M' and lines[y+1][x-1] == 'S')):
        return True

num_matches = 0
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        if is_x_mas(lines, x, y):
            print(f"X-MAS at {y,x}")
            num_matches += 1
print (f"Part2: Total number of matches: {num_matches}")
