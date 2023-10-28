import unittest

from main import Solution


class TopKFrequentElementsTest(unittest.TestCase):
    def test_simplest_case(self):
        nums = [1]
        k = 1
        self.assertEqual([1], Solution().topKFrequent(nums, k))


if __name__ == '__main__':
    unittest.main()
