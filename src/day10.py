# --- Day 10: Adapter Array ---

from collections import defaultdict


def joltage_differences(adapters):
    differences = defaultdict(int)
    current = 0
    for next in adapters:
        differences[next - current] += 1
        current = next
    differences[3] += 1  # the device has 3 jolts more than the final adapter
    return differences


def distinct_ways_from(adapter, adapters, cached_results):
    if adapter == max(adapters):
        # if this is the last adapter (it will always match the end device), count this path
        return 1
    if adapter in cached_results:
        # if this adapter has already been processed, return its result
        return cached_results[adapter]
    count = 0
    for j in range(1, 4):
        if adapter + j in adapters:
            count += distinct_ways_from(adapter + j, adapters, cached_results)
    cached_results[adapter] = count
    return count


def distinct_ways(adapters):
    socket = 0
    return distinct_ways_from(socket, adapters, cached_results={})


if __name__ == '__main__':
    print('Day 10: Adapter Array')
    print('---------------------')

    with open('../res/day10.txt') as file:
        adapters = sorted(int(n) for n in file.readlines())

    differences = joltage_differences(adapters)
    print(f'{differences[1]} (1-jolt) * {differences[3]} (3 jolt) = {differences[1] * differences[3]}')

    c = distinct_ways(adapters)
    print(f'Distinct ways: {c}')
