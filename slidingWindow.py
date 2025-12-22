# 1. Given a string and an integer k, find the length of the longest substring with at most k
# distinct characters.

# def substring(s,k):
#     left = 0
#     maxLength = 0
#     char_count = {}
#     for right in range(len(s)):
#         char = s[right]
#         char_count[char] = char_count.get(char,0) + 1
        
#         while len(char_count) > k:
#             left_char =s[left]
#             char_count[left_char] -= 1

#             if char_count[left_char] == 0:
#                 del char_count[left_char]
#             left +=1

#         maxLength = max(maxLength,right - left +1)
#     return maxLength
# string = "eceba"
# k = 2
# print(substring(string,k))



# 2. Given a binary array, find the maximum number of consecutive 1s if you can flip at most one
# 0.

def flip(arr):
    left = 0
    zero_count = 0
    max_len = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            zero_count += 1
        
        while zero_count > 1:
            if arr[left] == 0:
                zero_count -= 1
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len
arr = [1, 0, 1, 1, 0]
print(flip(arr))

