
##twosumII 

# def twosum(num,tar):
#     i = 0
#     j = len(num)-1
#     while i < j:
#         s= num[i] + num[j]
#         if s == tar:
#             return i,j
#         elif s < tar:
#             i +=1
#         else:
#             j-=1
#     return -1,-1
    
            
# num = [2,7,11,15]
# tar = 13
# print(twosum(num,tar))


# 2. Given a string, determine if it is a palindrome considering only alphanumeric characters and
# ignoring cases.

# def palandrome(str):
#     i = 0
#     j = len(str) - 1

#     while i < j:
#         while i < j and not s[i].isalnum():
#             i += 1

#         while i < j and not s[j].isalnum():
#             j -= 1
            
#         if str[i].lower() != str[j].lower() :
#             return False
#         i += 1
#         j -= 1    
        
#     return True
 

# s = "A man, a plan, a canal: Panama"
# print(palandrome(s))


#3. Given an array of integers sorted by absolute value, return a new array of their squares,
# also sorted.

# def squares(arr):
#     result = []

#     for i in arr:
#         result.append(i*i)
#     return result

# arr = [-1, 1, -2, 2, 3]
# print(squares(arr))

# 4. Given a sorted array, remove duplicates in-place and return the new length

# def duplicates(arr):
#     i=0
#     j=1
#     while j != len(arr):
#         if arr[i] == arr[j]:
#             arr.pop(j)
#         else:
#             i += 1
#             j +=1 

#     return arr

# arr = [1, 1, 2, 2, 2, 3]
# print(duplicates(arr))



# def duplicates(arr):
#     i= 0
#     for j in range(1,len(arr)):
#         if arr[j] != arr[i]:
#             i +=1
#             arr[i] = arr[j]
#     return i+1

# arr = [1, 1, 2, 2, 2, 3]
# print(duplicates(arr))


# 5. Given an array of integers, partition it so that all even numbers appear before all odd
# numbers using O(1) extra space.

# def evenodd(arr):
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         if arr[left] % 2 == 0: left +=1
#         elif arr[right] % 2 != 0: right -=1
#         else:
#             arr[left],arr[right] = arr[right],arr[left]
#             left +=1
#             right -=1
#     return arr
# arr = [3, 8, 5, 12, 7, 6, 4]
# print(evenodd(arr))


# 6. Given a string, reverse the order of vowels using two pointers.

# def vowels(str):
#     # vowels = {'a','e','i','o','u','A','E','I','O','U'}
#     vowels = set("aeiouAEIOU")
#     left = 0
#     right = len(str) - 1 

#     str = list(str)

#     while left < right:
#         if str[left] not in vowels:
#             left +=1
#         elif str[right] not in vowels:
#             right -=1
#         # if str[left] in vowels and str[right] in vowels:
#         else:
#             str[left],str[right] = str[right],str[left]
#             left += 1
#             right -= 1

#     return "".join(str)

# string = "hello"
# print(vowels(string))



# 7. Given two sorted arrays, merge them into one sorted array without using extra space beyond a
# few variables (assume one has extra capacity at the end).

# def extraSpace(arr1,arr2):
#     m = len(arr1) - len(arr2)
#     n = len(arr2)
#     i = m - 1
#     j = n - 1
#     k = m + n - 1

#     while j >= 0:
#         if i >= 0 and arr1[i] > arr2[j]:
#             arr1[k] = arr1[i]
#             i -= 1
#         else:
#             arr1[k] = arr2[j]
#             j -= 1
#         k -=1
#     return arr1

# arr1 = [1, 3, 5, 0, 0, 0]
# arr2 = [2, 4, 6]
# print(extraSpace(arr1,arr2))


# 8. Given a sorted array, find the closest pair of numbers whose sum is closest to a given
# target.

# def close(arr,tar):
#     left = 0
#     right = len(arr) - 1
#     clo = float("inf")
#     best_pair = None

#     while left < right:
#         add = arr[left] + arr[right]
#         comp = abs(tar - add)

#         if comp < clo:
#             clo = comp
#             best_pair = (arr[left],arr[right])

#         if add < tar:
#             left += 1
#         else:
#             right -= 1
        
#     return best_pair

# arr = [1, 3, 4, 7, 10]
# target = 15
# print(close(arr,target))


# 9. Given two sorted arrays, find the median of the combined data in O(log(min(n, m))) time

def combine(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1,nums2 = nums2,nums1

    n,m = len(nums1) , len(nums2)
    low , high = 0 ,n

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = (n + m +1) // 2 - cut1

        left1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
        right1 = float("-inf") if cut1 == n else nums1[cut1]

        left2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
        right2 = float("-inf") if cut2 == n else nums2[cut2]
        if left1 <= right2 and left2 <= right1:
            if (n+m)%2 == 0:
                return (max(left1,left2)+min(right1,right2)) /2
            else:
                return max(left1,left2)
        elif left1 > right2:
            high = cut1 - 1
        else:
            low =cut1 + 1
arr1=[1, 4, 7]
arr2=[2, 3, 6, 8]
print(combine(arr1,arr2))