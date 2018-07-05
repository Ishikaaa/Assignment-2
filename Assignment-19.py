#Q1.
import numpy as np
a=np.random.rand(10,1)
print(a)
print("Mean =",np.mean(a))

#Q2.
import numpy as np
a=np.random.rand(20,1)
print(a)
print("Variance =",a.var())
print("Standard Deviation =",a.std())

#Q3.
import numpy as np
A=np.random.rand(10,20)
B=np.random.rand(20,25)
C=np.dot(A,B)
print("Multiplication of matrix A and matrix B,i.e., matrix C =",C)
print("Shape of C matrix =",C.shape)
print("Sum of all elements of matrix C =",np.sum(C))

#Q4.
import numpy as np
def f(i):
    return( 1 / (1 +( np.exp(-i))))
A=np.random.rand(10,1)
print("Original array =",A)
B=f(A)
print("New array =",B)
