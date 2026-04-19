
from typing import List
class Solution:
    def sort_key(self,log):
        # Split the log into (identifier, content)
        identifier, content = log.split(" ", 1)
        # Return (content, identifier) to sort by content first, then identifier
        return (content, identifier)

    # Use the key function with sorted()
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        text=[]
        digit=[]
        for i in logs:
            # id=i.split(' ')[0]
            value=i.split(' ',1)[1].replace(' ','')
            if value.isdigit():
                digit.append(i)
            else:
                text.append(i)
        return sorted(text,key=self.sort_key)+digit


logs =["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(Solution().reorderLogFiles(logs))

logs = ["let1 art can", "let3 art zero", "let2 art can", "let4 own kit dig"]

def sort_key(log):
    # Split the log into (identifier, content)
    identifier, content = log.split(" ", 1)
    # Return (content, identifier) to sort by content first, then identifier
    return (content, identifier)

# Use the key function with sorted()
sorted_logs = sorted(logs, key=sort_key)
print(sorted_logs)



# Standard solution
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def sorting_algo(log):
            left_side, right_side = log.split(' ', 1)

## assigning the sorting rule
            if right_side[0].isalpha():
                # priority of 0 for the sorting
                    # any log with a right_side that begins with a letter will comebefore any log with a right_side that begins with a number
                return (0, right_side, left_side)

            else:
                # missing instructions on how to be sorted with only (1, ) passed into it, missing the second arg. 
                return (1,)

        return sorted(logs, key=sorting_algo)
        