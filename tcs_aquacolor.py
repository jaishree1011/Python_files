str = input("Enter string:")
label = int(input("Enter no:"))
count = 0
maxi = 0
for i in range(len(str)):
  if (i % label == 0):
    maxi = max(count, maxi)
    count = 0
  if (str[i] == 'a'):
    count += 1
if (count > maxi):
  maxi = count
print(maxi)
