class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        inital = x
        reverse = 0
        
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        return reverse == inital
            

print(Solution.isPalindrome(121, 121))