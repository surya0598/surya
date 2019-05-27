def evenodd(x):
  if x%2==0:
    return("Even")
  elif x%2!=0:
    return("Odd")
  else:
    print("Invalid")
x=int(input())
print(evenodd(x))
