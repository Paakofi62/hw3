import unittest
from Examples.squareroot import SquareRoot
from Examples.encap import Force


class MyTestCase(unittest.TestCase):
    def test_Examples_root(self):
        self.assertEqual(6, SquareRoot.squareroot(36, 2))



if __name__ == '__main__':
    unittest.main()
