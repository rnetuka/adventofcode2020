from util import *


def next_operand(expression):
    if expression.startswith('('):
        operand = matching_parenthesis_substring(expression)
        return operand, expression[len(operand) + 1:]
    else:
        if ' ' in expression:
            i = expression.index(' ')
            operand = expression[:i]
            return operand, expression[i + 1:]
        else:
            operand = expression
            return operand, ''


def next_operation(expression):
    i = expression.index(' ')
    operation = expression[:i]
    return operation, expression[i + 1:]


class ExpressionEvaluator:

    def __init__(self):
        self.operator_priorities = {'+': 1, '*': 1}
        self.operations = {'+': lambda a, b: a + b,
                           '*': lambda a, b: a * b}

    @property
    def max_operation_priority(self):
        return max(self.operator_priorities.values())

    def evaluate_operand(self, operand):
        if isinstance(operand, int):
            return operand
        elif operand.startswith('('):
            e = ExpressionEvaluator()
            e.operator_priorities = self.operator_priorities
            return e.evaluate(operand[1:-1])
        elif isinstance(operand, str):
            return int(operand)

    # decompose an expression into a stack
    def decompose(self, expression, priority_level):
        stack = []
        while len(expression) > 0:
            if len(stack) == 0:
                a, expression = next_operand(expression)
                stack.append(a)
            else:
                a = stack.pop()
                operator, expression = next_operation(expression)
                b, expression = next_operand(expression)

                if self.operator_priorities[operator] == priority_level:
                    a = self.evaluate_operand(a)
                    b = self.evaluate_operand(b)
                    operation = self.operations[operator]
                    stack.append(operation(a, b))
                else:
                    stack.append(a)
                    stack.append(operator)
                    stack.append(b)

        return stack

    def evaluate(self, expression):
        priority_level = self.max_operation_priority
        stack = self.decompose(expression, priority_level)

        while priority_level >= 1:
            stack = self.evaluate_stack(stack, priority_level)
            priority_level -= 1

        return stack.pop()

    def evaluate_stack(self, stack, priority_level):
        if len(stack) == 1:
            return stack

        queue = []

        a = stack.pop()
        while len(stack) > 0:
            operator = stack.pop()
            b = stack.pop()

            if self.operator_priorities[operator] == priority_level:
                a = self.evaluate_operand(a)
                b = self.evaluate_operand(b)
                operation = self.operations[operator]
                result = operation(a, b)
                queue.append(result)
                a = result
            else:
                if len(queue) == 0:
                    queue.insert(0, a)
                queue.insert(0, operator)
                queue.insert(0, b)
                a = b

        return queue


def evaluate(expression, operator_priorities):
    evaluator = ExpressionEvaluator()
    evaluator.operator_priorities = operator_priorities
    return evaluator.evaluate(expression)


if __name__ == '__main__':
    with open('../res/day18.txt') as file:
        expressions = file.readlines()

    sum = 0
    for expression in expressions:
        sum += evaluate(expression, operator_priorities={'+': 1, '*': 1})
    print(sum)

    sum = 0
    for expression in expressions:
        sum += evaluate(expression, operator_priorities={'+': 2, '*': 1})
    print(sum)
