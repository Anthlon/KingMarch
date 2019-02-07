

X0 = 0.5
X1 = 0.3
X_1 = 0.2
Y0 = 0.4
Y1 = 0.4
Y_1 = 0.2


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Position({0}, {1})'.format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Position(x, y)

    def __hash__(self):
        return hash('x: {0}, y: {1}'.format(self.x, self.y))


def start(x=0, y=0):
    return {Position(x, y): 1}


def get_choices():
    if X_1 + X0 + X1 == 1.0 and Y_1 + Y0 + Y1 == 1.0:
        x_chance = X0, X1, X_1
        y_chance = Y0, Y1, Y_1
        value = [-1, 0, 1]
        return {Position(x, y): x_chance[x] * y_chance[y] for x in value for y in value}
    else:
        raise ValueError


def step(position):
    choices = get_choices()
    new = {}
    for pos in position.keys():
        for choice in choices.keys():
            s = pos + choice
            if s in new.keys():
                new[pos] = new[pos] + (position[pos] * choices[choice])
            else:
                new[pos] = position[pos] * choices[choice]
    return new


def walker(steps=1, x=0, y=0):
    new = {}
    while steps:
        steps = steps - 1
        if not new:
            new = start(x, y)
        new = step(new)
    return new

