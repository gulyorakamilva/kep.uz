# 1 - usul
n = input().lower(); print(n == n[::-1])    

#2-usul
def is_palindrome_str(string):
    return string == string[::-1]

s = input().strip()
print(is_palindrome_str(s))