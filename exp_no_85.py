n=input()
s1,s2='',''
for i in range(0,len(n)):
  if i%2==0:
    s1+=n[i]
  else:
    s2+=n[i]
print(s1,s2)
