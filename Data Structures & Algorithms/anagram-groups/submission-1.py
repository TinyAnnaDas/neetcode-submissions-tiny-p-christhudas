class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26 

            for char in s:
                count[ord(char) - ord("a")] +=1

            my_dict[tuple(count)].append(s)
        return list(my_dict.values())


        