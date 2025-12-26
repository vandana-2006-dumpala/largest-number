def twosum(nums,target):
        n = len(nums)
        for i in range(n):
            sum=nums[i]
            for j in range(i+1,n):
                if sum+nums[j]==target:
                    return[i,j]

nums = list(map(int, input().split()))
target = int(input())
print(twosum(nums, target))