from test_framework import generic_test


def evaluate(expression: str) -> int:

    resultados = []

    for element in expression.split(","):
        if element == '*':
            resultados.append(resultados.pop() * resultados.pop())

        elif element == '/':
            resultados.append(resultados.pop(-2) // resultados.pop())

        elif element == '+':
            resultados.append(resultados.pop() + resultados.pop())

        elif element == '-':
            resultados.append(resultados.pop(-2) - resultados.pop())
        else:
            resultados.append(int(element))

    return resultados[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
