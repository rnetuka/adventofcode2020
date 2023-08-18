class Numbers:

    def __init__(self, list):
        self.turn = len(list)
        self.last = {}
        self.previously = {}
        self.n = list[-1]
        for i, n in enumerate(list):
            self.last[n] = i + 1

    def last_spoken(self):
        return self.n

    def previously_spoken(self, n):
        return self.previously[n]

    def has_been_spoken_once(self, n):
        return n not in self.previously

    def speak(self, n):
        if n in self.last:
            self.previously[n] = self.last[n]
        self.last[n] = self.turn
        self.n = n


if __name__ == '__main__':
    numbers = Numbers([2, 0, 6, 12, 1, 3])
    for _ in range(30_000_000 - numbers.turn):
        numbers.turn += 1
        n = numbers.last_spoken()
        if numbers.has_been_spoken_once(n):
            numbers.speak(0)
        else:
            i = numbers.previously_spoken(n)
            j = numbers.turn - 1
            m = j - i
            numbers.speak(m)

        if numbers.turn == 2020:
            print(numbers.last_spoken())

    print(numbers.last_spoken())
