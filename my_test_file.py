import unittest


class TestSum(unittest.TestCase):

    def test_add(self):
        self.assertEqual(sum([4, 2, 1]), 7, "Answer is 7")

if __name__ == '__main__':
    unittest.main()

