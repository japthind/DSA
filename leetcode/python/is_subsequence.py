"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).


In this kind of problem we can easily use Two Pointers approach.

In two pointers what we do that we initialze the 2 pointers, one on string s and one on string t.
Then we traverse both the strings and check that whether the character at s[i] == s[j]. if it is equal we increment both
the pointers and perform the comparison on the next character.

If they are not same then only j is incremented so if i reaches the end of string s that means that it is a subsequence and
if j reaches the end it means that it is not a subsequence

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s):
            return True
        else:
            return False

s='abc'
t='ahbdgc'        
solutions = Solution()
results = solutions.isSubsequence(s,t)

print(results)