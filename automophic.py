inp=int(input())
org=inp
inp=inp%10
sq=org**2
org=sq%10
if(inp==org):
  print("Automorphic")
else:
  print("Not Automorphic")