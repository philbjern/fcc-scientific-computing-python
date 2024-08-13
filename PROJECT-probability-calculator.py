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
        # not enought balls ever
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