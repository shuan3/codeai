text=["abe" ,"tea" ,"tan" ,"ate" ,"nat" ,"bat"]
for i in text:
    print(sorted(i),set(sorted(i)),"".join(set(sorted(i))))



from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        for i in strs:
            if "".join(sorted(i)) in d:
                 d["".join(sorted(i))].append(i)
            else:
                d["".join(sorted(i))]=[i]
        return [val for val in d.values()]




from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        check_anagram = defaultdict(list)
        for string in strs:
            s = "".join(sorted(string))
            check_anagram[s].append(string)
        return list(check_anagram.values())