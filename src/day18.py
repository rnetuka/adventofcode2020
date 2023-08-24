from util import *


class ExpressionEvaluator:

    def __init__(self):
        self.operator_priorities = {'+': 1, '*': 1}
        self.operations = {'+': lambda a, b: a + b,
                           '*': lambda a, b: a * b}

    @property
    def max_operation_priority(self):
        return max(self.operator_priorities.values())

    def next_operand(self, expression):
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

    def next_operation(self, expression):
        i = expression.index(' ')
        operation = expression[:i]
        return operation, expression[i + 1:]

    # decompose an expression into a queue
    def decompose(self, expression):
        queue = []
        a, expression = self.next_operand(expression)
        queue.append(a)
        while len(expression) > 0:
            operator, expression = self.next_operation(expression)
            b, expression = self.next_operand(expression)
            queue.append(operator)
            queue.append(b)
        return queue

    def evaluate_operand(self, operand):
        if isinstance(operand, int):
            # operand has been already converted to int
            return operand
        elif operand.startswith('('):
            # operand is a sub-expression, evaluate it recursively
            sub_expression = operand[1:-1]
            return self.evaluate(sub_expression)
        else:
            # operand is a string representing a number
            return int(operand)

    def evaluate(self, expression):
        queue = self.decompose(expression)

        for priority_level in range(self.max_operation_priority, 0, -1):
            queue = self.evaluate_queue(queue, priority_level)

        # right now, the queue should have only one element, the result of all applied operations
        return queue.pop()

    def evaluate_queue(self, queue, priority_level):
        if len(queue) == 1:
            # the queue contains the result and no other operations
            return queue

        # already move the first-most operand to the new queue
        result = [queue.pop(0)]

        # process the other operands and operations
        while len(queue) > 0:
            operator = queue.pop(0)
            b = queue.pop(0)

            if self.operator_priorities[operator] == priority_level:
                a = result.pop()
                a = self.evaluate_operand(a)
                b = self.evaluate_operand(b)
                operation = self.operations[operator]
                result.append(operation(a, b))
            else:
                result.append(operator)
                result.append(b)

        return result


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
