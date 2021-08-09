s = input()
p = input()
s1 = s + s[:-1]
if (p in s1 and len(p) <= len(s)):
    print("Yes")
else:
    print("No")