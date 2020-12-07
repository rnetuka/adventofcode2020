def count_if(list, test):
    return sum(test(item) for item in list)
