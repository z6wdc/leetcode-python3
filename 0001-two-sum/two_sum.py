class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            if target - nums[i] in numMap:
                return [ numMap.get(target - nums[i]), i]
            else:
                numMap[nums[i]] = i
