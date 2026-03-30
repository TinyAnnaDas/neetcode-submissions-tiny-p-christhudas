class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_array = {}
        for num in nums: 
            count_array[num] = count_array.get(num, 0) +1
        
        max_count = 0
        majority = None
        for num, count in count_array.items():
            if count > max_count:
                max_count = count
                majority = num
                
        return majority 
        

        


        