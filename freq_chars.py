s=input()
s=sorted(s)
dictt={}
for i in s:
  if i in dictt:
    dictt[i]+=1
  else:
    dictt[i]=1
for i in dictt:
  print(i+str(dictt[i]),end=" ")