import os

class Warehouse:
    warehouse: list[list]

    def get_warehouse(self,x,y):
        return self.warehouse[y][x]

    def set_warehouse(self,x,y,c):
        self.warehouse[y][x] = c

    def find_free(self,pos, dir):
        dx, dy = dir
        x, y = pos
        item = self.get_warehouse(x+dx, y+dy)
        if item == '.':
            return (x+dx, y+dy)
        if item == '#':
            return None
        return self.find_free((x+dx, y+dy), dir)
        
    # might_need_dirs = {'[': 1, ']': -1, '@': 0}
    def push(self, x,y,dx,dy) -> bool:
        push_rows = [{(x,y)}]
        while True:
            new_row={ (x+dx, y+dy) for x,y in push_rows[-1]}
            if all(self.get_warehouse(x,y) == '.' for x,y in new_row):
                break
            if any(self.get_warehouse(x,y) == '#' for x,y in new_row):
                return False
            # extend sideways to full pushed block
            if dx == 0:
                for x,y in set(new_row):
                    b = self.get_warehouse(x,y)
                    if b == '[':
                        new_row.add((x+1,y))
                    elif b == ']':
                        new_row.add((x-1,y))
            push_rows.append({ (x, y) for x,y in new_row if self.get_warehouse(x, y) != '.'})
        for row in reversed(push_rows):
            for x,y in row:
                self.set_warehouse(x+dx, y+dy, self.get_warehouse(x,y))
                self.set_warehouse(x,y,'.')
        return True

    def gps_score(self):
        sum_gps = 0
        for row_no, row in enumerate(self.warehouse):
            for col_no, c in enumerate(row):
                if c == 'O' or c =='[': sum_gps += 100 * row_no + col_no
        return sum_gps

    def to_str(self):
        return "\n".join("".join(c for c in r) for r in self.warehouse)

    def print(self):
        print(self.to_str())

    def __init__(self, warehouse, part2):
        if part2:
            wh = []
            for line in warehouse:
                r = []
                for c in line:
                    r.extend(list({'#': '##', 'O': '[]', '.': '..', '@': '@.'}[c]))
                wh.append(r)
            warehouse = wh
        self.warehouse = list(warehouse)

def read_input(filename):
    warehouse=[]
    cur_dir = os.path.dirname(__file__) 
    with open(os.path.join(cur_dir, filename), "r") as in_file:
        for line in in_file:
            if line == "\n": break
            warehouse.append(list(line.strip()))

        moves = "".join(map(str.strip, in_file.readlines()))
    return warehouse, moves

def solve1_old(warehouse, moves):
    warehouse = Warehouse(warehouse, False)
    warehouse.print()
    print (moves)

    robot, = ((row.index('@'), row_no) for row_no, row in enumerate(warehouse.warehouse) if '@' in row)
    print (robot)

    for move in moves:
        dir = {'<': (-1,0), '^': (0,-1), '>': (1,0), 'v': (0,1)}[move]
        free_spot = warehouse.find_free(robot, dir)
        if free_spot:
            assert warehouse.get_warehouse(*free_spot) == '.'
            warehouse.set_warehouse(*free_spot, 'O')
            warehouse.set_warehouse(*robot, '.')
            robot = tuple(r+d for r,d in zip(robot, dir))
            warehouse.set_warehouse(*robot, '@')
    warehouse.print()
    print (f"Part 1: Sum of GPS coordinates = {warehouse.gps_score()}")
    return warehouse.gps_score()

def solve1(warehouse, moves):
    warehouse = Warehouse(warehouse, False)
    warehouse.print()

    robot, = ((row.index('@'), row_no) for row_no, row in enumerate(warehouse.warehouse) if '@' in row)

    for move in moves:
        dir = {'<': (-1,0), '^': (0,-1), '>': (1,0), 'v': (0,1)}[move]
        if warehouse.push(*robot, *dir):
            robot = tuple(r+d for r,d in zip(robot, dir))
    warehouse.print()
    print (f"Part 1: Sum of GPS coordinates = {warehouse.gps_score()}")
    return warehouse.gps_score()

def solve2(warehouse, moves):
    warehouse = Warehouse(warehouse, True)
    warehouse.print()

    robot, = ((row.index('@'), row_no) for row_no, row in enumerate(warehouse.warehouse) if '@' in row)

    for move in moves:
        dir = {'<': (-1,0), '^': (0,-1), '>': (1,0), 'v': (0,1)}[move]
        # print(f"{move} with robot at {robot} => ")
        pushed = warehouse.push(*robot, *dir)
        if pushed:
            robot = tuple(r+d for r,d in zip(robot, dir))
        # warehouse.print()
    warehouse.print()
    print (f"Part 2: Sum of GPS coordinates = {warehouse.gps_score()}")
    return warehouse.gps_score()

if __name__== "__main__":
    wh, moves = read_input("input.txt")
    solve1(wh, moves)
    wh, moves = read_input("input.txt")
    solve2(wh, moves)