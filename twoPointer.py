
##twosumII 

def twosum(num,tar):
    i = 0
    j = len(num)-1
    while i < j:
        s= num[i] + num[j]
        if s == tar:
            return i,j
        elif s < tar:
            i +=1
        else:
            j-=1
    return -1,-1
    
            
num = [2,7,11,15]
tar = 13
print(twosum(num,tar))