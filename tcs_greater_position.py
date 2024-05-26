arr = [7, 4, 8, 2, 9]
out = 0
max = -2**31
for i in range(len(arr)):
  if (arr[i] > max):
    max = arr[i]
    out += 1
print(out)
