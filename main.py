nums = [1,2,3,1]
k = 3
indxObj = {}

for i in range(len(nums)):
    if (nums[i] in indxObj):
        indxObj[nums[i]].append(i)
    else:
        indxObj[nums[i]] = [i]

for indices in indxObj.values():
    for i in range(len(indices) - 1):
        if (indices[i + 1] - indices[i] <= k):
            print("True")
    


        

    