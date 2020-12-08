# --- Day 8: Handheld Halting ---


def read_instructions(text):
    instructions = []
    for instruction in text.splitlines():
        operation, argument = instruction.split()
        instructions.append((operation, int(argument)))
    return instructions


class ForceHaltError(RuntimeError):

    def __init__(self, message):
        super().__init__(message)


class HandheldConsole:

    def __init__(self):
        self.accumulator = 0

    def run(self, instructions):
        line = 0
        visited_lines = set()

        while line < len(instructions):
            if line in visited_lines:
                raise ForceHaltError('Infinite loop detected! Force halt')

            visited_lines.add(line)
            operation, argument = instructions[line]

            if operation == 'jmp':
                line += argument
                continue

            if operation == 'acc':
                self.accumulator += argument

            line += 1


def repaired(code):
    def needs_repair(operation):
        return operation in ('jmp', 'nop')

    def repair(operation, argument):
        return ('jmp', argument) if operation == 'nop' else ('nop', argument)

    # make a copy of the source code in order not to modify the original
    code = list(code)

    for line, instruction in enumerate(code):
        operation, argument = instruction
        if needs_repair(operation):
            code[line] = repair(operation, argument)
            try:
                console = HandheldConsole()
                console.run(code)
            except ForceHaltError:
                # revert to original instruction
                code[line] = (operation, argument)
            else:
                return code


if __name__ == '__main__':
    print('Day 8: Handheld Halting')
    print('-----------------------')

    with open('../res/day08.txt') as file:
        code = read_instructions(file.read())

    try:
        console = HandheldConsole()
        console.run(code)
    except ForceHaltError:
        print(f'Accumulator value before force halt: {console.accumulator}')

    code = repaired(code)
    console = HandheldConsole()
    console.run(code)
    print(f'Accumulator value after program termination: {console.accumulator}')
