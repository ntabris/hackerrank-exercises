#!/bin/python3

if __name__ == '__main__':
    
    n = input()
    nums = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    
    mean = sum(nums[i] * weights[i] for i in range(len(nums))) / sum(weights)
        
    print(round(mean,1))
