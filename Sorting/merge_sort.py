class solution:
    def merge(self,arr,low,mid,high): # func to merge two halves
        temp = []
        left , right = low , mid + 1

        while(left <= mid and right <= high):
            if(arr[left] <= arr[right]):
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        
        while(left <= mid):
            temp.append(arr[left])
            left += 1
        
        while(right <= high):
            temp.append(arr[right])
            right += 1

        for i in range(low,high+1):
            arr[i] = temp[i-low]

    # recursive merge sort

    def mergeSort(self,arr,low,high):
        if(low >= high):
            return
        mid = (low + high) // 2
        self.mergeSort(arr,low,mid)
        self.mergeSort(arr,mid+1,high)
        self.merge(arr,low,mid,high)

arr = list(map(int,input("Enter array: ").split()))
sol = solution()
sol.mergeSort(arr, 0, len(arr)-1)
print(*arr)

# Array har baar 2 halves me divide hota hai → log n levels.
# Har level par merge karne me O(n) time lagta hai.
# Total  TC= O(n × log n) = O(n log n)

# SC = O(n) (using "temp" array to store element in sorted order)