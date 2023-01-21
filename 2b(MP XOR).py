# MP Neuron XOR
print("XOR function using M-P\n")
x1input=[1,1,0,0]
x2input=[1,0,1,0]
print("Calculating Z1 = x1*w11 + x2*w21")
print("Considering one weight as excitatory and other one as inhibitory.")
w11=[1,1,1,1]
w21=[-1,-1,-1,-1]
print("x1 ", " x2 "," z1")
z1=[]
for i in range(0,4):
    z1.append(x1input[i]*w11[i]+ x2input[i]*w21[i])
    print(x1input[i], " ", x2input[i], " ", z1[i])
w21=[-1,-1,-1,-1]
w22=[1,1,1,1]
print("x1 ", " x2 "," z2")
z2=[]
for i in range(0,4):
    z2.append(x1input[i]*w21[i]+ x2input[i]*w22[i])
    print(x1input[i], "", x2input[i], "", z2[i])
print("Applying threshold is equal to 1 for z1 and z2")
for i in range(0,4):
    if(z1[i]>=1):
        z1[i]=1
    else:
        z1[i]=0
    if(z2[i]>=1):
        z2[i]=1
    else:
        z2[i]=0
print("z1","z2")
for i in range(0,4):
    print(z1[i]," ",z2[i])
print("x1","x2","y")
y=[]
v1=1
v2=1
for i in range(0,4):
    y.append(z1[i]*v1 + z2[i]*v2)
    print(x1input[i]," ",x2input[i]," ",y[i])