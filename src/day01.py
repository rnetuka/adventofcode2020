# --- Day 1: Report Repair ---

def find_two_entries(expense_report, sum=2020):
    for a in expense_report:
        b = sum - a
        if b in expense_report:
            return a, b


def find_three_entries(expense_report):
    for a in expense_report:
        if result := find_two_entries(expense_report, 2020 - a):
            b, c = result
            return a, b, c


if __name__ == '__main__':
    with open('../res/day01.txt') as file:
        expense_report = [int(line) for line in file.readlines()]

    print('Day 1: Report Repair')
    print('--------------------')

    a, b = find_two_entries(expense_report)
    print(f'{a} * {b} = {a * b}')

    a, b, c = find_three_entries(expense_report)
    print(f'{a} * {b} * {c} = {a * b * c}')
