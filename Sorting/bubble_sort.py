# Brute Force

# class BubbleSort:
#     def bubble_sort(self,arr):
#         n = len(arr)

#         for i in range(n-1,-1,-1):
#             for j in range(i):
#                 if(arr[j] > arr[j+1]):
#                     arr[j], arr[j+1] = arr[j+1], arr[j] # Swapping
        
#         print("After using bubble sort: ")
#         print(" ".join(map(str,arr)))

# arr = list(map(int,input("Enter array: ").split()))
# print("Before bubble sort: ")
# print(" ".join(map(str,arr)))
# sorter = BubbleSort()
# sorter.bubble_sort(arr)

# TC = O(n²) (All Cases) --> array sorted hone pr bhi saare paas execute honge (because there is no swapped flag (True/False) to check swapping)
# SC = O(1)

# Optimal approach (with swapped flag)

class BubbleSort:
    def bubble_sort(self,arr):
        n = len(arr)

        for i in range(n-1,-1,-1):
            did_swap = False
            for j in range(i):
                if(arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j] # Swapping
                    did_swap = True
            if not did_swap:
                break
        
        print("After using bubble sort: ")
        print(" ".join(map(str,arr)))
        
arr = list(map(int,input("Enter array: ").split()))
print("Before bubble sort: ")
print(" ".join(map(str,arr)))
sorter = BubbleSort() 
sorter.bubble_sort(arr)

# TC = O(n) --> Best Case
# TC = O(n²) --> Worst,Avg Case

# SC = O(1)