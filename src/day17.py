class Cube:

    def __init__(self, x, y, z, w=None):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w is other.w

    def __hash__(self):
        return hash((self.x, self.y, self.z, self.w))

    def __repr__(self):
        return '(x={},y={},z={},w={})'.format(self.x, self.y, self.z, self.w)

    def neighbors(self):
        neighbors = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if self.w is not None:
                        for w in range(-1, 2):
                            if x != 0 or y != 0 or z != 0 or w != 0:
                                neighbors.append(Cube(self.x + x, self.y + y, self.z + z, self.w + w))
                    elif x != 0 or y != 0 or z != 0:
                        neighbors.append(Cube(self.x + x, self.y + y, self.z + z))
        return neighbors

    def is_neighbor_of(self, other):
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        dz = abs(self.z - other.z)
        dw = 0
        if self.w is not None:
            dw = abs(self.w - other.w)
        if dx + dy + dz + dw == 0:
            # not a neighbor of itself
            return False
        return dx <= 1 and dy <= 1 and dz <= 1 and dw <= 1


class PocketDimension:

    def __init__(self):
        self.active_cubes = []
        self.w_coordinates = False

    @staticmethod
    def from_file(path):
        with open(path) as file:
            dimension = PocketDimension()
            for y, line in enumerate(file.read().splitlines()):
                for x, contents in enumerate(line):
                    if contents == '#':
                        dimension.active_cubes.append(Cube(x, y, 0))
            return dimension

    @staticmethod
    def four_dimensional_from_file(path):
        with open(path) as file:
            dimension = PocketDimension()
            dimension.w_coordinates = True
            for y, line in enumerate(file.read().splitlines()):
                for x, contents in enumerate(line):
                    if contents == '#':
                        dimension.active_cubes.append(Cube(x, y, 0, 0))
            return dimension

    def inactive_cubes(self):
        # tweak: only consider neighbors of an active cube, because there will be a check for 3 active neighbors later
        inactiv_cubes = set()
        for cube in self.active_cubes:
            for neighbor in cube.neighbors():
                if neighbor not in self.active_cubes:
                    inactiv_cubes.add(neighbor)
        return inactiv_cubes

    def active_neighbors_of(self, cube):
        return [other for other in self.active_cubes if other.is_neighbor_of(cube)]

    def do_step(self):
        next_generation = []
        for cube in self.active_cubes:
            active_neighbors = len(self.active_neighbors_of(cube))
            if active_neighbors == 2 or active_neighbors == 3:
                next_generation.append(cube)
        for cube in self.inactive_cubes():
            active_neighbors = len(self.active_neighbors_of(cube))
            if active_neighbors == 3:
                next_generation.append(cube)
        self.active_cubes = next_generation


def solution_1():
    dimension = PocketDimension.from_file('../res/day17.txt')
    for step in range(6):
        dimension.do_step()
    return len(dimension.active_cubes)


def solution_2():
    dimension = PocketDimension.four_dimensional_from_file('../res/example17.txt')
    for step in range(6):
        dimension.do_step()
    return len(dimension.active_cubes)


if __name__ == '__main__':
    print('Day 14: Docking Data')
    print('--------------------')
    #print(solution_1())
    print(solution_2())
