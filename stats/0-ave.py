#!/bin/python3

if __name__ == '__main__':
    
    n = input()
    nums = list(map(int, input().split()))
    
    mean = sum(nums)/len(nums)
    
    nums.sort()
    if len(nums)%2 == 0:
        median = (nums[len(nums)//2-1] + nums[len(nums)//2])/2
    else:
        median = nums[len(nums)//2-1]
    
    hist = dict()
    for x in nums:
        hist[x] = hist.get(x,0) + 1
        

    s = sorted(hist.items(),key = lambda x:(-x[1],x[0]))
    mode,occurances = s[0]
    
    print(round(mean,1))
    print(round(median,1))
    print(mode)
