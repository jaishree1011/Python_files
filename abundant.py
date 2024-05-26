inp=int(input())
org=inp
sum=0
for i in range(1,inp):
  if(inp%i==0):
    sum+=i
if(sum>org):
  print("Abundant")
else:
  print("Not Abundant")
