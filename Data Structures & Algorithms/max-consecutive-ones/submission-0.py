class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        count = 0 
        for i in nums:
            if i == 1: 
                count += 1 
            else: 
                if max_num < count:
                    max_num = count
                count = 0 
        if max_num < count:
                    max_num = count
        return max_num
        
        