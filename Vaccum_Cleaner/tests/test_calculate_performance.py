# test_calculate_performance.py

import unittest
from source.calculate_performance import calculate_performance

class TestCalculatePerformance(unittest.TestCase):
    def test_calculate_performance(self):
        # Test with some example values
        result = calculate_performance(2, 2, 2, 2)
        self.assertEqual(result['total_actions'], 6)
        self.assertEqual(result['performance'], 3)

        # Test division by zero (no dirt cleaned)
        result = calculate_performance(2, 2, 2, 0)
        self.assertEqual(result['performance'], 0)  # Performance should be 0 when no dirt is cleaned

if __name__ == '__main__':
    unittest.main()
