n=input()
i="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
s=""
for x in n:
  if x in i:
    print("Alphabet")
  else:
    print("No")
