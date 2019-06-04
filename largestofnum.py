x=list(map(int,input().split()))
a=x[0]
b=x[1]
c=x[2]
if a>b and a>c:
  print(a)
elif b>a and b>c:
  print(b)
else:
  print(c)
