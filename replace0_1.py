num = int(input("Enter number : "))
string=str(num)
repl=[]
for i in string:
  if(i=='0'):
    repl.append('1')
  else:
    repl.append(i)
stri=""
for i in repl:
  stri+=i
print(int(stri))
  