import base64
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "[]"  # Encode an empty list as "[]"
        if strs == [""]:
            return '[""]'
        
        encoded_strings = [base64.b64encode(s.encode('utf-8')).decode('utf-8') for s in strs]
        print("!!",encoded_strings)
        return ("~~~").join(encoded_strings)

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []  # Decode "[]" back to an empty list
        if s == '[""]':
            return [""]

        split_string = s.split("~~~")
        print("??",split_string)
        decode_strings = [base64.b64decode(s.encode('utf-8')).decode('utf-8') for s in split_string]
        print("@@",decode_strings)
        return decode_strings


solutions = Solution()
strs = [""]
result = solutions.encode(strs)
print("~~",result)

dec = solutions.decode(result)
print(dec)