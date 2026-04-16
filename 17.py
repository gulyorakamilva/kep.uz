#17
from unicodedata import digit


for son in range(1000, 10000):
    ming = son // 1000
    yuz = (son // 100) % 10
    on = (son // 10) % 10
    bir = son % 10
    
    yigindi = ming + yuz + on + bir
    
    if yigindi % 2 == 0:
        print(son, end=" ")


# 2-usul
def sum_of_digits(number):
    s = 0
    for char in str(number):
        s += int(char)
    return s   
# print(sum_of_digits(152)) 8  