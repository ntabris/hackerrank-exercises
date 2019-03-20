import math

def next_permutation(s):
    # find tail: longest sequence of ascending items from end
    tail = len(s) - 1
    while tail > 0 and s[tail-1] >= s[tail]:
        tail -= 1
    # if tail is whole array, then we're already on final permutation
    if tail == 0:
        return False
    # otherwise, swap item before tail with next larger item from tail
    ins = s[tail-1]
    t = len(s)-1
    while s[t] <= ins:
        t -= 1
    ext = s[t]
    s[tail-1],s[t] = ext,ins
    # reverse order of tail
    t = len(s)-1
    for i in range((t-tail)//2+1):
        s[tail+i],s[t-i] = s[t-i],s[tail+i]
    return True
       
    

if __name__ == "__main__":
    a = [1,2,3,4,5]
    i = 0
    print(a)
    while next_permutation(a):
        print(a)
        i+=1
