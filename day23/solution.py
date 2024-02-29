from heapq import heappush, heappop
from typing import List


class TopKFrequentElements:
    def __init__(self, values):
        self.values = values

    def get(self, k: int) -> List[int]:
        if not self.values:
            return []

        map = {}
        for num in self.values:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        heap = []
        for key,value in map.items():
            if len(heap) < k:
                heappush(heap,[value,key])
            elif heap[0][0] < value:
                heappop(heap)
                heappush(heap,[value,key])

        return [item for count,item in heap[::-1]]