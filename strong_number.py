def factorial(n):
  if (n == 0):
    return 1
  else:
    return (n) * factorial(n - 1)
inp=int(input())
org=inp
sum=0
while(inp>0):
  last=inp%10
  inp=inp//10
  factt=factorial(last)
  sum+=factt
if(sum==org):
  print("Strong")
else:
  print("Not Strong")
