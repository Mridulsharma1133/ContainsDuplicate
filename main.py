nums = [5]
k = 1
Sum = 0
maxAvg = 0

if (len(nums) == 1):
    print(nums[0]/k)

for i in range(k):
    Sum += nums[i]

avg = Sum/k
maxAvg = max(maxAvg, avg)
i = 0
for j in range(k, len(nums)):
    Sum += nums[j] - nums[j - k]
    avg = Sum / k
    maxAvg = max(maxAvg, avg)
print(maxAvg)
    
