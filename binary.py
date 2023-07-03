class Solution(object):
    def addBinary(self, a, b):
        a = a
        b = b       
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
    def IntBinary(self, a):
        a = a
        j = 0
        conv = 0
        for i in range(0,len(a)):
            j = -(i+1)
            if a[j] == '1':
                conv = conv + 2**i
        return conv
        
ob = Solution()
a = input()
b = input()
print(ob.addBinary(a,b))   
print(ob.IntBinary(a))
print(ob.IntBinary(b))
print(ob.IntBinary(ob.addBinary(a,b))) 