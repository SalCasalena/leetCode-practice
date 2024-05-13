class Solution(object):
    def romanToInt(self, s):
        
        romanValues = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        length = len(s)
        
        if length < 2:
            return romanValues[s[0]]
        
        sum = 0
        temp = 0
        
        i = 1
        while (i < length):
            p = romanValues[s[i - 1]]
            c = romanValues[s[i]]
            temp += p
               
            if (c < p):
                sum += temp
                temp = 0
                
            elif (c > p): 
                sum -= temp
                temp = 0
                        
            i += 1
        sum += (temp + c)
        return sum

roman = "IVI"
print(Solution.romanToInt(roman, roman))