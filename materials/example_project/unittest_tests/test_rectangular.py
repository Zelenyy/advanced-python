import os
import sys
import unittest
from unittest import TestCase
from spc.rectangular import Rectangular


class RectangularTest(TestCase):
    HEIGHT = 100
    WIDTH = 50

    def setUp(self) -> None:
        print("a")
        self.rect = Rectangular(self.HEIGHT, self.WIDTH)

    def test_area(self):
        self.assertEqual(self.rect.area, self.HEIGHT*self.WIDTH)

    def test_resize(self):

        for i in range(5):
            with self.subTest(scale = i):
                self.rect.resize(i*self.HEIGHT, i*self.WIDTH)
                self.assertEqual(self.rect.width, i*self.WIDTH)
                self.assertEqual(self.rect.height, i*self.HEIGHT)

        for pair in [(-10, 10), (10, -10)]:
            with self.subTest(pair = pair):
                with self.assertRaises(ValueError):
                    self.rect.resize(*pair)

        for pair in [(10, 10.0), (10.0, 10)]:
            with self.subTest(pair = pair):
                with self.assertRaises(TypeError):
                    self.rect.resize(*pair)

    @unittest.skip
    def test_rotation(self):
        self.rect.rotate()
        self.assertEqual(self.rect.height, self.WIDTH)
        self.assertEqual(self.rect.width, self.HEIGHT)

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_system(self):
        os.system("ls")

    def tearDown(self) -> None:
        del self.rect
        print("I open at the close")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(RectangularTest("test_area"))
    suite.addTest(RectangularTest("test_system"))
    runner = unittest.TextTestRunner()
    runner.run(suite)