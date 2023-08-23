# --- Day 6: Custom Customs ---

def answers(person):
    return set(answer for answer in person)


def anyone_yes(group):
    s = set()
    for person in group:
        s.update(answers(person))
    return len(s)


def everyone_yes(group):
    s = set(answers(group[0]))
    for person in group[1:]:
        s = s.intersection(answers(person))
    return len(s)


def read_groups():
    groups = []
    with open('../res/day06.txt') as file:
        lines = file.read().splitlines()
        lines.append('')  # add last empty line
        group = []
        for line in lines:
            if line:
                group.append(line)
            else:
                groups.append(group)
                group = []
    return groups


if __name__ == '__main__':
    print('Day 6: Custom Customs')
    print('---------------------')

    count_a = 0
    count_b = 0

    for group in read_groups():
        count_a += anyone_yes(group)
        count_b += everyone_yes(group)

    print(f'Sum (anyone): {count_a}')
    print(f'Sum (everyone): {count_b}')
