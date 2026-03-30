class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        l = 0 
        resp = 0 
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) +1 
            max_repet_char_count = max(count.values())
            while (r-l +1) - max_repet_char_count > k:
                count[s[l]]-=1
                l +=1 
            resp = max(resp, (r-l +1))

        return resp 


        