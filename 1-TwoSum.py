class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        x = nums
        for i in range(len(x)):
            for j in range(len(x)):
                if (i == j):
                    continue
                elif target == x[i]+x[j]:
                    return [i,j]
