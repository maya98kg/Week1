class Solution(object):
    def isPalindrome(self, x):
        backwards=0
        right_way=x
        if(x<0):
            return False
        while(x>0):
            backwards=backwards*10+(x%10)
            x=x//10
        if(right_way==backwards):
            return True
        return False

objekat=Solution()
number=int(input())
print(objekat.isPalindrome(number))
        