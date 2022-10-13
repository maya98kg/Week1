class Solution(object):
    def containsDuplicate(self, nums):
        mySet=set(nums)
        if(len(nums)>len(mySet)):
            return True
        return False

objekat=Solution()
n=int(input())
list=[]
for i in range(0,n):
    list.append(int(input()))
print(objekat.containsDuplicate(list))