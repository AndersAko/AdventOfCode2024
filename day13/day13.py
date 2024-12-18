from dataclasses import dataclass
import os
import re
from math import isclose
# from sympy.solvers.diophantine import diophantine
# from sympy import Eq, symbols, solve

filename = "input.txt"

@dataclass
class Machine:
    button_A: tuple[int, int]
    button_B: tuple[int, int]
    prize: tuple[int,int]

def presses(a_x, a_y, b_x, b_y, t_x, t_y):
    denom = a_y - b_y * a_x / b_x
    assert denom != 0

    a = (t_y - b_y * t_x / b_x) / denom
    b = t_x / b_x - a_x / b_x * a
    return a,b

cur_dir = os.path.dirname(__file__)
machines = []
with open(os.path.join(cur_dir, filename), "r") as in_file:
    for line in in_file:
        button_a = re.match(r"Button A: X([\+\d]+).*Y([\+\d]+)", line).groups()
        button_b = re.match(r"Button B: X([\+\d]+).*Y([\+\d]+)", next(in_file)).groups()
        target = re.match(r"Prize: X=([\d]+).*Y=([\d]+)", next(in_file)).groups()
        next(in_file, None)
        machines.append(Machine(tuple(map(int, button_a)),
                                tuple(map(int, button_b)),
                                tuple(map(int, target)))
                        )
# print (machines)

total_cost = 0
for machine in machines:
    denom = machine.button_A[1] - machine.button_B[1] * machine.button_A[0] / machine.button_B[0]
    if denom == 0:
        print("Handle this!")
        raise
    else:
        a,b = presses(*machine.button_A, *machine.button_B, *machine.prize)
        # a = (machine.prize[1] - machine.button_B[1] * machine.prize[0] / machine.button_B[0]) / denom
        # b = machine.prize[0] / machine.button_B[0] - machine.button_A[0] / machine.button_B[0] * a
        if isclose(a, round(a), abs_tol=1e-10)  and isclose(b, round(b), abs_tol=1e-10):
            cost = 3 * round(a) + round(b)
            total_cost += cost
        else:
            print(f"Not possible for {machine}: => {a=} {b=} = {cost}")
            continue
        print(f"{machine}: => {a=} {b=} = {cost}")
print(f"Part 1: total cost = {total_cost}\n")

total_cost = 0
for machine in machines:
    denom = machine.button_A[1] - machine.button_B[1] * machine.button_A[0] / machine.button_B[0]
    if denom == 0:
        print("Handle this!")
        raise
    else:
        prize = (machine.prize[0] + 10000000000000, machine.prize[1] + 10000000000000)
        a,b = presses(*machine.button_A, *machine.button_B, *prize)
        a1 = round(a * 0.99999)
        b1 = round(b * 0.99999)
        prize = (prize[0] - a1 * machine.button_A[0] - b1 * machine.button_B[0],
                 prize[1] - a1 * machine.button_A[1] - b1 * machine.button_B[1])
        a,b = presses(*machine.button_A, *machine.button_B, *prize)

        if isclose(a, round(a)) and isclose(b, round(b)):
            cost = 3 * (round(a) + a1) + round(b) + b1
            total_cost += cost
        else:
            print(f"Not possible for {machine}: => {a=} {a1} {b=} {b1=} = {cost}")
            continue
        print(f"{machine}: => {a=} {b=} = {cost}")
print(f"Part 2: total cost = {total_cost}")