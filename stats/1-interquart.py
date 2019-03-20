def median(nums):
    if len(nums)%2 == 0:
        med = (nums[len(nums)//2-1] + nums[len(nums)//2])/2.
    else:
        med = nums[len(nums)//2]
    return med
    

if __name__ == '__main__':
    
    n = int(input())
    ns = list(map(int, input().split()))
    freq = list(map(int, input().split()))
    
    nums = []
    for i in range(len(freq)):
        nums.extend([ns[i]]*freq[i])
    
    nums.sort()
    n = len(nums)
    
    med = median(nums)
    
    q = int((n-1)/2) if n%2==1 else int(n/2)
    
    left = nums[:q]
    right = nums[-q:]
    
    print(float(round(median(right)-median(left),1)))
    