def majorityElement(nums):
        frequencies = {}
        res = []
        for num in nums:
            frequencies[num] = 0
        for num in nums:
            frequencies[num] += 1
        for num in frequencies:
            if frequencies[num] > (len(nums)//3):
                res.append(num)
        return res        


print(majorityElement([3,2,3]))

"dqefas"