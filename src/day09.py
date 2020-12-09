# --- Day 9: Encoding Error ---

def find_decomposition(n, candidates):
    for a in candidates:
        for b in candidates:
            if a + b == n and a != b:
                return True
    return False


def find_first(data, preamble_length=25):
    for i, n in enumerate(data[preamble_length:]):
        candidates = data[i:preamble_length + i]

        if not find_decomposition(n, candidates):
            return n


def find_subsequence(data, n):
    for i, a in enumerate(data):
        sum = a
        seq = [a]
        j = i + 1
        while True:
            if j >= len(data):
                break
            sum += data[j]
            seq.append(data[j])
            j += 1
            if sum == n:
                return seq
            if sum > n:
                break


def find_encryption_weakness(data, n=None):
    if not n:
        n = find_first(data)
    seq = find_subsequence(data, n)
    a = min(seq)
    b = max(seq)
    return a + b


if __name__ == '__main__':
    print('Day 9: Encoding Error')
    print('---------------------')

    with open('../res/day09.txt') as file:
        data = [int(line) for line in file.read().splitlines()]

    n = find_first(data)
    print(f'n = {n}')

    w = find_encryption_weakness(data, n)
    print(f'Encryption weakness: {w}')
