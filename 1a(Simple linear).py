# Simple linear neural Network
x=float(input("Enter the input x = "))
w=float(input("Enter the weight w = "))
b=float(input("Enter the bias b = "))
yin=(b+x*w)
print("The value of yin is ",yin)
if(yin<0):
  output = 0
elif(yin>1):
  output = 1
else:
  output = yin
print("Output = ",output)
print(yin)