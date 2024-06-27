def arithmetic_arranger(problems, show_answers=False):
    expressions = []
    SPACING = '    '

    for problem in problems:
        if len(expressions) == 5:
            return 'Error: Too many problems.'
        first_space_index = problem.find(" ")
        expressions.append({
            'top': problem[:first_space_index],
            'bottom': problem[first_space_index+3:].strip(),
            'op': problem[first_space_index:first_space_index+3].strip()
        })

        if expressions[-1]['op'] not in ('+', '-'):
            return 'Error: Operator must be \'+\' or \'-\'.'
        elif not expressions[-1]['top'].isnumeric() or not expressions[-1]['bottom'].isnumeric():
            return 'Error: Numbers must only contain digits.'

    lines = ['', '', '']
    if show_answers == True:
        lines.append('')

    for index, expr in enumerate(expressions):
        if max(len(expr['top']), len(expr['bottom'])) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        expr['width'] = max(len(expr['top']), len(expr['bottom'])) + 2
        
        lines[0] += f'{expr["top"]:>{expr["width"]}}' \
        + (SPACING if index < len(expressions) - 1 else '')

        lines[1] += f'{expr["op"]}{expr["bottom"]:>{expr["width"]-1}}' \
        + (SPACING if index < len(expressions) - 1 else '')
        
        lines[2] += '-' * expr["width"] \
        + (SPACING if index < len(expressions) - 1 else '')

        if show_answers == True:
            result = calculate_result(expr)
            lines[3] += f'{str(result):>{expr["width"]}}' \
            + (SPACING if index < len(expressions) - 1 else '')

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


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
