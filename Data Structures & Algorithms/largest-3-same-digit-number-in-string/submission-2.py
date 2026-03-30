class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                string_piece = num[i:i+3]
                if not result:
                    result = string_piece
                else:
                    if int(result) < int(string_piece):
                        result = string_piece

        return result


        