s=input()
result=""
for i in range(len(s)):
  if(s[i]!='a' and s[i]!='e' and s[i]!='i' and s[i]!='o' and s[i]!="u"):
    result+=s[i]
print(result)