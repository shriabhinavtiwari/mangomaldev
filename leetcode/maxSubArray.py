from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(cur_sum + num, num)
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum
