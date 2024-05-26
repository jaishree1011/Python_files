s=input()
result=""
for i in range(len(s)):
  if((s[i]>='A' and s[i]<='Z')) or ((s[i]>='a' and s[i]<='z')):
    result+=s[i]
print(result)