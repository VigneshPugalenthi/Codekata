a,b=map(int,input().split())
for i in range(a+1,b):
  c=i
  s=0
  while i>0:
    d=i%10
    s+=d**3
    i=i//10
  if s==c:
    print(s,end=' ')
    
  
    
