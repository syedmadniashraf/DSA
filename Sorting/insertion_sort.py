class Solution:
    # Function to sort the array using insertion sort
    def insertionSort(self, nums):
        n = len(nums) # Size of the array 
        
        # For every element in the array 
        for i in range(1, n):
            key = nums[i] # Current element as key 
            j = i - 1
            
            # Shift elements that are greater than key by one position
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            
            nums[j + 1] = key # Insert key at correct position
        
        return nums

arr = list(map(int, input("Enter array: ").split()))

print("Before Insertion Sort:")
print(" ".join(map(str, arr)))

solution = Solution()
solution.insertionSort(arr)

print("After Insertion Sort:")
print(" ".join(map(str, arr)))

# TC = O(n) --> Best Case
# TC = O(n²) --> Worst,Avg Case

# SC = O(1)