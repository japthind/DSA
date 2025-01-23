"""
    Time Complexity Analysis

    Splitting the string (s.split()):
    Time complexity: O(n), where n is the length of the string s. 
    The split() method scans the entire string to identify words and splits them.
    
    Reversing the list (string[::-1]):
    Time complexity: O(m), where m is the number of words in the list. 
    Reversing involves iterating through the list once.
    
    Joining the list (' '.join(string[::-1])):
    Time complexity: O(k), where k is the total number of characters in all the words in the list. 
    Joining requires scanning each word and adding spaces.
    
    Since k is at most equal to n (the total length of the input string), 
    the overall time complexity is dominated by the splitting operation.

    Overall Time Complexity
    The overall time complexity is O(n), where n is the length of the input string s.
"""

class Solution:
    def isSubsequence(self, s: str) -> str:
        string = s.split()
        result = ' '.join(string[::-1])
        return result

s="hello    world"
solutions = Solution()
results = solutions.isSubsequence(s)

print(results)