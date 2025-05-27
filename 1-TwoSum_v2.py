class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash_map = {}   # dictionary
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map and hash_map[complement] != i:
                return [i,hash_map[complement]]
        return []
        
