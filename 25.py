import math

def solve():
    a = float(input())
    b = float(input())
    
    discriminant = a**2 - 4*b
    sqrt_d = math.sqrt(discriminant)
    
    x = (a + sqrt_d) / 2
    y = (a - sqrt_d) / 2
    
    print(f"{x} {y}")

solve()


# 2- usul
import math
a = int(input())
b = int(input())
d =  a ** 2 - 4 * b
sqrt_d = math.sqrt(d)
x1 = (a + sqrt_d) / 2
x2 = (a - sqrt_d) / 2
print(x1, x2)