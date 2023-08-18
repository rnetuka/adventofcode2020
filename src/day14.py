# --- Day 14: Docking Data ---
test_input = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
'''

def parse_mask(instruction):
    return instruction[instruction.index('=') + 2:]


def parse_write_instruction(instruction):
    address = int(instruction[instruction.index('[') + 1:instruction.index(']')])
    value = int(instruction[instruction.index('=') + 2:])
    return address, value


def set_bit(n, i, bit):
    return n | (1 << i) if bit else n & ~(1 << i)


def mask(value, bitmask):
    for i, bit in enumerate(reversed(bitmask)):
        if bit == '0' or bit == '1':
            value = set_bit(value, i, int(bit))
    return value


def mask_v2(address, bitmask):
    address = f'{address:036b}'
    result = ''
    for i, bit in enumerate(bitmask):
        if bit == '0':
            result += address[i]
        else:
            result += bit
    return result


def fill_floating_bits(address):
    if 'X' not in address:
        return [address]
    else:
        i = address.index('X')
        result = []
        result += fill_floating_bits(address[:i] + '0' + address[i+1:])
        result += fill_floating_bits(address[:i] + '1' + address[i+1:])
        return result


if __name__ == '__main__':
    print('Day 14: Docking Data')
    print('--------------------')

    with open('../res/day14.txt') as file:
        instructions = file.read().splitlines()

    memory = {}

    for instruction in instructions:
        if instruction.startswith('mask'):
            bitmask = parse_mask(instruction)
        if instruction.startswith('mem'):
            address, value = parse_write_instruction(instruction)
            memory[address] = mask(value, bitmask)

    print(f'Sum of all memory values: {sum(memory.values())}')

    memory = {}

    for instruction in instructions:
        if instruction.startswith('mask'):
            bitmask = parse_mask(instruction)
        if instruction.startswith('mem'):
            address, value = parse_write_instruction(instruction)
            address = mask_v2(address, bitmask)

            addresses = fill_floating_bits(address)
            for address in addresses:
                memory[int(address, 2)] = value

    print(f'Sum of all memory values: {sum(memory.values())}')