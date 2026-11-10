def check_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False

nums = eval(input())
target = int(input())
print(check_sum(nums, target))

