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

        sorted_k_frequencies = sorted(k_frequencies.values(), key=lambda item: item)
        return sorted_k_frequencies[:k]


class Solution:
    def __init__(self, strategy=DictionaryTopKStrategy):
        self.strategy = strategy()

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.strategy.solve(nums, k)
