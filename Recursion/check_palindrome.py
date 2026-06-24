# Two pointer approach
# def chk_palindrome(s):
#     left , right = 0 , len(s) - 1

#     while left < right:
#         if not s[left].isalnum():  # Agar left side wala character letter ya digit nahi hai, to usko skip kar do.
#             left += 1
#         elif not s[right].isalnum():
#             right -= 1
#         elif s[left].lower() != s[right].lower():
#             return False
#         else:
#             left += 1
#             right -= 1
#     return True
    
# str = input("Enter str: ")
# ans = chk_palindrome(str)

# if ans:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# TC = O(n)
# SC = O(1)

# Recursion + Functional Return approach (Optimal)

def chk_palindrome(i,s):
    if i >= len(s) // 2:
        return True

    if s[i] != s[len(s) - i - 1]:
        return False
    
    return chk_palindrome(i + 1, s)

str = input("Enter str: ")
ans = chk_palindrome(0,str)

if ans:
    print("Palindrome")
else:
    print("Not Palindrome")

# TC = O(n)
# SC = O(n) (recursion stack)

