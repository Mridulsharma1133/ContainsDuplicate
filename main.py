nums = [0,1,0,3,12]
res = [0] * len(nums)

i = 0
for j in range(len(nums)):
    if (nums[j] == 0):
        continue
    else:
        res[i] = nums[j]
        i += 1

nums[:] = res
print(nums)