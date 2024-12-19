import os

filename = "input.txt"

non_matching = set()
def match(design):
    if design in non_matching: return False
    print(f"Matching {design}")
    for t in (t for t in towels if design.startswith(t)):
        remaining = design[len(t):]
        if len(remaining) == 0 or match(remaining):
            return True
    non_matching.add(design)
    return False

match_count = {}
def count_match(design):
    if design in match_count: return match_count[design]
    print(f"Matching {design}")
    possible = 0
    for t in (t for t in towels if design.startswith(t)):
        remaining = design[len(t):]
        if len(remaining) == 0:
            possible += 1
            continue
        possible += count_match(remaining)
    match_count[design] = possible
    return possible


cur_dir = os.path.dirname(__file__) 
with open(os.path.join(cur_dir, filename), "r") as in_file:
    towels = list(map(str.strip, in_file.readline().split(",")))
    next(in_file)
    designs = list(map(str.strip, in_file.readlines()))

print (f"Towel patterns {towels}")
print (f"Designs {designs}")
possible = 0
for design in designs:
    if match(design):
        print(f"Design {design} is possible")
        possible += 1
    else:
        print(f"Design {design} is NOT possible")

print (f"Part1: {possible} designs can be made")

all_possible = 0
for design in designs:
    options = count_match(design)
    if options:
        print(f"Design {design} is possible in {options} ways")
        all_possible += options

print (f"Part2: {all_possible} ways are possible")