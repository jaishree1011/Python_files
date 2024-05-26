arr=[8,0,9,11,0,4,0,7]
j=0
arr1=[]
for i in range(len(arr)):
  if(arr[i]==0):
    j+=1
  else:
    arr1.append(arr[i])
for i in range(j):
  arr1.append(0)
print(arr1)
