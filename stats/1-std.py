#!/bin/python3

if __name__ == '__main__':
    
    n = int(input())
    nums = list(map(int, input().split()))
    
    mean = sum(nums)/len(nums)
    ssqr = sum((x-mean)**2 for x in nums)/len(nums)
    std = ssqr**(.5)
    print(round(std,1))