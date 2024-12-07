import os

filename = "input.txt"

cur_dir = os.path.dirname(__file__) 
with open(os.path.join(cur_dir, filename), "r") as in_file:
    lines = in_file.readlines()

def calc_options (expr: list[int], part2=False):
    if len(expr) == 1:
        return expr
    
    results = []
    for lh_result in calc_options(expr[:-1], part2):
        for operator in ["+", "*", "||"]:
            if operator == "+":
                results.append(lh_result + expr[-1])
            elif operator == "*":
                results.append(lh_result * expr[-1])
            elif part2 and operator == "||":
                results.append(int(str(lh_result) + str(expr[-1])))
    return results

calibration_sum = 0
for line in lines:
    parts = line.split(":")
    test_value = int(parts[0])
    operands = list(map(int, (x for x in parts[1].split(" ") if x!= "")))

    if test_value in calc_options(operands):
        print(f"Possible to match {test_value}")
        calibration_sum += test_value

print (f"Part1: Calibration sum = {calibration_sum}")
calibration_sum = 0
for line in lines:
    parts = line.split(":")
    test_value = int(parts[0])
    operands = list(map(int, (x for x in parts[1].split(" ") if x!= "")))

    if test_value in calc_options(operands, True):
        print(f"Possible to match {test_value}")
        calibration_sum += test_value
print (f"Part2: Calibration sum = {calibration_sum}")
