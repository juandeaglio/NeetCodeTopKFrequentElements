from abc import ABC, abstractmethod
from typing import List, Protocol


class TopKStrategy(Protocol):
    @abstractmethod
    def solve(self, nums: List[int], k: int) -> List[int]:
        pass


class DictionaryTopKStrategy(TopKStrategy, ABC):
    def solve(self, nums: List[int], k: int) -> List[int]:
        pass


class Solution:
    def __init__(self, strategy=DictionaryTopKStrategy):
        self.strategy = strategy()

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.strategy.solve(nums, k)
