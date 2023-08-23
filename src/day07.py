# --- Day 7: Handy Haversacks ---

class Rules:

    def __init__(self):
        self.dict = {}

    @staticmethod
    def parse(input):
        rules = Rules()
        for line in input.splitlines():
            words = (word for word in line.split())
            a = next(words) + ' ' + next(words)
            rules.dict[a] = []
            assert next(words) == 'bags'
            assert next(words) == 'contain'
            while (word := next(words)) not in ('bag.', 'bags.'):
                if word.isnumeric():
                    n = int(word)
                    b = next(words) + ' ' + next(words)
                    rules.dict[a].append((n, b))
        return rules

    def direct_predecessors_of(self, bag):
        result = []
        for a, contents in self.dict.items():
            for n, b in contents:
                if b == bag:
                    result.append(a)
        return result

    def count_predecessors_of(self, bag):
        result = set(self.direct_predecessors_of(bag))
        queue = list(result)
        while queue:
            a = queue.pop(0)
            result.add(a)
            queue.extend(self.direct_predecessors_of(a))
        return len(result)

    def contents_of(self, bag):
        return self.dict[bag]

    def count_total_contents_of(self, bag):
        queue = list(self.contents_of(bag))
        count = 0
        while queue:
            n, b = queue.pop(0)
            count += n
            for m, c in self.contents_of(b):
                queue.append((n * m, c))
        return count


if __name__ == '__main__':
    print('Day 7: Handy Haversacks')
    print('-----------------------')

    with open('../res/day07.txt') as file:
        input = file.read()

    rules = Rules.parse(input)
    bag = 'shiny gold'

    count = rules.count_predecessors_of(bag)
    print(f'{count} bags can eventually contain {bag} bag')

    count = rules.count_total_contents_of(bag)
    print(f'{count} bags are required inside {bag} bag')
