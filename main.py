
nums = [-1,0,1,2,-1,-4]
Sum = 0
triplet = []
window = []
i = 0
left = 0
right = 3
while i < right:
    window.append(nums[i])
    Sum += nums[i]
    if Sum == 0 and len(window) == 3:
        if sorted(window) not in triplet:
            triplet.append(sorted(window))
    i += 1
print(triplet)

print(i)
# while right < len(nums):
#     window.remove(nums[left])
#     window.append(nums[right])
#     if Sum == 0 and len(window) == 3:
#         if sorted(window) not in triplet:
#             triplet.append(sorted(window))
#     left = right - i  + 1
    


