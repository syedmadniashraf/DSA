# Brute Force 

# def count_freq(arr,x):
#     count = 0
#     for i in range(len(arr)):
#         if(arr[i]) == x:
#             count += 1
#     return count
    
# arr = list(map(int,input("Enter arr: ").split()))
# x = int(input("Enter num: "))

# print(f"The freq of {x} is :",count_freq(arr,x))

# Hash approach

n = int(input("Enter array size: "))

arr = list(map(int,input("Enter arr: ").split()))

# Precompute
hash_arr = [0] * 13

for i in range(n):
    hash_arr[arr[i]] += 1

q = int(input("Enter queries: "))

while q > 0:
    number = int(input("Enter number to find frequency: "))
    print(hash_arr[number])
    q -= 1

# Prestoring --> TC = O(n)
# Fetching  --> TC = O(1)
# Overall  --> TC = O(n + q)
# SC = O(max element)  --> Agr code mai hash_arr = [0] * (max_element + 1)