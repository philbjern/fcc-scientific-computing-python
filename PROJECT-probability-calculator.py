import copy
import random

class Hat:
    contents = []

    def __init__(self, **vargs):
        for key, value in vargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, number):
        if number >= len(self.contents):
            return self.contents

        draw_balls = []
        contents_copy = copy.copy(self.contents)
        for i in range(number):
            rnd_ball = random.choice(contents_copy)
            draw_balls.append(rnd_ball)
            contents_copy.remove(rnd_ball)
        
        return draw_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for _ in range(num_experiments):
        draw = hat.draw(num_balls_drawn)    
        expected_balls_cpy = copy.copy(expected_balls)
        for ball in draw:
            if ball in expected_balls_cpy:
                if expected_balls_cpy[ball] > 0:
                    expected_balls_cpy[ball] -= 1

        if all(map(lambda x: x == 0, expected_balls_cpy.values())):
            num_success += 1

    return float(num_success / num_experiments)


if __name__ == '__main__':
    hat1 = Hat(yellow=3, blue=2, green=6)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    print(hat3.draw(3))

    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
                      expected_balls={'red':2,'green':1},
                      num_balls_drawn=5,
                      num_experiments=2000)

    print(probability)