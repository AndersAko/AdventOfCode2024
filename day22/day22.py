from collections import defaultdict
import os
import itertools

filename = "input.txt"

def read_input(filename):
    cur_dir = os.path.dirname(__file__) 

    with open(os.path.join(cur_dir, filename), "r") as in_file:
        secrets = list(map(int, in_file.readlines()))
    return secrets

def next_secret_gen(secret):
    for _ in range(2000):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
        yield secret
    
def solve1(filename):
    secrets = read_input(filename)

    sum_2000_secrets = 0
    for secret in secrets:
        gen = next_secret_gen(secret)
        *_, secret = gen
        # print(secret)
        sum_2000_secrets += secret
    print (f"Part1: Sum of the 2000th secrets is {sum_2000_secrets}")
    return sum_2000_secrets

def solve2(filename):
    secrets = read_input(filename)

    prices = []
    for secret in secrets:
        seller_prices = {}
        gen = next_secret_gen(secret)
        last_price = secret % 10
        sequence = ()
        for i, price in enumerate(gen):
            price = price % 10
            if i < 4:
                sequence += (price - last_price),
            else:
                sequence = sequence[1:] + ((price - last_price),)
                if sequence not in seller_prices:
                    seller_prices[sequence] = price
                else:
                    pass
            last_price = price
        prices.append(seller_prices)
    # print(prices)
    all_sequences = set()
    for seller in prices:
        all_sequences |= set(seller.keys())
    print(f"Found {len(all_sequences)} sequences to test")
    best_bananas = 0
    best_sequence = None
    for seq in all_sequences:
        bananas = sum(price[seq] for price in prices if seq in price)
        if bananas > best_bananas:
            best_bananas = bananas
            best_sequence = seq
    print(f"Part2: the best sequence is {best_sequence}, which gives {best_bananas}")    
    return best_bananas

if __name__ == "__main__":
    solve1(filename)
    solve2(filename)
