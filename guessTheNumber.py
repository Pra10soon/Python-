def isPalindrome(str):
    return str == str[::-1]

s = str(input("Enter the string "))
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")
