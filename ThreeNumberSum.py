def threeNumberSum(nums, targetSum):
    res = []
    nums = sorted(nums)
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r :
            s = nums[i] + nums[l] + nums[r]
            if s == targetSum:
                res.append([nums[i] ,nums[l] ,nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < targetSum :
                l += 1
            else:
                r -= 1
    return res


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
print(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))
