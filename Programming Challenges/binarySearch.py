from random import randint
#algorithm for binary search
def valueExists(items, targetValue,leftPtr, rightPtr):
    while (leftPtr <= rightPtr):
        midPoint = int((rightPtr + leftPtr)/2)
        if items[midPoint] == targetValue:
            return True
        elif (items[midPoint] < targetValue):
            leftPtr = midPoint+1
        else:
            rightPtr = midPoint -1
    return False

randomArray = [randint(1,1000) for i in range(400)]
randomArray.sort()

print(randomArray)
print(valueExists(randomArray, 68, 0, len(randomArray)-1))
