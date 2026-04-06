class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        else:
            return False




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in set(s):
            if s.count(i)!=t.count(i):
                return False
        for i in set(t):
            if s.count(i)!=t.count(i):
                return False
        return True