def median(nums):
    if len(nums)%2 == 0:
        med = int((nums[len(nums)//2-1] + nums[len(nums)//2])/2)
    else:
        med = nums[len(nums)//2]
    return med
    

if __name__ == '__main__':
    
    n = int(input())
    nums = list(map(int, input().split()))
    n = len(nums)
    
    nums.sort()
    
    
    med = median(nums)
    
    q = int((n-1)/2) if n%2==1 else int(n/2)
    
    left = nums[:q]
    right = nums[-q:]
    
    
    print(median(left))
    print(med)
    print(median(right))
    