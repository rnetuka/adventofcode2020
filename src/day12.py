# --- Day 12: Rain Risk ---

from src.geom import Point, vector


class Ship:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.orientation = 'E'
        self.waypoint = Point(x=10, y=1)

    @property
    def position(self):
        return Point(self.x, self.y)

    @position.setter
    def position(self, point):
        self.x = point.x
        self.y = point.y

    @property
    def distance(self):
        return abs(ship.x) + abs(ship.y)

    def turn(self, direction, times=1):
        order = ['N', 'E', 'S', 'W']
        for _ in range(times):
            next = order[(order.index(self.orientation) + direction) % len(order)]
            self.orientation = next

    def simple_action(self, action, value):
        if action == 'N':
            self.y += value
        if action == 'S':
            self.y -= value
        if action == 'E':
            self.x += value
        if action == 'W':
            self.x -= value
        if action == 'F':
            self.simple_action(self.orientation, value)
        if action == 'R':
            self.turn(+1, value // 90)
        if action == 'L':
            self.turn(-1, value // 90)

    def waypoint_action(self, action, value):
        if action == 'N':
            self.waypoint.y += value
        if action == 'S':
            self.waypoint.y -= value
        if action == 'E':
            self.waypoint.x += value
        if action == 'W':
            self.waypoint.x -= value
        if action == 'F':
            for _ in range(value):
                v = vector(self.position, self.waypoint)
                self.position += v
                self.waypoint += v
        if action == 'R':
            self.waypoint.rotate(value, s=self.position)
        if action == 'L':
            self.waypoint.rotate(-value, s=self.position)


def parse(instruction):
    action = instruction[:1]
    value = int(instruction[1:])
    return action, value


if __name__ == '__main__':
    print('Day 12: Rain Risk')
    print('-----------------')

    with open('../res/day12.txt') as file:
        instructions = [parse(line) for line in file.read().splitlines()]

    ship = Ship()
    for action, value in instructions:
        ship.simple_action(action, value)

    print(f'{ship.distance}')

    ship = Ship()
    for action, value in instructions:
        ship.waypoint_action(action, value)

    print(f'{ship.distance}')
