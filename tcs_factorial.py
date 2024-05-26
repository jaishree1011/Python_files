def factorial(n):
  if (n == 0):
    return 1
  else:
    return (n) * factorial(n - 1)
inp = int(input("Enter no:"))
ans = 2
res = factorial(inp-1)
ans *= res
print(ans)
