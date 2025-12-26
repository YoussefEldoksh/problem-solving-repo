
def maxArea(height):
    low = 0
    high = len(height)-1
    currentArea = 0
    maxArea = 0
    while low < high:
        currentArea = (high - low) * min(height[low], height[high])
        maxArea = max(maxArea, currentArea)
        # try to remove short lengths
        if height[low] < height[high]:
            low += 1
        else:
            high -= 1

    print(f"'low': {low} 'high': {high}")
    return maxArea

height = [2,3,4,5,18,17,6]

print(maxArea(height))


