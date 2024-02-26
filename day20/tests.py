import unittest

from day20.solution import IslandMapper


class IslandMapperTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(6, IslandMapper([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]).get_biggest_surface_area())

    def test_2(self):
        self.assertEqual(0, IslandMapper([[0,0,0,0,0,0,0,0]]).get_biggest_surface_area())
