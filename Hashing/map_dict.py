# Hashing using (dict) in python 

# n = int(input("Enter size of array: "))

# arr = list(map(int,input("Enter element: ").split()))

# mp = {}

# for num in arr:
#     mp[num] = mp.get(num,0) + 1

# q = int(input("Enter queries: "))

# while q > 0:
#     number = int(input("Enter number to find frequency: "))
#     print(mp.get(number,0))
#     q -= 1


# For characters
s = input("Enter string: ")

mp = {}

# Precompute
for ch in s:
    mp[ch] = mp.get(ch, 0) + 1

q = int(input("Enter queries: "))

# Fetch
while q > 0:
    c = input("Enter character: ")
    print(mp.get(c, 0))
    q -= 1

# Precompute: O(n)
# Fetching (each query): O(1) (average)
# Overall TC (q queries): O(n + q)
# Space Complexity: O(n) (worst case, for the dictionary storing frequencies)