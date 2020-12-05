# --- Day 5: Binary Boarding ---

max_row = 127
max_col = 7


def binary_half(interval, part):
    min, max = interval
    pivot = min + (max - min) // 2

    if part in ('F', 'L'):
        # return lower part of the interval
        return min, pivot

    elif part in ('B', 'R'):
        # return upper part of the interval
        return pivot + 1, max


def seat_position(description, max, min=0):
    for char in description:
        min, max = binary_half(interval=(min, max), part=char)

    assert min == max
    return min


def seat_location(description):
    row = seat_position(description[:7], max_row)
    col = seat_position(description[7:], max_col)
    return row, col


def seat_id(description):
    row, col = seat_location(description)
    return row * 8 + col


def find_my_seat(seat_ids):
    seat_ids = sorted(seat_ids)
    for i, current in enumerate(seat_ids):
        next = seat_ids[i + 1]
        if next != current + 1:
            return current + 1


if __name__ == '__main__':
    print('Day 5: Binary Boarding')
    print('----------------------')

    with open('../res/day05.txt') as file:
        descriptions = file.read().splitlines()

    seat_ids = [seat_id(description) for description in descriptions]
    print(f'Highest seat id: {max(seat_ids)}')

    print(f'My seat id is {find_my_seat(seat_ids)}')
