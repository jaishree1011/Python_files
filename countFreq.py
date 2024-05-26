arr = [10, 5, 10, 15, 10, 5]
dictt = {}
for i in arr:
  if (i in dictt):
    dictt[i] += 1
  else:
    dictt[i] = 1
print(dictt)
