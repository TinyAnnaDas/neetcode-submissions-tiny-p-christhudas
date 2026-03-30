class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count_dict = {}
        for i in range(len(nums)):
            count_dict[nums[i]] = count_dict.get(nums[i], 0) + 1

        max_value = -1
        for num in count_dict:
            if num > max_value and count_dict[num]==1: 
                max_value = num
        
        return max_value 
            



        