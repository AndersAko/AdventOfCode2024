import os

filename = "input.txt"

cur_dir = os.path.dirname(__file__) 
with open(os.path.join(cur_dir, filename), "r") as in_file:
    orig_numbers = list(map(int, in_file.read().split(' ')))

def blink(numbers:list):
    result = []
    for n in numbers:
        if isinstance(n,list):
            result.append(blink(n)) 
        else:
            str_n = str(n)
            if n == 0:
                result.append(1)
            elif len(str_n) % 2 == 0:
                num_digits = len(str_n)
                result.append(int(str_n[0:num_digits//2]))
                result.append(int(str_n[num_digits//2:]))
            else:
                result.append(n * 2024)
    return result

numbers = orig_numbers    
print(numbers)
for _ in range(6):
    numbers = blink(numbers)
    print(numbers)

numbers = orig_numbers
for i in range(25):
    numbers = blink(numbers)
    print(f"{i+1}: {len(numbers)}")

print("Part2")
numbers = [1]
for i in range(15):
    numbers = blink(numbers)
    print(f"{i+1}: {numbers}")
