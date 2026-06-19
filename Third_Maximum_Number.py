class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        unique_nums = list(unique_nums)
        unique_nums.sort()
        if len(unique_nums) < 3:
            return max(unique_nums)
        else:
            return unique_nums[-3]
