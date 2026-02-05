# merge sort

# def merge_sort(arr, left , right):

#     if left < right:
#         mid = (left + right)//2

#         merge_sort(arr,left , mid)

#         merge_sort(arr,mid + 1, right)

#         merge(arr, left , mid ,right )

# def merge(arr, left , mid , right):
#     L = arr[left : mid+1]
#     R = arr[mid+1 : right+1]

#     i = j = 0
#     k = left

#     while i < len(L) and j < len(R):
#         if L[i] <= R[j]:
#             arr[k] = L[i] 
#             i +=1
#         else:
#             arr[k] = R[j]
#             j +=1
#         k +=1

#     while i < len(L):
#         arr[k] = L[i]
#         i+=1
#         k+=1

#     while j < len(R):
#         arr[k] = R[j]
#         j+=1
#         k+=1



# arr = [6, 3, 9, 5]
# merge_sort(arr, 0, len(arr)-1)
# print(arr)






#quick sort

# def quick_sort(arr, low , high):

#     if low < high:
#         pivit_point= partition(arr,low,high)

#         quick_sort(arr,low,pivit_point - 1)

#         quick_sort(arr,pivit_point + 1,high)

# def partition(arr,low,high):
#     pivit = arr[high]
#     i= low - 1
#     for j in range(low , high):
#         if arr[j] < pivit:
#             i+=1
#             arr[i],arr[j]= arr[j],arr[i]

#     arr[i+1],arr[high] = arr[high],arr[i+1]
#     return i + 1


# arr = [6, 3, 9, 5, 2, 8]

# quick_sort(arr,0,5)

# print(arr)








#heap sort

# def heapify(arr,n,i):
#     largest = i
#     left = 2*i+1
#     right = 2*i+1

#     if n > left and arr[left] > arr[largest]:
#         largest = left

#     if n > right and arr[right] > arr[largest]:
#         largest = right

#     if largest != i:
#         arr[i],arr[largest] = arr[largest],arr[i]
#         heapify(arr,n,largest)


# def heap_sort(arr):
#     n = len(arr)

#     for i in range(n//2-1,-1,-1):
#         heapify(arr,n,i)

#     for i in range(n-1,0,-1):
#         arr[i],arr[0] = arr[0],arr[i]
#         heapify(arr,i,0)
    
#     return arr


# arr = [4, 10, 3, 5, 1]
# print(heap_sort(arr))





#Bubble sort 

# def bubbleSort(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr


# arr = [4, 10, 3, 5, 1]
# print(bubbleSort(arr))




#selection sort 

# def selectionSort(arr):
#     n= len(arr)
#     for i in range(n):
#         min_val= i
#         for j in range(i+1,n):
#             if arr[j] < arr[min_val]:
#                 min_val = j
#         arr[i],arr[min_val]= arr[min_val],arr[i] 
#     return arr

# arr = [64, 25, 12, 22, 11]
# print(selectionSort(arr))



#Insertion sort


# def insertionSort(arr):
#     for i in range(1,len(arr)):
#         key = i 
#         j = i-1

#         while j>=0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -=1
#         arr[j+1] = key

#     return arr



# arr = [5, 3, 4, 11, 2]
# print(insertionSort(arr))




#counting sorting


# def countingSort(arr):
#     max_v = max(arr)

#     count = [0] * (max_v + 1)
#     output = [0] * (len(arr))

#     for num in arr:
#         count[num] += 1

#     for i in range(1,len(count)):
#         count[i] += count[i-1]

#     for num in reversed(arr):
#         output[count[num] - 1] = num
#         count[num] -=1

#     for i in range(len(arr)):
#         arr[i] = output[i]

#     return arr



# arr = [4, 2, 2, 8, 3, 3, 1]
# print(countingSort(arr))



# bubble sort

# def bubbleSort(nums):
#     n = len(nums)

#     for i in range(n):
#         isSwaping = False
#         for j in range(n-i-1):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#                 isSwaping = True
#         if not isSwaping:
#             break
#     return nums



