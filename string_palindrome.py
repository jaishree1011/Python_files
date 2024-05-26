s=input()
s=s.lower()
for i in range(0,len(s)//2):
  if(s[i]!=s[len(s)-i-1]):
    print("No")
    break
  else:
    print("Yes")
  
  