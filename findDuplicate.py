class Solution(object):
    def findDuplicate(self, nums):
        n=1
        for i in range(2,len(nums)):
            n=n^i
        pom=nums[0]
        for i in range(1,len(nums)):
            pom=pom^nums[i]
        return n^pom


n1=int(input())
nums=[]
for i in range(0,n1+1):
    nums.append(int(input()))

objekat=Solution()
print(objekat.findDuplicate(nums))

            