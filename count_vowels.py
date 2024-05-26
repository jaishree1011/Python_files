s = input()
s = s.lower()
vowels = 0
consonants = 0
space = 0
for i in range(len(s)):
  if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
    vowels += 1
  elif (s[i] == ' '):
    space += 1
  else:
    consonants += 1
print(vowels)
print(consonants)
print(space)
