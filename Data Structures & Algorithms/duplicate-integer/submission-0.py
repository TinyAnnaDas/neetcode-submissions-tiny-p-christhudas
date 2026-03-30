class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for element in nums:
            if element in count:
                return True
            else:
                count[element] = 1
        return False