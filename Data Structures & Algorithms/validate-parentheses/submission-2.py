class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_close_p = {"(" : ")", "[": "]", "{": "}"}
        for bracket in s:

            if bracket in open_close_p:
                stack.append(bracket)
            else:
                if stack and bracket == open_close_p[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
            