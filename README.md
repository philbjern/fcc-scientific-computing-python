# Scientific computing with python
All solutions to `scientific computing with python` certification course on fcc

## arithmetic-formatter.py
```
def arithmetic_arranger(problems, show_answers=False):
    SPACING = '    '
    OPERATOR_OFFSET = 2
    OPERATOR_INPUT_OFFSET = 3
    MAX_INPUT_DIGITS = 4
    MAX_PROBLEMS_AMOUNT = 5

    # Expressions validation and parsing
    expressions = []

    for problem in problems:
        if len(expressions) == MAX_PROBLEMS_AMOUNT:
            return 'Error: Too many problems.'
        first_space_index = problem.find(" ")
        expressions.append({
            'top': problem[:first_space_index],
            'bottom': problem[first_space_index+OPERATOR_INPUT_OFFSET:].strip(),
            'op': problem[first_space_index:first_space_index+OPERATOR_INPUT_OFFSET].strip()
        })

        if expressions[-1]['op'] not in ('+', '-'):
            return 'Error: Operator must be \'+\' or \'-\'.'
        elif not expressions[-1]['top'].isnumeric() or not expressions[-1]['bottom'].isnumeric():
            return 'Error: Numbers must only contain digits.'

    LAST_INDEX = len(expressions) - 1

    lines = ['', '', '']
    if show_answers == True:
        lines.append('')

    # Create output lines
    for index, expr in enumerate(expressions):
        if max(len(expr['top']), len(expr['bottom'])) > MAX_INPUT_DIGITS:
            return 'Error: Numbers cannot be more than four digits.'

        expr['width'] = max(len(expr['top']), len(expr['bottom'])) + OPERATOR_OFFSET
        
        lines[0] += f'{expr["top"]:>{expr["width"]}}' \
        + (SPACING if index < LAST_INDEX else '')

        lines[1] += f'{expr["op"]}{expr["bottom"]:>{expr["width"]-1}}' \
        + (SPACING if index < LAST_INDEX else '')
        
        lines[2] += '-' * expr["width"] \
        + (SPACING if index < LAST_INDEX else '')

        if show_answers == True:
            result = calculate_result(expr)
            lines[3] += f'{str(result):>{expr["width"]}}' \
            + (SPACING if index < LAST_INDEX else '')

    return "\n".join(lines).strip('\n')


def calculate_result(expression):
    first = int(expression['top'])
    second = int(expression['bottom'])
    op = expression['op']
    
    if op == '+':
        return first + second
    elif op == '-':
        return first - second
    else:
        return None

# Tests
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
```
