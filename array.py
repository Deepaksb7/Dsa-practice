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


# def zeroRight(arr):
#     pos = 0

#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[pos] = arr[i]
#             pos += 1
        
#     for i in range(pos,len(arr)):
#         arr[i] = 0

#     return arr

# arr = [0, 1, 0, 3, 12]
# print(zeroRight(arr))



#  6. Given an array of integers, return the length of the longest sequence of consecutive
#  integers (not necessarily contiguous in the array).

# def sequence(arr):
#     map = {}
#     longest = 0
#     for i in arr:
#         map[i] = i - 1

#     for i in range(len(arr)):
#         if arr[i] - 1 not in map:
#             current = arr[i]
#             count = 1

#             while current + 1 in map:
#                 current = current + 1
#                 count += 1       

#             longest= max(longest,count)
#     return longest

# arr = [100, 4, 200, 1, 3, 2]
# print(sequence(arr))


# def sequence(arr):
#     numSet = set(arr)
#     longest = 0

#     for n in numSet:
#         if n - 1 not in numSet:
#             length = 1
#             current = n
#             while current +1 in numSet:
#                 current += 1
#                 length += 1
#             longest = max(longest , length)

#     return longest

# arr = [100, 4, 200, 1, 3, 2 ,5 ,6,7,8]
# print(sequence(arr))




#  7. Given an array of integers, find the element that appears more than n/2 times (you may
#  assume such an element always exists).

# def count(arr):
#         candidate = 0
#         counter = 0
#         for num in arr:
#             if counter == 0:
#                   candidate = num
#             if num == candidate:
#                   counter += 1
#             else:
#                   counter -= 1
#         return candidate


# arr = [3, 3, 4, 3, 2, 3, 3]
# print(count(arr))


# 8. Given an array of strings, group the strings that are anagrams of each other.

# def anagrams(arr):
#     map = {}
#     for s in arr:
#         key ="".join(sorted(s))
#         if key not in map:
#             map[key] = []
#         map[key].append(s)              
#     return list(map.values())

# arr=["eat", "tea", "tan", "ate", "nat", "bat"]
# print(anagrams(arr))


#  9. Given an array of integers, find all unique triplets [a,b,c] such that a + b + c = 0.


# def threeSum(arr):
#     arr.sorted()
#     result = []
#     for i in range(len(arr)):
#         if i > 0 and arr[i] == arr[i-1]:
#             continue
#         left = i + 1
#         right = len(arr) -1 
#         while left < right:
#             total = arr[i] + arr[left] + arr[right]
#             if total == 0:
#                 result.append([arr[i], arr[left], arr[right]])
#                 left += 1
#                 right -= 1
#                 while left < right and arr[left] == arr[left - 1]:
#                     left +=1
#                 while left < right and arr[right] == arr[right + 1]:
#                     right -= 1

#             elif total < 0:
#                 left += 1  
#             else:
#                 right -= 1 

# arr= [-1, 0, 1, 2, -1, -4]
# print(threeSum(arr))



# 10. Given an integer array, find the maximum value of (nums[i] - nums[j]) for i > j


# def difference(nums):
#     min_val= nums[0]
#     max_diff =nums[1] - nums[0]
#     for i in range(1,len(nums)):
#         max_diff= max(max_diff,nums[i] - min_val)
#         min_val = min(min_val,nums[i])

#     return max_diff
# nums = [10, 4, 8, 3, 15]
# print(difference(nums))
