
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

def palandrome(str):
    i = 0
    j = len(str) - 1

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1

        while i < j and not s[j].isalnum():
            j -= 1
            
        if str[i].lower() != str[j].lower() :
            return False
        i += 1
        j -= 1    
        
    return True
 

s = "A man, a plan, a canal: Panama"
print(palandrome(s))
