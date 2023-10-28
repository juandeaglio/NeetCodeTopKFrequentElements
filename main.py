from abc import ABC, abstractmethod
from typing import List, Protocol


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


class Solution:
    def __init__(self, strategy=DictionaryTopKStrategy):
        self.strategy = strategy()

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.strategy.solve(nums, k)
