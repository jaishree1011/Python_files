input = 725648
result = 0
out = 1
while (input > 0):
  rem = input % 10
  result = result * 10 + rem
  out *= rem
  input = input // 10
print(out)
