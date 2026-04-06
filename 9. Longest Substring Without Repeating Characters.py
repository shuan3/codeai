s=[1,2,3,4,5]
print(s[1:5])
print(s[1:6])



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if len(s[i:j+1])==len(set(s[i:j+1])):
                    l=max(l,len(s[i:j+1]))
        return l

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        charSet=set()
        for r in range(len(s)):
            # We use a while loop here (not if) because there may be multiple duplicates in the window.
            # The while loop keeps removing characters from the left until s[r] is not in charSet,
            # ensuring the window always contains unique characters.
            # Example: s = "abba"
            # When r=2 (s[2]='b'), charSet={'a','b'}; 'b' is in charSet, so we remove from the left
            # until 'b' is no longer in charSet. This handles cases with consecutive duplicates.
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
                
        

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    res = max(res, j - i + 1)
        return res
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        char_map = {}
        max_len = 0
        j = 0
        
        for i in range(len(s)):
            if s[i] in char_map:
                # Move the left pointer j, but only if the duplicate is inside the current window
                j = max(j, char_map[s[i]] + 1)
                
            char_map[s[i]] = i
            max_len = max(max_len, i - j + 1)
            
        return max_len