import time
import unittest

from main import Solution, HeapQueueTopKStrategy, BucketSortTopKStrategy, DictionaryTopKStrategy


class TopKFrequentElementsTest(unittest.TestCase):
    def test_simplest_case(self):
        nums = [1]
        k = 1
        self.assertEqual([1], Solution().topKFrequent(nums, k))

    def test_non_trivial_case(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        self.assertEqual([1, 2], Solution().topKFrequent(nums, k))

    def test_negative_numbers(self):
        nums = [-1, -1]
        k = 1
        self.assertEqual([-1], Solution().topKFrequent(nums, k))

    def test_non_trivial_case_heap_queue(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        self.assertEqual([1, 2], Solution(strategy=HeapQueueTopKStrategy).topKFrequent(nums, k))

    def test_non_trivial_case_bucket_sort(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        self.assertEqual([1, 2], Solution(strategy=BucketSortTopKStrategy).topKFrequent(nums, k))

    def test_large_array_dictionary(self):
        nums = []
        largest_value = 10000
        for i in range (0, largest_value):
            for j in range(0, i):
                nums.append(i)
        k = largest_value
        start = time.time()
        Solution(strategy=DictionaryTopKStrategy).topKFrequent(nums, k)
        end = time.time()
        resultTime = end-start
        self.assertLess(resultTime, 10)

    def test_large_array_heap_queue(self):
        nums = []
        largest_value = 10000
        for i in range (0, largest_value):
            for j in range(0, i):
                nums.append(i)
        k = largest_value
        start = time.time()
        Solution(strategy=HeapQueueTopKStrategy).topKFrequent(nums, k)
        end = time.time()
        resultTime = end-start
        self.assertLess(resultTime, 10)

    def test_large_array_bucket_sort(self):
        nums = []
        largest_value = 10000
        for i in range (0, largest_value):
            for j in range(0, i):
                nums.append(i)
        k = largest_value
        start = time.time()
        Solution(strategy=BucketSortTopKStrategy).topKFrequent(nums, k)
        end = time.time()
        resultTime = end-start
        self.assertLess(resultTime, 10)

if __name__ == '__main__':
    unittest.main()
