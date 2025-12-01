#  1. Given an integer array, return a new array where each element at index i is the product of all numbers in the original array except nums[i], without using division

def newArray(arr):
    n = len(arr)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix 
        suffix *= arr[i]

    return result


arr=[1,4,5,6,7]
print(newArray(arr))