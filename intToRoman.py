class Solution(object):
    def intToRoman(self, num):
        result=""
        if(num//1000>0):
            for i in range(0,num//1000):
                result+="M"
            num=num%1000
        if(num//900==1):
            result+="CM"
            num=num-900
        
        if(num//500>0):
            for i in range(0,num//500):
                result+="D"
            num=num%500
        if(num//400==1):
            result+="CD"
            num=num-400
        if(num//100>0):
            for i in range(0,num//100):
                result+="C"
            num=num%100
        if(num//90==1):
            result+="XC"
            num=num-90
        if(num//50>0):
            for i in range(0,num//50):
                result+="L"
            num=num%50
        if(num//40==1):
            result+="XL"
            num=num-40
        if(num//10>0):
            for i in range(0,num//10):
                result+="X"
            num=num%10
        if(num//9==1):
            result+="IX"
            num=num-9
        if(num//5>0):
            for i in range(0,num//5):
                result+="V"
            num=num%5
        if(num//4==1):
            result+="IV"
            num=num-4
        if(num>0):
            for i in range(0,num):
                result+="I"
        return result



objekat=Solution()

print(objekat.intToRoman(3))
print(objekat.intToRoman(58))
print(objekat.intToRoman(1994))
