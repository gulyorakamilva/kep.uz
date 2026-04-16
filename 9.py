# 2178 * 4 = 8712
# 8712
# stringni kesish va teskarisini o`girish
# txt = "2178"
# print(txt[::-1])  # 8712
#print(int(txt[::-1]) * 4)  # 34848
# print(int(txt[::-1]) * 4 == 8712)  # False

def reverse_number(num):
    return int(str(num)[::-1])
# print(reverse_number(1589))  # 9851
for number in range(1000, 10000):
    if reverse_number(number) * 4 == number:
        print(number)