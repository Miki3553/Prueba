class Solution(object):
    def addBinary(self, a, b):
        a = input()
        b = input()
        c = ''
        extra = 0
        if len(a) > len(b):
            for i in range(len(a)-len(b)):
                b = '0' + b
        elif len(a) < len(b):
            for i in range(len(b)-len(a)):
                a = '0' + a       
        for i in range(1, len(a) + 1):
            i = -i
            if a[i] == b[i] == '1':
                if extra == 1:
                    c = '1' + c
                else:
                    c = '0' + c
                    extra = 1          
            elif a[i] == b[i] == '0':
                if extra == 1:
                    c = '1' + c
                    extra = 0
                else:
                    c = '0' + c  
            else:
                if extra == 1:
                    c = '0' + c
                else:
                    c = '1' + c
        if extra == 1:
            c = '1' + c
        return c
        
ob = Solution()
print (ob.addBinary(input,input))    