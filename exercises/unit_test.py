import unittest

def suma(num_1, num_2):
    return num_1 + num_2

class BlackBoxTest(unittest.TestCase):

    def test_sum_two_positives(self):
        num_1 = 10
        num_2 = 5

        result = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_sum_two_nagatives(self):
        num_1 = -10
        num_2 = -7

        result = num_1 - num_2

        self.assertEqual(result, -17)

if __name__ == '__main__':
    unittest.main()