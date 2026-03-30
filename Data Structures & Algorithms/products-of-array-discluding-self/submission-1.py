class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 1 
        result = [1] * n
        for i in range(n): 
            result[i] = result[i] * left 
            left = left * nums[i]

        right = 1
        for i in range(n-1, -1, -1):
            result[i] = result[i] * right
            right = right * nums[i]

        return result
