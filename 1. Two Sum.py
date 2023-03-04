# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """


    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if target == (nums[i]+nums[j]):
                return [i,j]

print(twoSum([2, 7, 11, 15],9))

print(twoSum([3,2,4],6))

