#  1. Given an integer array, return a new array where each element at index i is the product of all numbers in the original array except nums[i], without using division

# def newArray(arr):
#     n = len(arr)
#     result = [1] * n

#     prefix = 1
#     for i in range(n):
#         result[i] = prefix
#         prefix *= arr[i]

#     suffix = 1
#     for i in range(n - 1, -1, -1):
#         result[i] *= suffix 
#         suffix *= arr[i]

#     return result


# arr=[1,4,5,6,7]
# print(newArray(arr))




#  2. Given an integer array, determine if any value appears at least twice

# def repeat(arr):
#     seen = set()
#     dublicate = set()

#     for value in arr:
#         if value not in seen:
#             seen.add(value)
#         else:
#             dublicate.add(value)

#     return list(dublicate)
# arr = [1,3,4,5,2,4,5,3]
# print(repeat(arr))



# 3. Given an integer array and a target, return indices of the two numbers such that they add up
#  to target (assume exactly one solution).


# def twoSum(arr,target):
#     map = {}
#     for i , num in enumerate(arr):
#         complement = target - num
#         if complement in map:
#             return [map[complement] , i]
#         map[num] = i
#     return []

# arr=[2, 7, 11, 15]
# target = 9
# print(twoSum(arr,target))


# 4. Given two arrays, return their intersection where each element in the result appears as many
#  times as it shows in both arrays.

# def intersection(num1 , num2):
#     map = {}
#     intersection=[]

#     for i in range(len(num1)):
#         if num1[i] not in map:
#             map[num1[i]] = 0
#         map[num1[i]] += 1 

#     for j in range(len(num2)):
#         if num2[j] in map and map[num2[j]] > 0:
#             intersection.append(num2[j])
#             map[num2[j]] -= 1

    
#     return intersection




# nums1 = [4, 9, 5, 9]
# nums2 = [9, 4, 9, 8, 4]
# print(intersection(nums1,nums2))


# def intersection(num1,num2):
#     num1.sort()
#     num2.sort()

#     i = j = 0
#     result = []
#     while i < len(num1) and j < len(num2):
#         if num1[i] == num2[j]:
#             result.append(num1[i])
#             i +=1
#             j += 1
#         elif num1[i] > num2[j]:
#             j+=1
#         else:
#             i+=1

#     return result

# nums1 = [4, 9, 5, 9]
# nums2 = [9, 4, 9, 8, 4]
# print(intersection(nums1,nums2))



#  5. Given an array of integers, move all zeros to the end while keeping the relative order of
#  non-zero elements.


def zeroRight(arr):
    pos = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
        
    for i in range(pos,len(arr)):
        arr[i] = 0

    return arr

arr = [0, 1, 0, 3, 12]
print(zeroRight(arr))