
def asereje (array, minimum):
    array = array
    m = minimum
    higher = 0
    for index in range(len(array)):
        higher = max(higher, array[index])
    n = 0   
    for x in range(1, higher + 1):
        n = m * x
        for index in range(len(array)):
            if n == array[index]:
                return False
    return True

arrayObstacles = [15,10,22,12,13,16,18,21]
#respuesta deberia ser 7
check = False
minimumJump = 0
while check == False:
    minimumJump += 1
    check = asereje(arrayObstacles,minimumJump)

       
        
print('The minimum jump to avoid all the obstacles is: ', minimumJump)
    


