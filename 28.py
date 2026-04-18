# n = int(input())
# strings = []
# for _ in range(n):
#        s = input().strip()
#        if len(s) > 10:
#                 strings.append(s[0] + s[-1])
#        else:
#                 strings.append(s)
# print(strings)

n = int(input())
for _ in range(n):
    s = input().strip()
    if len(s) > 10:
        print(s[0] + s[-1])
    else:
        print(s)