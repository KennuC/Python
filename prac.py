arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxN = 0
sumN = 0
l = r = 0 

# while l < len(arr) and r < len(arr):
#     sumN = sum(arr[l:r])
#     print(arr[l], sumN)
#     l +=1

for i in range(len(arr)):
    sumN = sum(arr[i:len(arr)])
    print(sumN)
    