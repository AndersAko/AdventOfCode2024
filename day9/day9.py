import os
from enum import Enum

class State (Enum):
    File = 1
    Free = 2

filename = "input.txt"

def checksum():
    checksum = 0
    for ix in range(len(disk)):
        checksum += disk[ix] * ix if disk[ix] != -1 else 0
    return checksum

def read_map():
    cur_dir = os.path.dirname(__file__) 
    with open(os.path.join(cur_dir, filename), "r") as in_file:
        line = in_file.read()
    state = State.File
    file_ix = 0
    disk = []
    file_size = {}

    for c in line:
        for _ in range(int(c)):
            if state is State.File:
                disk.append(file_ix)
            else:
                disk.append(-1)
        if state is State.File:
            file_size[file_ix] = int(c)
            file_ix += 1
            state = State.Free
        else:
            state = State.File
    return disk, file_size

# Compact part 1
disk, _ = read_map()
first_free = disk.index(-1)
last_block = len(disk)-1

while first_free < last_block:
    if disk[last_block] != -1:
        disk[first_free] = disk[last_block]
        disk[last_block] = -1
        first_free = disk.index(-1, first_free)
    last_block -= 1

print(f"Part1: checksum = {checksum()}")

def find_free(size, cur_pos):
    ix = disk.index(-1)
    s = size
    while ix < cur_pos:
        if s == 0:
            return ix - size
        if disk[ix] == -1: 
            s -= 1
            ix += 1
        else:
            ix = disk.index(-1, ix)
            s = size
    return -1

disk, file_size = read_map()
last_block = len(disk)-1
while last_block > 0:
    if disk[last_block] != -1:
        file_id = disk[last_block]
        free = find_free(file_size[file_id], last_block)
        if free != -1:
            for i in range(file_size[file_id]):
                assert disk[free + i] == -1
                disk[free + i] = file_id
                disk[last_block] = -1
                last_block -= 1
        else: 
            last_block -= file_size[file_id]
    else:
        last_block -= 1

print(f"Part2: checksum = {checksum()}")
