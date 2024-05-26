s=input()
out={}
for i in range(len(s)):
  if s[i] not in out:
   out[s[i]]=1
  else:
    out[s[i]]+=1
for key,value in out.items():
  print(key,"-",value)