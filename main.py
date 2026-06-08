nums = [2,2,3,1]
nums = set(nums)
if len(nums) < 3: 
    print(min(nums))

else:
    nums.remove(max(nums))
    nums.remove(max(nums))
    print(max(nums))