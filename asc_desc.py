arr = [9,6,1,2,4,11,17]
arr = sorted(arr)
mid = len(arr) // 2
temp = 0
for i in range(mid, len(arr)):
  for j in range(i + 1, len(arr)):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
print(arr)
