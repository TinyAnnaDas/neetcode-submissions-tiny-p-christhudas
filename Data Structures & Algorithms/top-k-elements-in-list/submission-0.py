class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}

        for n in nums:
            my_dict[n] = my_dict.get(n, 0) +1 

        sorted_nums = sorted(my_dict, key=my_dict.get, reverse=True)
        result_array= []
        for i in range(k):
            result_array.append(sorted_nums[i])

        return result_array
        
            
        