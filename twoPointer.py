
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



def duplicates(arr):
    i= 0
    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            i +=1
            arr[i] = arr[j]
    return i+1

arr = [1, 1, 2, 2, 2, 3]
print(duplicates(arr))