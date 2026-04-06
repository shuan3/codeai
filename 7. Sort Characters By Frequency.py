# This file contains several implementations of the 'Sort Characters By Frequency' problem.
# Each Solution class provides a different approach to sorting the characters in a string
# so that characters with higher frequency appear before those with lower frequency.
#
# The function signature is always:
#   def frequencySort(self, s: str) -> str
#
# The output is a string with characters sorted by their frequency in descending order.

class Solution:
    def frequencySort(self, s: str) -> str:
        # First implementation: Group characters by frequency using manual grouping
        d = dict()         # Dictionary to group substrings by their length (frequency)
        temp_l = []       # Temporary list to hold grouped substrings
        s = sorted(s)     # Sort the string to group identical characters together
        print(s)
        for i in range(len(s)):
            if i == 0 and len(s) > 1:
                prev_i = i
                ss = s[i]
                continue
            elif len(s) <= 1:
                return s
            elif s[i] != s[prev_i] and i < len(s) - 1:
                temp_l.append(ss)   # End of a group, add to temp_l
                ss = s[i]
                prev_i = i
            elif s[i] == s[prev_i] and i < len(s) - 1:
                ss = ss + s[i]      # Continue grouping
                prev_i = i
            elif s[i] != s[prev_i] and i == len(s) - 1:
                temp_l.append(ss)   # Last group
                temp_l.append(s[i])
            elif s[i] == s[prev_i] and i == len(s) - 1:
                print("chck here", s[i], ss, ss + s[i])
                temp_l.append(ss + s[i])

        print(temp_l)
        for i in temp_l:
            if len(i) in d.keys():
                d[len(i)].append(i)   # Group substrings by their length
            else:
                d[len(i)] = []
                d[len(i)].append(i)
        print(d)
        sss = ""
        max_freq = sorted(d.keys(), reverse=True)  # Sort frequencies descending
        print(max_freq)
        for i in range(len(max_freq)):
            s1 = "".join(i for i in d[max_freq[i]])
            print(s1)
            sss = sss + s1
        return sss


class Solution:
    def frequencySort(self, s: str) -> str:
        # Second implementation: Count frequencies using a dictionary, then sort
        d = {}
        for j in s:
            if j in d:
                d[j] += 1   # Count each character
            else:
                d[j] = 1
        ds = sorted(d.items(), key=lambda x: x[1], reverse=True)  # Sort by frequency
        x = ""
        for i, j in ds:
            x += i * j      # Repeat character by its frequency
        return x

class Solution:
    def frequencySort(self, s: str) -> str:
        # Third implementation: Count frequencies, sort, and build result
        res = ""
        h = dict()
        for i in range(len(s)):
            h[s[i]] = h.get(s[i], 0) + 1   # Count each character
        h_sort = dict(sorted(h.items(), key=lambda x: x[1], reverse=True))  # Sort by frequency
        for k, v in h_sort.items():
            for i in range(v):
                res += k   # Add character v times
        return res
    

# Fourth implementation: Use collections.Counter for concise frequency counting
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Use Counter to count frequencies, then sort and build result
        s_cnt = Counter(s)  # Count each character
        srted_s_cnt = sorted(s_cnt.items(), key=lambda x: -x[1])  # Sort by frequency
        result = ''.join([char * freq for char, freq in srted_s_cnt])  # Build result string
        return result




# d={"aa":[1,2,3],"bb":2}
# d["aa"]=d.get("aa",[]).append(4)
# print(d)



