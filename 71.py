n = input()
s = 0
for r in n[:3]:
    son = int(r)
    s += son 
t = 0
for r in n[3:6]:
    raqam = int(r)
    t += raqam
if s == t:
    print("True")
else:
    print("False")