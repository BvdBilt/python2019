import math

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceFromPoint(self, point):
        dx = (point.getX() - self.x)
        dy = (point.getY() - self.y)
        return math.sqrt(dy ** 2 + dx ** 2)

    def reflect_x(self):
        reflect = self.x -self.x *2
        return reflect, self.y

Point(20, 5).reflect_x()