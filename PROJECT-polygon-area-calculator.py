class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        cls_name = self.__class__.__name__
        args = ', '.join(arg_list)
        return f'{cls_name}({args})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        pic = ''
        for y in range(self.height):
            pic += '*' * self.width + '\n'
        return pic

    def get_amount_inside(self, shape):
        hor_times = self.width // shape.width
        vert_times = self.height // shape.height
        return hor_times * vert_times


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def __repr__(self):
        return f'Square(side={self.side})'

    def set_side(self, side):
        self.side = side

    def set_width(self, width):
        self.width = width
        self.side = width

    def set_height(self, height):
        self.height = height
        self.side = height

    def get_picture(self):
        self.set_width(self.side)
        self.set_height(self.side)
        print('Square, ', self.width, self.height)
        return super().get_picture()


if __name__ == "__main__":
    r1 = Rectangle(3, 6)
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
    print(Rectangle(15,10).get_amount_inside(Square(5)))