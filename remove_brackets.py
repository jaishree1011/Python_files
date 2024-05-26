s=input()
result=""
for i in range(len(s)):
  if(s[i]!='(' and s[i]!=')'):
    result+=s[i]
print(result)
  