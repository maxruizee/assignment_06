'''
Created on Mar 6, 2016

@author: Max Ruiz
'''
import unittest
from point import Point

class TestPointClass(unittest.TestCase):
    def setUp(self):
        pass

    def test_set_coords(self):
        _x = 5
        _y = 120
        point0 = Point(_x, _y)
        self.assertEqual(_x, point0.getx())
        self.assertEqual(_y, point0.gety())

    def test_check_coincident(self):
        _x = 5
        _y = 120
        point0 = Point(_x, _y)
        point1 = Point(5, 120)
        point2 = Point(_x+3, _y)
        point3 = Point(_x, _y+22)
        point4 = Point(_x+3,_y+22)

        self.assertTrue(point0.check_coincident(point1.getPoint()))
        self.assertFalse(point0.check_coincident(point2.getPoint()))
        self.assertFalse(point0.check_coincident(point3.getPoint()))
        self.assertFalse(point0.check_coincident(point4.getPoint()))

    def test_shift(self):
        _x = 5
        _y = 120
        point0 = Point(_x, _y)
        point0.shift_point(816, 80085)
        self.assertEqual((_x + 816, _y + 80085), point0.getPoint())



