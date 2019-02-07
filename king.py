

import collections


X0 = 0.5
X1 = 0.3
X_1 = 0.2
Y0 = 0.4
Y1 = 0.4
Y_1 = 0.2

Coordinates = collections.namedtuple('Coordinates', ['x', 'y'])


class Position:
    def __init__(self, x=0, y=0, chance=1):
        self._coordinates = Coordinates(x, y)
        self._chance = chance

    def __eq__(self, other):
        if self.__repr__() == other.__repr__():
            return True
        else:
            return False

    def __getattr__(self, item):
        if item == 'chance':
            return self._chance
        elif item == 'x':
            return self._coordinates.x
        elif item == 'y':
            return self._coordinates.y
        else:
            raise AttributeError(item)

    def __repr__(self):
        return self._coordinates.__repr__()

    def __str__(self):
        return 'Position x: {0:>2}, y: {1:>2}, chance: {2:.10f} %'.format(self.x, self.y, self.chance*100)

    def __add__(self, other):
        chance = self.chance + other.chance
        return Position(self.x, self.y, chance)

    def __hash__(self):
        return hash(self._coordinates)

    def __mul__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        chance = self.chance * other.chance
        return Position(x, y, chance)


def adder(positions, new):
    if new in positions:
        index = positions.index(new)
        new = positions[index] + new
        del positions[index]
    positions.append(new)
    return positions


def get_choices():
    if X_1 + X0 + X1 == 1.0 and Y_1 + Y0 + Y1 == 1.0:
        x_chance = X0, X1, X_1
        y_chance = Y0, Y1, Y_1
        values = [-1, 0, 1]
        choices = []
        for x in values:
            for y in values:
                current = Position(x, y, x_chance[x] * y_chance[y])
                choices = adder(choices, current)
        return choices
    else:
        raise ValueError('Sum of chances != 1')


def step(positions):
    choices = get_choices()
    new = []
    for pos in positions:
        for choice in choices:
            current = pos * choice
            new = adder(new, current)
    return new


def walker(steps=1, x=0, y=0):
    new = []
    while steps:
        steps = steps - 1
        if not new:
            new = [Position(x, y)]
        new = step(new)
    return new


def manager(steps=1, tracked=None):
    result = walker(steps)
    if tracked:
        index = result.index(tracked)
        return str(result[index])
    else:
        return '\n'.join(str(s) for s in result)


def answer(all=False):
    if all:
        return manager(steps=5)
    else:
        tracked = Position(0, 0)
        return manager(steps=5, tracked=tracked)


if __name__ == '__main__':
    print(answer(True))
    print('-'*40)
    print(len(walker(5)))
    print('-' * 40)
    print(answer())
