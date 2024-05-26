inp = int(input("Enter the digit:"))
n = int(input("Enter number:"))
res = 0
sum = 0
mul = 0
while (inp > 0):
  rem = inp % 10
  res = rem * 10 + rem
  sum += rem
  inp = inp // 10
mul = sum * n
sum = 0
while (mul > 0):
  rem = mul % 10
  res = rem * 10 + rem
  sum += rem
  mul = mul // 10
print(sum)
