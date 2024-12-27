from collections import defaultdict
import os
from heapq import heappop, heappush

filename = "input.txt"

def read_input(filename):
    cur_dir = os.path.dirname(__file__) 

    with open(os.path.join(cur_dir, filename), "r") as in_file:
        track = list(map(str.strip, in_file.readlines()))

    start, = ((row.index('S'), row_no) for row_no, row in enumerate(track) if 'S' in row)
    end, = ((row.index('E'), row_no) for row_no, row in enumerate(track) if 'E' in row)
    x,y = start
    assert track[y][x] == 'S'
    track[y] = track[y].replace('S','.')
    x,y = end
    assert track[y][x] == 'E'
    track[y] = track[y].replace('E','.')
    return track, start, end

def remain(x,y,end):
    x1, y1, = end
    return abs(y1 - y) + abs(x1 - x)

# def moves(map, state):
#     x,y,cheat,p = state
#     moves = []
#     for dx, dy in [(0,-1), (1,0), (0,1), (-1,0)]:
#         if map[y+dy][x+dx] != '#':
#             moves.append((x+dx,y+dy, cheat, p+[(x+dx,y+dy)]))
#         elif cheat is None:
#             moves.append((x+dx,y+dy,(x,y,x+dx,y+dy),p+[(x+dx,y+dy)]))
#     return moves

# def find_shortest_path(map, cheat, start, end):
#     visited = {}
#     search = []
#     heappush(search, (0, *start, cheat, 0))
#     while search:
#         _, *state_to_check = heappop(search)
#         print(state_to_check)
#         for next_state in moves(map, state_to_check):
#             x,y,_,path = next_state
#             if (x,y) == end:
#                 return path
#             if (x,y) not in visited or len(path) < visited[(x,y)]:
#                 visited[(x,y)] = len(path)
#                 heappush(search, (path + remain(x,y,end), *next_state))
#     print("No solution found")

def moves_path(map, state):
    x,y,cheat,p = state
    moves = []
    for dx, dy in [(0,-1), (1,0), (0,1), (-1,0)]:
        if map[y+dy][x+dx] != '#' or cheat == (x,y,x+dx,y+dy):
            moves.append((x+dx,y+dy, cheat, p+[(x+dx,y+dy)]))
    return moves

def moves(map, state):
    x,y,cheat,p = state
    moves = []
    for dx, dy in [(0,-1), (1,0), (0,1), (-1,0)]:
        if map[y+dy][x+dx] != '#' or cheat == (x,y,x+dx,y+dy):
            moves.append((x+dx,y+dy, cheat, p+1))
    return moves

def find_shortest_path(map, cheat, start, end):
    visited = set()
    search = []
    heappush(search, (0, *start, cheat, [start]))
    while search:
        _, *state_to_check = heappop(search)
        x,y,*_ = state_to_check
        if (x,y) not in visited:
            visited.add((x,y))
            # print(state_to_check)
            for next_state in moves_path(map, state_to_check):
                x,y,_,path = next_state
                if (x,y) == end:
                    return path
                if (x,y) not in visited:
                    heappush(search, (len(path) + remain(x,y,end), *next_state))
    print("No solution found")

def find_shortest_path_with_limit(map, cheat, start, end, max_length):
    visited = set()
    search = []
    heappush(search, (0, *start, cheat, 1))
    while search:
        _, *state_to_check = heappop(search)
        x,y,*_ = state_to_check
        if (x,y) not in visited:
            visited.add((x,y))
            # print(state_to_check)
            for next_state in moves(map, state_to_check):
                x,y,_,path = next_state
                if (x,y) == end:
                    return path
                score = path + remain(x,y,end)
                if (x,y) not in visited and score <= max_length:
                    heappush(search, (score, *next_state))
    # print("No solution found")

def find_shortest_path_with_cheats(map, start, end, max_length):
    visited = set()
    search = []
    heappush(search, (0, *start, None, 1))
    best_paths
    while search:
        _, *state_to_check = heappop(search)
        x,y,*_ = state_to_check
        if (x,y) not in visited:
            visited.add((x,y))
            # print(state_to_check)
            for next_state in moves(map, state_to_check):
                x,y,_,path = next_state
                if (x,y) == end:
                    return path
                score = path + remain(x,y,end)
                if (x,y) not in visited and score <= max_length:
                    heappush(search, (score, *next_state))
    # print("No solution found")

# cheat: None = not cheated yet; (start, length): during cheat 
# def find_paths(map, cheat_start, cheat_len, cheat_end, start, end):
#     x,y = start
#     x1,y1 = end
#     paths = {}  # cheat(start,end): length
#     for dx, dy in [(0,-1), (1,0), (0,1), (-1,0)]:
#         if map[y+dy][x+dx] != '#':
#             for cheat, length in find_paths(map, cheat, (x+dx, y+dy), )
            
#             or cheat == (x,y,x+dx,y+dy):


def solve1(filename, limit):
    track, start, end = read_input(filename)
    size_x = len(track[0])
    size_y = len(track)

    path_without_cheat = find_shortest_path(track, False, start, end)
    print(f"Shortest path without cheat: {len(path_without_cheat)}")

    cheat_savings = defaultdict(int)
    for (x,y) in path_without_cheat:
        cheats = [(x,y,x+dx,y+dy) for dx, dy in [(0,-1), (1,0), (0,1), (-1,0)] 
                  if track[y+dy][x+dx] == '#' and x+dx > 0 and x+dx < size_x - 1 and y+dy > 0 and y+dy < size_y - 1]
        for cheat in cheats:
            shortest_with_cheat = find_shortest_path_with_limit(track, cheat, start, end, len(path_without_cheat)-limit)
            if shortest_with_cheat is None:
                continue
            savings = len(path_without_cheat) - shortest_with_cheat
            if savings > 0:
                print (f"Cheat at {cheat} saves {savings} ps")
                cheat_savings[savings] += 1
    for savings in cheat_savings:
        print(f"A total of {cheat_savings[savings]} cheats save {savings} ps")

    num_viable_cheats = sum(num for save, num in cheat_savings.items() if save >= limit)
    print(f"Part1: A total of {num_viable_cheats} cheats will save at least {limit} ps")
    return num_viable_cheats

if __name__ == "__main__":
    solve1(filename, 100)
    # solve2(filename)

