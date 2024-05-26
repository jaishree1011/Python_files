binary = int(input())
decimal = 0
i = 0
while (binary != 0):
  rem = binary % 10
  decimal = decimal + rem * pow(2, i)
  binary = binary // 10
  i += 1
print(decimal)
