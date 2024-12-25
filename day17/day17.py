import os
import re

def read_input(filename):
    cur_dir = os.path.dirname(__file__) 

    with open(os.path.join(cur_dir, filename), "r") as in_file:
        registers = {}
        for line in in_file:
            if line == '\n': break
            register, value = re.match(r"Register (\w+): (\d+)", line).groups()
            registers[register] = int(value)
        
        program, = re.match(r"Program: ([\d,]+)+", next(in_file)).groups()
        program = list(map(int, program.split(',')))

        return registers, program

class Computer:
    A: int
    B: int
    C: int
    ip: int

    def __init__(self, registers):
        self.A = registers['A']
        self.B = registers['B']
        self.C = registers['C']
        self.ip = 0

    def combo(self, operand):
        if operand < 4:
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        raise Exception(f"Received invalid operand {operand}")

    def execute_instr(self, instr, operand):
        if instr == 0:      # adv
            denom = 2 ** self.combo(operand)
            self.A = self.A // denom
        elif instr == 1:    # bxl
            self.B = self.B ^ operand
        elif instr == 2:    # bst
            self.B = self.combo(operand) % 8
        elif instr == 3:    # jnz
            if self.A != 0:
                self.ip = operand
                return None
        elif instr == 4:    # bxc
            self.B = self.B ^ self.C
        elif instr == 5:    # out
            output = self.combo(operand) % 8
            # print(output)
            self.ip += 2
            return output
        elif instr == 6:    # bdv
            denom = 2 ** self.combo(operand)
            self.B = self.A // denom
        elif instr == 7:    # cdv
            denom = 2 ** self.combo(operand)
            self.C = self.A // denom
        self.ip += 2
        return None

    def execute(self, program):
        self.ip = 0
        output = []
        while self.ip < len(program)-1:
            result = self.execute_instr(program[self.ip], program[self.ip+1])
            if result is not None:
                output.append(result)
        return output

    def execute_part_2(self, program):
        self.ip = 0
        output = []
        while self.ip < len(program)-1:
            result = self.execute_instr(program[self.ip], program[self.ip+1])
            if result is not None:
                if program[len(output)] != result:
                    return None
                output.append(result)
        return output


def solve1(filename):
    registers, program = read_input(filename)

    computer = Computer(registers)
    output = computer.execute(program)
    print("Part1")
    return ",".join(map(str, output))

def solve2(filename):
    registers, program = read_input(filename)
    
    for a in range(1000000000):
        computer = Computer(registers)
        computer.A = a
        output = computer.execute_part_2(program)
        if output == program:
            print(f"Part2: output = program at {a}")
            print(",".join(map(str, output)))
            return a
    

if __name__ == "__main__":
    filename = "input.txt"
    result = solve1(filename)
    print (result)
    result = solve2(filename)
    print (result)
