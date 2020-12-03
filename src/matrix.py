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

    def __getitem__(self, row):
        return Row(self.data[row])
