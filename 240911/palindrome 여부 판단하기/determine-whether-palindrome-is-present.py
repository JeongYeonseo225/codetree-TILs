def palindrome(a):
    if a[::-1]==a:
        print("Yes")
    else:
        print("No")

A=input()
palindrome(A)