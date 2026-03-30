class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        shortest_string = min(strs, key=len)
        
        for i in range(len(shortest_string)): 
            char = shortest_string[i]
            for s in strs:
                if char != s[i]:
                    return shortest_string[:i]

        return shortest_string

        