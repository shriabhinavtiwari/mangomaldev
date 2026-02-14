from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        result = 1
        greater = False
        smaller = False
        cur_sum = 1
        for idx in range(1,len(arr)):
            if arr[idx-1]>arr[idx]:
                if greater:
                    cur_sum=1
                greater = True
                smaller = False
            elif arr[idx-1]<arr[idx]:
                if smaller:
                    cur_sum = 1
                smaller = True
                greater = False
            else:
                greater = False
                smaller = False
                cur_sum = 1
            cur_sum=cur_sum+1 if greater^smaller else cur_sum
            result = max(cur_sum, result)
        return result