s = input()
s = sorted(s)
dictt = {}
count = 0
ans = ""
for i in s:
  if i in dictt:
    dictt[i] += 1
  else:
    dictt[i] = 1
  if (count < dictt[i]):
    count = dictt[i]
    ans = i
print(ans)
