class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        p = 0
        q = len(x) - 1
        
        while p <= q:
            if x[p] != x[q]:
                return False
            p += 1
            q -= 1
        
        return True
        


print(Solution.isPalindrome(121, 121))