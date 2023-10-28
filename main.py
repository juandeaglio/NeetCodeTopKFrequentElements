from abc import ABC, abstractmethod
from typing import List, Protocol
import heapq

class TopKStrategy(Protocol):
    @abstractmethod
    def solve(self, nums: List[int], k: int) -> List[int]:
        pass


class DictionaryTopKStrategy(TopKStrategy, ABC):
    def solve(self, nums: List[int], k: int) -> List[int]:
        k_frequencies = {}

        for num in nums:
            k_frequencies[num] = k_frequencies.get(num, 0) + 1

        items = k_frequencies.items()
        sorted_k_frequencies = [key for key, _ in sorted(items, key=lambda item: item[1], reverse=True)[:k]]
        return list(sorted_k_frequencies)


class HeapQueueTopKStrategy(TopKStrategy, ABC):
    def solve(self, nums: List[int], k: int) -> List[int]:
        k_frequencies = {}

        for num in nums:
            k_frequencies[num] = k_frequencies.get(num, 0) + 1

        min_heap = []
        for key, val in k_frequencies.items():
            heapq.heappush(min_heap, (val, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        sorted_heap = sorted(min_heap, reverse=True)
        top_k_keys = []

        for val, key in sorted_heap:
            top_k_keys.append(key)

        return top_k_keys


class BucketSortTopKStrategy(TopKStrategy, ABC):
    def solve(self, nums: List[int], k: int) -> List[int]:
        k_frequencies = {}
        buckets = [[] for _ in range(len(nums)+1)]
        for num in nums:
            k_frequencies[num] = k_frequencies.get(num, 0) + 1

        for num, freq in k_frequencies.items():
            buckets[freq].append(num)

        top_k = []
        for bucket in range(len(buckets)-1, -1, -1):
            for val in buckets[bucket]:
                top_k.append(val)
                if len(top_k) == k:
                    return top_k

        return top_k


class Solution:
    def __init__(self, strategy=BucketSortTopKStrategy):
        self.strategy = strategy()

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.strategy.solve(nums, k)
