import unittest

def square(n):
    return n**2

class ActivityTests(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(5),25)
        self.assertEqual(square(10),100)
        self.assertEqual(square(20), 400)
        self.assertEqual(square(50), 2500)
        self.assertEqual(square(7), 49)
        self.assertEqual(square(3), 9)
        self.assertEqual(square(5), 25)
        self.assertEqual(square(10), 100)


if __name__ == "__main__":
    unittest.main()
