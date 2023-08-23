from util import *


class ExpressionEvaluator:

    def __init__(self, expression):
        self.expression = expression
        self.stack = []
        self.operator_priorities = {'+': 1, '*': 1}
        self.operations = {'+': lambda a, b: a + b,
                           '*': lambda a, b: a * b}

    def read_operand(self):
        if self.expression.startswith('('):
            operand = matching_parenthesis_substring(self.expression)
            self.expression = self.expression[len(operand)+1:]
            return operand
        else:
            if ' ' in self.expression:
                i = self.expression.index(' ')
                operand = self.expression[:i]
                self.expression = self.expression[i+1:]
                return operand
            else:
                operand = self.expression
                self.expression = ''
                return operand

    def read_operation(self):
        i = self.expression.index(' ')
        operation = self.expression[:i]
        self.expression = self.expression[i + 1:]
        return operation

    def evaluate_operand(self, operand):
        if isinstance(operand, int):
            return operand
        elif operand.startswith('('):
            e = ExpressionEvaluator(operand[1:-1])
            e.operator_priorities = self.operator_priorities
            return e.evaluate()
        else:
            return int(operand)

    def evaluate(self):
        priority_level = max(self.operator_priorities.values())
        while len(self.expression) > 0:
            if len(self.stack) == 0:
                a = self.read_operand()
                self.stack.append(a)
            else:
                a = self.stack.pop()
                operator = self.read_operation()
                b = self.read_operand()

                if self.operator_priorities[operator] == priority_level:
                    a = self.evaluate_operand(a)
                    b = self.evaluate_operand(b)
                    operation = self.operations[operator]
                    self.stack.append(operation(a, b))
                else:
                    self.stack.append(a)
                    self.stack.append(operator)
                    self.stack.append(b)

        while len(self.stack) > 1:
            a = self.evaluate_operand(self.stack.pop())
            operator = self.stack.pop()
            b = self.evaluate_operand(self.stack.pop())
            operation = self.operations[operator]
            self.stack.append(operation(a, b))

        return self.stack.pop()


def evaluate(expression, consider_operator_priorities=False):
    evaluator = ExpressionEvaluator(expression)
    if consider_operator_priorities:
        evaluator.operator_priorities = {'+': 2, '*': 1}
    return evaluator.evaluate()


if __name__ == '__main__':
    with open('../res/day18.txt') as file:
        sum = 0
        for line in file.readlines():
            pass
            sum += evaluate(line)
        print(sum)

    with open('../res/day18.txt') as file:
        sum = 0
        for line in file.readlines():
            pass
            sum += evaluate(line, consider_operator_priorities=True)
        print(sum)
