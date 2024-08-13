# Scientific computing with python
All solutions to `scientific computing with python` certification course on fcc

## PROJECT-probability-calculator.py
```
import copy
import random

# random.seed(95)

class Hat:
    def __init__(self, **kwargs):
        print(kwargs)
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
            
        self.orig_contents = []
        self.orig_contents = copy.deepcopy(self.contents)
        print(self.contents)

    def __str__(self):
        return 'hat=[' + ', '.join(self.orig_contents) + ']'

    def draw(self, number):
        # not enough balls ever
        if number > len(self.orig_contents):
            draw = self.orig_contents
            self.contents = []
            return draw

        # enough balls but need to reset
        if number >= len(self.contents):
            draw_balls = self.contents
            self.reset_balls()         
        else:
            draw_balls = []

        # pick random balls
        for _ in range(number):
            ball_choice = random.choice(self.contents)
            draw_balls.append(ball_choice)
            self.contents.remove(ball_choice)

        return draw_balls

    def reset_balls(self):
        print('resetting balls')
        self.contents.clear()
        self.contents = copy.copy(self.orig_contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    orig_balls = copy.deepcopy(hat.contents)
    for _ in range(num_experiments):
        draw = hat.draw(num_balls_drawn)    
        print(f'{_ + 1}nth draw = {draw}')
        expected_balls_cpy = copy.deepcopy(expected_balls)
        for ball in draw:
            if ball in expected_balls_cpy:
                if expected_balls_cpy[ball] > 0:
                    expected_balls_cpy[ball] -= 1
        
        if all(map(lambda x: x == 0, expected_balls_cpy.values())):
            print('-->!successful draw')
            num_success += 1

    print(num_success / num_experiments, num_success, num_experiments, num_balls_drawn, expected_balls, hat)
    return float(num_success / num_experiments)

# hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
# print(hat3.draw(3))

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print('Probability=', probability)
```


## PROJECT-arithmetic-formatter.py
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
