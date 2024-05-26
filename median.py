arr = [2,5,1,7]
n = len(arr)
arr = sorted(arr)
if(n%2==0):
  a=(n//2)-1
  b=n//2
  median=((arr[a]+arr[b])/2)
else:
  median = arr[n//2]
print(median)
