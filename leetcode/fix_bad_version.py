# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # brute force version
        # O(n)
        # for num in range(1,n+1):
        #     if isBadVersion(num):
        #         return num
        # optimized solution
        low:int  = 1
        high: int = n
        while high >= low:
            mid:int = (low+high)//2
            bad:bool = isBadVersion(mid)
            if bad:
                result = mid
                high = mid-1
            else:
                low = mid + 1
        return result