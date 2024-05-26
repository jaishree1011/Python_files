s=input()
out=""
for i in range(len(s)):
  if s[i] not in out:
    out+=s[i]
print(out)