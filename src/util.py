
def count_if(list, test):
    return sum(test(item) for item in list)


def matching_parenthesis_substring(string):
    if string[0] != '(':
        raise ValueError()
    c = 0
    for i in range(len(string)):
        if string[i] == '(':
            c += 1
        elif string[i] == ')':
            c -= 1
        if c == 0:
            return string[:i+1]
    raise ValueError()
