import numpy as np
i1= .05
i2= .10
t1=.01
t2=.99
b1=1
w1=.15
w2=.20
w3=.25
w5=.40
w6=.45
w7=.50
w8=.55
wb1=.35
wb2=.60

#forward pass
neth1=(i1*w1)+(i2*w2)+(b1*wb1)
print(neth1)
outh1=1/(1+(np.exp(-neth1)))
print(outh1)
neth2=(i1*w3)+(i2*w2)+(b1*wb1)
print(neth2)
outh2=1/(1+(np.exp(-neth2)))
print(outh2)

y1=(outh1*w5)+(outh2*w6)+(wb2)
print(y1)
outy1=1/(1+(np.exp(-y1)))
print(outy1)
y2=(outh2*w7)+(outh2*w8)+(wb2)
print(y2)
outy2=1/(1+(np.exp(-y2)))
print(outy2)

#error calculation
e1=1/2*((t1-outy1)**2)
print(e1)
e2=1/2*((t2-outy2)**2)
print(e2)
etotal = 1/2*((t1-outy1)**2)+1/2*((t2-outy2)**2)
print("Error calculation:", etotal)

#backword pass
a=-(t1-outy1)
print(a)
b=outy1*(1-outy1)
print(b)
c=outh1
print(c)
x=a*b*c
print("Backword pass value:", x)

w5=w5-0.5*x
print("w5 Adjesment value:", w5)