n = int(input())
s = 1
for son in range(1, n + 1):
    s *= son
print(s)


# 2-usul
# n = 4 
# sikldagi qadamlar:
# 1. son == > s *= 1 = 1
# 2. son == > s *= 2 = 2
# 3. son == > s *= 3 = 6
# 4. son == > s *= 4 = 24
