from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            total = 0
            for banana in piles:
                total += math.ceil(banana / k)
            if total > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res

