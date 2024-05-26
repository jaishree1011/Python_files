start = "tue"
n = 20
dictt = {"mon": 6, "tue": 5, "wed": 4, "thu": 3, "fri": 2, "sat": 1, "sun": 0}
out = 0
if ((n - dictt[start[:3]]) >= 1):
  out = 1 + (n - dictt[start[:3]]) // 7
print(out)
