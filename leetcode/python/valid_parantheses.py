class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check_dict = {")":"(", "]":"[", "}":"{"}

        for character in s:
            if character in check_dict:
                if stack  and stack[-1] == check_dict[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
        
        return True if not stack else False