import re
from template import FieldTemplate, FieldTemplates


class Ticket:

    def __init__(self):
        self.fields = {}

    @staticmethod
    def merge(fields, values):
        ticket = Ticket()
        for i in range(len(fields)):
            field = fields[i]
            value = values[i]
            ticket.fields[field] = value
        return ticket


class Puzzle:

    def __init__(self):
        self.field_templates = FieldTemplates()
        self.my_ticket_values = None
        self.my_ticket = None
        self.nearby_ticket_values = []

    @staticmethod
    def from_file(path):
        puzzle = Puzzle()
        with open(path) as file:
            lines = file.read().splitlines()
            parsing_my_ticket = False
            parsing_nearby_tickets = False

            for line in lines:
                if 'or' in line:
                    field_name = line[:line.index(':')]
                    numbers = re.findall('[0-9]+', line)
                    template = FieldTemplate()
                    template.lower_min = int(numbers[0])
                    template.lower_max = int(numbers[1])
                    template.upper_min = int(numbers[2])
                    template.upper_max = int(numbers[3])
                    puzzle.field_templates[field_name] = template
                elif line == 'your ticket:':
                    parsing_my_ticket = True
                elif line == 'nearby tickets:':
                    parsing_my_ticket = False
                    parsing_nearby_tickets = True
                elif line.strip() != '':
                    if parsing_my_ticket:
                        puzzle.my_ticket_values = get_numbers(line)
                    elif parsing_nearby_tickets:
                        puzzle.nearby_ticket_values.append(get_numbers(line))
        return puzzle

    @property
    def ticket_values(self):
        return [self.my_ticket_values] + self.nearby_ticket_values

    def field_values(self, i):
        values = []
        for ticket_values in self.ticket_values:
            values.append(ticket_values[i])
        return values

    def validate(self, ticket_values):
        for number in ticket_values:
            if not self.field_templates.validate(number):
                return False
        return True

    def remove_invalid_tickets(self):
        valid_ticket_values = []
        for ticket_values in self.nearby_ticket_values:
            if self.validate(ticket_values):
                valid_ticket_values.append(ticket_values)
        self.nearby_ticket_values = valid_ticket_values


def get_numbers(line):
    return [int(n) for n in line.split(',')]




def first_resolvable(field_candidates):
    for i in range(len(field_candidates)):
        if len(field_candidates[i]) == 1:
            return i

def resolve_field(field_candidates, i, field):
    for j in range(len(field_candidates)):
        if i != j and field in field_candidates[j]:
            field_candidates[j].remove(field)
    field_candidates[i] = []
    return field_candidates

if __name__ == '__main__':
    print('Day 16: Ticket Translation')
    print('-----------------')

    puzzle = Puzzle.from_file('../res/day16.txt')
    ticket_scanning_error_rate = 0

    for ticket_values in puzzle.nearby_ticket_values:
        for number in ticket_values:
            if not puzzle.field_templates.validate(number):
                ticket_scanning_error_rate += number

    print('Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?')
    print(ticket_scanning_error_rate)
    print()

    puzzle.remove_invalid_tickets()

    field_count = len(puzzle.field_templates.field_names())
    field_candidates = []
    fields = [None] * field_count

    for i in range(field_count):
        values = puzzle.field_values(i)
        field_candidates.append(puzzle.field_templates.match(values))

    while True:
        i = first_resolvable(field_candidates)
        if i is None:
            break
        field = field_candidates[i][0]
        fields[i] = field
        field_candidates = resolve_field(field_candidates, i, field)

    puzzle.my_ticket = Ticket.merge(fields, puzzle.my_ticket_values)

    c = 1
    for field, value in puzzle.my_ticket.fields.items():
        if field.startswith('departure'):
            c *= value

    print('What do you get if you multiply those six values together?')
    print(c)
