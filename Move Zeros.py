class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        n = len(nums) - j
        for i in range(n):
            nums[j] = 0
            j+=1
        return nums