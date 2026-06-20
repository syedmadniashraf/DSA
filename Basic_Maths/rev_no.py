# def revNum(n):
#     rev = 0
#     while(n > 0):
#         lastDigit = n % 10
#         n = n // 10
#         rev = (rev * 10) + lastDigit
#     return rev

# n = int(input("Enter n: "))
# print(f"N: {n}")
# revDigit = revNum(n)
# print(f"Reverse digit: {revDigit}")



class Solution:
    # Function to reverse digits of a number
    def reverseNumber(self, n):
        # Variable to store reversed number
        revNum = 0

        # Loop until all digits are processed
        while n > 0:
            # Get the last digit
            lastDigit = n % 10

            # Append it to the reversed number
            revNum = revNum * 10 + lastDigit

            # Remove the last digit from n
            n = n // 10

        # Return the reversed number
        return revNum

# Driver code
obj = Solution()
num = int(input("Enter num: "))
print(obj.reverseNumber(num)) 
