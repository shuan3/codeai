s="-042"
print(int(s))

class Solution:
    def myAtoi(self, s: str) -> int:
        data=""
        break_sign=0
        for r in range(len(s)):
            if break_sign==2 or (data!="" and s[r] in ("-","+")):
                break
            if s[r]==" " and data=="":
                continue
            elif s[r]=="+" or (s[r]=="-" and data==""):
                if s[r]=="+" or s[r]=="-":
                    break_sign+=1
                if break_sign<2:
                    data+=s[r]
            elif s[r] in ("0","1","2","3","4","5","6","7","8","9"):
                data+=s[r]
            elif data!="" and s[r] not in ("0","1","2","3","4","5","6","7","8","9"):
                break
            else:
                break
        
        num = 0 if data in ("","-","+","-+","+-") else data
        print(num)
        num=int(num)
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1
        return num




class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        # Check for sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        # After optional sign, next must be digit
        if i == n or not s[i].isdigit():
            return 0
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        num *= sign
        # Clamp to 32-bit signed int range
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1
        return num

s="0-1"
s="-91283472332"
s ="words and 987"
s="+-12"
print(Solution().myAtoi(s))