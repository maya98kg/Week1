class Solution(object):
    def numberOfMatches(self, n):
        br = 0
        while(n>1):
            br+=(n//2)
            if(n%2==0):
                n=n//2
            else:
                n=(n+1)//2
        return br
    

objekat=Solution()
print(objekat.numberOfMatches(14))

