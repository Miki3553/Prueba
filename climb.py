class Solution(object):
    def climbStairs(self, n):
        a = []
        b = 0
        if n >= 1 and n <= 45:
            for i in range(n):
                b += 1
                if i <= 1:
                    a.append(i+1)
                else:   
                    a.append(a[i-1]+a[i-2])   
            return a[b-1]
        else:
            e = "Can't climb"  
            return e  
climb = Solution()
print(climb.climbStairs(int(input())))