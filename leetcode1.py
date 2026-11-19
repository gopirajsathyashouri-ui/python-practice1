class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

result = Solution()

nums = eval(input())
target = int(input())

print(result.twoSum(nums, target))