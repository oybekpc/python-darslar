import unittest
from circle import getArea,getPerimetr

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmastEqual(getArea(5),78.53975)
        self.assertEqual(getArea(10),314.159)

    def test_perimetr(self):
        self.assertAlmastEqual(getArea(5),78.53975)

        
unittest.main()