import math
import unittest
def square_root(l):
    return math.sqrt(l)
class Testclass(unittest.TestCase):
    def test_case1(var):
        var.assertEqual(square_root(121), 11, "Should be 11")
    def test_case2(var):
        var.assertEqual(square_root(144), 12, "Should be 12")
    def test_case3(var):
        var.assertEqual(square_root(169), 13, "Should be 13")
    def test_case4(var):
        var.assertEqual(square_root(196), 14.3, "Should be 14")
    def test_case5(var):
        var.assertEqual(square_root(225), 15.2, "Should be 15")
    def test_case6(var):
        var.assertEqual(square_root(256), 16, "Should be 16")
if __name__ == "__main__":
    unittest.main()