# Code if the string contains only lowercase:

# s = input("Enter string: ")

# # Precompute
# hash_arr = [0] * 26

# for ch in s:
#     hash_arr[ord(ch) - ord('a')] += 1  # Yahan hum ASCII value ko 0–25 ke range me convert kar rahe hain.

# # number of query

# q = int(input("Enter number of queries: "))
# while q > 0:
#     c = input("Enter character: ")

#     # Fetch
#     print(hash_arr[ord(c) - ord('a')])

#     q -= 1

# Time Complexity:
# Precompute: O(n) (n = length of string)
# Har query: O(1)
# q queries ke liye: O(q)
# overall: O(n + q)
# SC = O(1) because 26 is constant


# Uppercase + Lowercase + Digits + Symbols (ASCII)

s = input("Enter string: ")

hash_arr = [0] * 256

for ch in s:
    hash_arr[ord(ch)] += 1  # Yahan hum character ki original ASCII value ko hi index bana rahe hain.

q = int(input("Enter number of queries: "))
while q > 0:
    c = input("Enter character: ")

    print(hash_arr[ord(c)])

    q -= 1


# Time Complexity:
# Precompute: O(n) (n = length of string)
# Har query: O(1)
# overall: O(n + q)
# SC = O(1) because 256 is constant