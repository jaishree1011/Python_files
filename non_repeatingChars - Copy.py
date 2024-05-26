s = input()
out = {}
for i in s:
  if i in out:
    out[i] += 1
  else:
    out[i] = 1
for j in out:
  if (out[j] <= 1):
    print(j, end=",")
