import copy

rules = {}


class Sequence:

    def __init__(self):
        self.elements = [0]

    def __repr__(self):
        chars = [str(element) for element in self.elements]
        return ''.join(chars)

    def first_expandable_i(self):
        for i, element in enumerate(self.elements):
            if element != 'a' and element != 'b':
                return i

    def replace(self, i, content):
        if isinstance(content, str):
            self.elements[i] = content
        if isinstance(content, tuple):
            self.elements = self.elements[:i] + list(content) + self.elements[i+1:]

    def potential_match(self, string):
        if len(self.elements) > len(string):
            return False
        for i, element in enumerate(self.elements):
            if element != 'a' and element != 'b':
                break
            if string[i] != self.elements[i]:
                return False
        return True


def matches(string):
    queue = [Sequence()]
    while len(queue) > 0:
        sequence = queue.pop(0)
        if str(sequence) == string:
            return True
        queue += expand(sequence, string)
    return False

def expand(sequence, string):
    i = sequence.first_expandable_i()
    if i is None:
        return []
    else:
        left = sequence.elements[i]
        right = rules[left]
        if isinstance(right, tuple):
            sequence = copy.deepcopy(sequence)
            sequence.replace(i, right)
            return [sequence] if sequence.potential_match(string) else []
        if isinstance(right, list):
            result = []
            for alternative in right:
                seq = copy.deepcopy(sequence)
                seq.replace(i, alternative)
                if seq.potential_match(string):
                    result.append(seq)
            return result
        if isinstance(right, str):
            sequence = copy.deepcopy(sequence)
            sequence.replace(i, right)
            return [sequence] if sequence.potential_match(string) else []


if __name__ == '__main__':
    messages = []

    with open('../res/day19.txt') as file:
        for line in file.readlines():
            line = line.strip()
            if ':' in line:
                # parsing rule
                i = line.index(':')
                left = int(line[:i])
                right = line[i+1:].strip()
                if right == '"a"' or right == '"b"':
                    rules[left] = right[1:-1]
                elif '|' in right:
                    rules[left] = []
                    parts = right.split('|')
                    for part in parts:
                        part = tuple([int(char) for char in part.strip().split(' ')])
                        rules[left].append(part)
                else:
                    right = tuple([int(char) for char in right.split(' ')])
                    rules[left] = right

            elif len(line.strip()) > 0:
                messages.append(line.strip())

    c = 0
    for message in messages:
        if matches(message):
            c += 1
    print(c)

    rules[8] = [(42,), (42, 8)]
    rules[11] = [(42, 31), (42, 11, 31)]

    c = 0
    for message in messages:
        if matches(message):
            c += 1
    print(c)
