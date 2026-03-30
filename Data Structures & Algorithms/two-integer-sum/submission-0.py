class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      value_index_map = {}  
      for i, value in enumerate(nums):
        complement = target - value 
        if complement in value_index_map:
            return [value_index_map[complement], i]

        value_index_map[value] = i
        