class Solution:
    def countElements(self, arr: List[int]) -> int:
        output = 0
        for i in arr:
            if i+1 in arr:
                output+=1
        return output

        