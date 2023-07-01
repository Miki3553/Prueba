
class Solution(object):
    def canReach(self, arr, start) -> bool:
       i = arr[start]
       jump = 0
       while i != 0:
           jump += 1
           i = arr[start]
           if i + start <= len(arr):
               start += i
           else:
                start -= i
        #if i == 0:
           return True    

ob = Solution()
print(ob.canReach[[4,2,3,0,3,1,2], 0])
print(ob.jump)