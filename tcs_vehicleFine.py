arr = [2, 5, 1, 6, 8]
date = int(input("Enter date:"))
fine = 300
odd = 0
even = 0
for i in range(len(arr)):
  if (arr[i] % 2 == 0):
    even += 1
  else:
    odd += 1
if (date % 2 == 0):
  fine *= odd
else:
  fine *= even
print(fine)
