import unittest
from activities import eat, nap


class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(eat("brocoli", is_healthy = True),
                            "I'm eating brocoli, because my body is a temple")
    def test_eat_unhealty(self):
        self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza, because YOLO!")

    def test_short_nap(self):
        self.assertEqual(nap(1), "I'm feeling refreshed after 1 hour of nap")

    def test_long_nap(self):
        self.assertEqual(nap(3), "Ughhh, I overslept")


if __name__ == "__main__":
    unittest.main()


