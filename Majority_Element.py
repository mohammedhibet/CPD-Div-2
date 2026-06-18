class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        x = Counter(nums)
        for i in x:
            if x[i] > n/2:
                return i
