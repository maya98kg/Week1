class Solution(object):
    def singleNumber(self, nums):
        n=nums[0]
        for i in range(1,len(nums)):
            n=n^nums[i]
        return n

n=int(input())
list=[]
for i in range(0,n):
    list.append(int(input()))

objekat=Solution()
print(objekat.singleNumber(list))