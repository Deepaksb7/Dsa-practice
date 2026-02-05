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

# def flip(arr):
#     left = 0
#     zero_count = 0
#     max_len = 0
#     for right in range(len(arr)):
#         if arr[right] == 0:
#             zero_count += 1
        
#         while zero_count > 1:
#             if arr[left] == 0:
#                 zero_count -= 1
#             left += 1
#         max_len = max(max_len, right - left + 1)

#     return max_len
# arr = [1, 0, 1, 1, 0]
# print(flip(arr))


# 3. Given an array of integers and a number k, find the maximum sum of any contiguous subarray
# of size k

# def subarray(arr,k):
#     window_sum = sum(arr[:k])
#     max_sum = window_sum
#     for right in range(k,len(arr)):
#         window_sum += arr[right]
#         window_sum -= arr[right - k]
#         max_sum = max(max_sum,window_sum)
#     return max_sum
# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# print(subarray(arr,k))


# 4. Given a string s and string t, find the minimum window in s which contains all characters of
# t (including multiplicity)

def contains(s,t):
    if not s or not t:
        return ""
    
    from collections import Counter

    need = Counter(t)
    window = {}

    have = 0
    need_count = len(need)

    res = [-1,-1]
    res_len = float("inf")

    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char,0) + 1

        if char in need and window[char] == need[char]:
            have += 1

        while have == need_count:
            if (right - left + 1) < res_len:
                res = [left , right]
                res_len = right - left + 1


            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1

    left , right = res

    return s[left:right+1] if res_len != float("inf") else ""

s = "ADOBECODEBANC"
t = "ABC"
print(contains(s,t))

