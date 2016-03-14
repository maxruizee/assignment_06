'''
Created on Mar 6, 2016

@author: Max Ruiz
'''


class Point(object):

    def __init__(self, x, y, **mark):
        self.x = x
        self.y = y
        self.mark = mark

    def check_coincident(self, point):
        return (self.x == point[0] and self.y == point[1])

    def shift_point(self, x_shift, y_shift):
        self.x += x_shift
        self.y += y_shift

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getPoint(self):
        return (self.x, self.y)
