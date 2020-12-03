# --- Day 3: Toboggan Trajectory ---

from src.matrix import Matrix


class Toboggan(Matrix):

    def is_tree(self, row, col):
        return self[row][col] == '#'

    def encountered_trees(self, start=(0, 0), slope=(3, 1)):
        row, col = start
        dx, dy = slope
        count = 0
        while not row >= self.height:
            if self.is_tree(row, col):
                count += 1

            col += dx
            row += dy
            if col >= self.width:
                col = col % self.width

        return count


if __name__ == '__main__':
    print('Day 3: Toboggan Trajectory')
    print('--------------------------')

    toboggan = Toboggan.from_file('../res/day03.txt')

    print(f'Trees encountered: {toboggan.encountered_trees()}')

    a = toboggan.encountered_trees(slope=(1, 1))
    b = toboggan.encountered_trees(slope=(3, 1))
    c = toboggan.encountered_trees(slope=(5, 1))
    d = toboggan.encountered_trees(slope=(7, 1))
    e = toboggan.encountered_trees(slope=(1, 2))
    print(f'Multiplied together: {a * b * c * d * e}')
