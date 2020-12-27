# --- Day 11: Seating System ---

from src.matrix import Matrix
import itertools


class Seats(Matrix):

    def __init__(self, width, height):
        super().__init__(width, height)

    def adjacent_occupied_seats(self, row, col) -> int:
        c = [coords for coords in itertools.product((-1, 0, 1), repeat=2)]
        c.remove((0, 0))
        result = 0
        for i, j in c:
            if 0 <= row + i < self.height and 0 <= col + j < self.width:
                if self[row + i][col + j] == '#':
                    result += 1
        return result

    def visible_occupied_seats(self, row, col) -> int:
        "Counts visible occupied seats from specified coordinates"
        def occupied_seat_in_direction(row, col, di=0, dj=0) -> bool:
            row += di
            col += dj
            while 0 <= row < self.height and 0 <= col < self.width:
                if self[row][col] == 'L':
                    return False
                if self[row][col] == '#':
                    return True
                row += di
                col += dj
            return False

        count = 0
        count += occupied_seat_in_direction(row, col, di=-1)
        count += occupied_seat_in_direction(row, col, di=1)
        count += occupied_seat_in_direction(row, col, dj=-1)
        count += occupied_seat_in_direction(row, col, dj=1)
        count += occupied_seat_in_direction(row, col, di=-1, dj=-1)
        count += occupied_seat_in_direction(row, col, di=-1, dj=1)
        count += occupied_seat_in_direction(row, col, di=1, dj=-1)
        count += occupied_seat_in_direction(row, col, di=1, dj=1)
        return count

    def __eq__(self, other):
        return repr(self) == repr(other)

    def occupied(self) -> int:
        count = 0
        for row in range(self.height):
            for col in range(self.width):
                if self[row][col] == '#':
                    count += 1
        return count


class SeatingSystem:

    def __init__(self, seats, strategy=Seats.adjacent_occupied_seats, treshold=4):
        self.seats = seats
        self.strategy = strategy
        self.treshold = treshold

    def __next__(self):
        result = Seats(self.seats.width, self.seats.height)
        for row in range(self.seats.height):
            for col in range(self.seats.width):
                seat = self.seats[row][col]
                if seat == 'L':
                    if self.strategy(self.seats, row, col) == 0:
                        result[row][col] = '#'
                    else:
                        result[row][col] = 'L'

                if seat == '#':
                    if self.strategy(self.seats, row, col) >= self.treshold:
                        result[row][col] = 'L'
                    else:
                        result[row][col] = '#'

                if seat == '.':
                    result[row][col] = '.'
        self.seats = result
        return result


if __name__ == '__main__':
    print('Day 11: Seating System')
    print('----------------------')

    with open('../res/day11.txt') as file:
        seats = Seats.parse(file.read().splitlines())

    system = SeatingSystem(seats)
    previous_state = seats
    while True:
        next_state = next(system)
        if next_state == previous_state:
            break
        else:
            previous_state = next_state
    print(system.seats.occupied())

    system = SeatingSystem(seats, strategy=Seats.visible_occupied_seats, treshold=5)
    previous_state = seats
    while True:
        next_state = next(system)
        if next_state == previous_state:
            break
        else:
            previous_state = next_state
    print(system.seats.occupied())
