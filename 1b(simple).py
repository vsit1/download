#Simple neural net
n=int(input("Enter inputs : "))
yin=0
for i in range(n):
  x=float(input("Enter x: "))
  w=float(input("Enter Weight:"))
  yin=yin+x*w
if(yin<0):
  output = 0
elif(yin>1):
  output = 1
else:
  output = yin
print("Output = ",output)