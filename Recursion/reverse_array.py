# Brute force

# class solution:
#     def reverseArray(self,arr):
#         n = len(arr)
#         rev_arr = [0] * n

#         for i in range(n):
#             rev_arr[i] = arr[n-i-1]
#         return rev_arr

# sol = solution()
# arr = list(map(int, input("Enter arr: ").split()))
# result = sol.reverseArray(arr)
# print("Reversed array:", result)

# TC = O(n)
# SC = O(n)

# Better approac (two pointers)

# class solution:
#     def reverseArray(self, arr):
#         p1 = 0
#         p2 = len(arr) - 1

#         while p1 < p2:
#             arr[p1] , arr[p2] = arr[p2] , arr[p1]

#             p1 += 1
#             p2 -= 1
#         return arr
# sol = solution()
# arr = list(map(int, input("Enter arr: ").split()))
# result = sol.reverseArray(arr)
# print("Reversed array:", result)


# TC): O(n)
# SC = O(1) Extra array is used

# Using built in func

class solution:
    def reverseArray(self, arr):
        arr[:] = arr[::-1]
        return arr
sol = solution()
arr = list(map(int, input("Enter arr: ").split()))
result = sol.reverseArray(arr)
print("Reversed array:", result)

# TC: O(n)
# SC: O(n)