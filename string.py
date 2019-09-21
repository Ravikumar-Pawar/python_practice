#print(sum(sorted(list(map(int, input().split())))[-3:]))
n=int(input('target'))
nums=list(map(int,input().split()))
list1=[]
print(nums)
print(len(nums))
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j]==n:
            print(i,j)