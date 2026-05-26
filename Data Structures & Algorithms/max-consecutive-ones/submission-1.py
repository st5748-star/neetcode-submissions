class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_ones = 0
        count_max = 0
        for num in nums:
            if num == 1:
                count_ones += 1
                count_max = max(count_max,count_ones)
            else:
                count_ones = 0
        return count_max
