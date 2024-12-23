from dataclasses import dataclass
import os
from enum import IntEnum
from heapq import heappop, heappush

filename="input.txt"

class Dir(IntEnum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3

def read_map(filename):
    cur_dir = os.path.dirname(__file__) 
    with open(os.path.join(cur_dir, filename), "r") as in_file:
        maze = list(map(str.strip, in_file.readlines())    )
    start, = ((row.index('S'), row_no) for row_no, row in enumerate(maze) if 'S' in row)
    end, = ((row.index('E'), row_no) for row_no, row in enumerate(maze) if 'E' in row)
    return maze, start, end

@dataclass
class State:
    x: int
    y: int
    d: Dir

def remain(x,y,d, end):
    x1, y1 = end
    score = abs(x1-x) + abs(y1-y)
    turns = 0
    if x1 < x and d != Dir.Left:    turns += 1
    if x1 > x and d != Dir.Right:   turns += 1
    if y1 < y and d != Dir.Up:      turns += 1
    if y1 > y and d != Dir.Down:    turns += 1
    score += turns * 1000
    return score

def moves(map, state):
    x,y,d,s,p = state
    dx = 1 if d is Dir.Right else -1 if d is Dir.Left else 0
    dy = 1 if d is Dir.Down else -1 if d is Dir.Up else 0
    possible = [(x,y,Dir((d+1)%4),s+1000,p), (x,y,Dir((d-1)%4),s+1000,p), (x+dx,y+dy,d,s+1,p+[(x+dx,y+dy)])]
    return list((x,y,d,s,p) for (x,y,d,s,p) in possible if map[y][x]!='#')

def find_shortest_path(map, start, end):
    visited = {}
    search = []
    heappush(search, (0, *start, Dir.Right, 0, [start]))
    best_paths = []
    best_score = None
    while search:
        _, *state_to_check = heappop(search)
        x,y,d,s,*_ = state_to_check
        visited[(x,y,d)] = s
        for next_state in moves(map, state_to_check):
            x,y,d,score,path = next_state
            if (x,y) == end:
                if best_score is None or score <= best_score:
                    best_score = score
                    best_paths.append(path)
            if (x,y,d) not in visited or score <= visited[(x,y,d)]:
                heappush(search, (score + remain(x,y,d,end), *next_state))
    return best_score, best_paths
    print("No solution found")

def solve1():
    map, start, end = read_map(filename)
    
    score, _ = find_shortest_path(map, start, end)

    print(f"Part1: lowest score is: {score}")

def solve2():
    map, start, end = read_map(filename)
    
    score, paths = find_shortest_path(map, start, end)
    good_tiles = { t for p in paths for t in p}
    print(f"Part2: lowest score is still: {score}. Possible paths: {paths}")
    print(f"Good spectator tiles: {len(good_tiles)}")
if __name__ == "__main__":
    solve1()
    solve2()