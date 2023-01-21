# Binary and Bipolar sigmodial
import math
n=int(input("Enter the number of elements : "))
yin=0
for i in range(0,n):
  x=float(input("Enter the input x = "))
  w=float(input("Enter the weight w = "))
  yin=yin+x*w
b=float(input("Enter the bias b = "))
yin=yin+b
binary_sigmoidal=(1/(1+math.e**(-yin)))
print("Binary Sigmoidal = ", round(binary_sigmoidal,3))
bipolar_sigmoidal=(2/(1+(math.e**(-yin))))-1
print("Bipolar Sigmoidal = ", round(bipolar_sigmoidal,3))