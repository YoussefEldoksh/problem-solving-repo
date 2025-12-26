

def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    A = 0
    for i in range(len(boxTypes)):
        if truckSize == 0:
            break
        if boxTypes[i][0] <= truckSize:
            A += boxTypes[i][0] * boxTypes[i][1]
            truckSize -= boxTypes[i][0]
        elif boxTypes[i][0] > truckSize:
            A+= truckSize * boxTypes[i][1]
            truckSize = boxTypes[i][0]-truckSize
            break
    return A
            

boxTypes = [[1,3],[2,2],[3,1]]


print(maximumUnits(boxTypes,4))