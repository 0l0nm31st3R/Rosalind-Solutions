s = input("Enter seq 1: ")
t = input("Enter seq 2: ")
HD = 0
for i in range(0, len(s)):
    if s[i]!=t[i]:
        HD += 1
print (HD)


