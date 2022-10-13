class Solution(object):
    def maxArea(self, height):
        max=0
        for l in range(0,len(height)):
            for r in range(l+1,len(height)):
                if(max<(r-l)*(min(height[l],height[r]))):
                    max=(r-l)*(min(height[l],height[r]))
        return max

objekat=Solution()
height=[]
n=int(input())
for i in range(0,n):
    height.append(int(input()))
print(objekat.maxArea(height))