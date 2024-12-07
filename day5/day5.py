import os
from collections import defaultdict

filename = "input.txt"

cur_dir = os.path.dirname(__file__) 
with open(os.path.join(cur_dir, filename), "r") as in_file:
    lines = in_file.readlines()

read_state = 1
rules = defaultdict(set)
before = defaultdict(set)
updates = []
for line in lines:
    line = line.strip()
    if read_state == 1: 
        if line == "": 
            read_state = 2
            continue
        rule = line.split("|")
        rules[rule[0]].add(rule[1])
        before[rule[1]].add(rule[0])
    else:
        updates.append(line.split(","))

print ("Rules: ", rules)
print ("Updates: ", updates)

def is_OK(update):
    printed = []
    for page in update:
        if rules[page].isdisjoint(set(printed)):
            printed.append(page)
        else:
            print (f"Page {page} breaks {page}|{rules[page]} since one in {printed} is already printed")
            return False
    else:
        print (f"Report: {update} is OK, middle page num is {printed[len(printed)//2]}")
        return True

sum_middle = 0
for update in updates:
    if is_OK(update):
        sum_middle += int(update[len(update)//2])

print ("Part1: Sum of middle page nums = ", sum_middle)

# Part2
def place(p, to_print, printed):
    if p not in to_print:
        return
    for print_before in  list(p for p in before[p] if p in to_print):
        place (print_before, to_print, printed)
    printed.append(p)
    to_print.remove(p)

sum_middle = 0
for update in (u for u in updates if not is_OK(u)):
    printed = []
    print(update, "=>", end=" ")
    for p in list(update):
        place(p, update, printed)

    print(f"Update = {printed}")
    sum_middle += int(printed[len(printed)//2])
print ("Part 2: Sum of middle page nums = ", sum_middle)
