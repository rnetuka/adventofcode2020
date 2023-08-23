class Row:

    def __init__(self, data):
        self.data = data

    def __setitem__(self, col, value):
        self.data[col] = value

    def __getitem__(self, col):
        return self.data[col]


class Matrix:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[0] * width for _ in range(height)]

    @classmethod
    def parse(cls, input):
        lines = [line.rstrip() for line in input if line]
        width = len(lines[0])
        height = len(lines)
        result = cls(width, height)
        for row in range(height):
            for col in range(width):
                result[row][col] = lines[row][col]
        return result

    @classmethod
    def from_file(cls, path):
        with open(path) as file:
            return cls.parse(file.readlines())

    def row_coords(self, i):
        return [(i, j) for j in range(0, self.width)]

    def column_coords(self, j):
        return [(i, j) for i in range(0, self.height)]

    def __getitem__(self, row):
        return Row(self.data[row])

    def __iter__(self):
        return MatrixIterator(self)

    def __repr__(self):
        repr = ''
        for row in range(self.height):
            repr += ''.join(self[row])
            repr += '\n'
        return repr


class MatrixIterator:

    def __init__(self, matrix):
        self.matrix = matrix
        self.row = 0
        self.col = 0

    def __next__(self):
        item = self.matrix[self.row][self.col]
        self.col += 1
        if self.col >= self.matrix.width:
            self.row += 1
            self.col = 0
        if self.row >= self.matrix.height:
            raise StopIteration
        return item
