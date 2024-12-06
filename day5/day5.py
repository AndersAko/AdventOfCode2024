from collections import defaultdict


print("Hello")
filename = "input.txt"

with open(filename, "r") as in_file:
    lines = in_file.readlines()

read_state = 1
rules = defaultdict(set)
updates = []
for line in lines:
    line = line.strip()
    print(f"#{line}#")
    if read_state == 1: 
        if line == "": 
            read_state = 2
            continue
        rule = line.split("|")
        rules[rule[0]].add(rule[1])
    else:
        updates.append(line.split(","))

print ("Rules: ", rules)
print ("Updates: ", updates)

sum_middle = 0
for update in updates:
    printed = []
    for page in update:
        if rules[page].isdisjoint(set(printed)):
            printed.append(page)
        else:
            print (f"Page {page} breaks {rules[page]} since {printed} is already printed")
            break
    else:
        print (f"Report: {update} is OK, middle page num is {printed[len(printed)//2]}")
        sum_middle += int(printed[len(printed)//2])

print ("Part1: Sum of middle page nums = ", sum_middle)