from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]
        min_sum = nums[0]
        cur_min = nums[0]
        total_sum = nums[0]

        for num in nums[1:]:
            total_sum+=num
            cur_sum = max(cur_sum+num, num)
            max_sum = max(cur_sum, max_sum)
            cur_min = min(cur_min+num, num)
            min_sum = min(cur_min, min_sum)
        if total_sum==min_sum:
            return max_sum
        return max(max_sum,total_sum - min_sum)