import numpy as np

x1 = int(input("digite o número de X1: "))
x2 = int(input("digite o número de X2: "))
x3 = int(input("digite o número de X3: "))

y1 = int(input("\ndigite o número de Y1: "))
y2 = int(input("digite o número de Y2: "))
y3 = int(input("digite o número de Y3: "))

z1 = int(input("\ndigite o número de Z1: "))
z2 = int(input("digite o número de Z2: "))
z3 = int(input("digite o número de Z3: "))


X = [x1, x2, x3]
Y = [y1, y2, y3]
Z = [z1, z2, z3]

A = np.array(X)
B = np.array(Y)
C = np.array(Z)

print("\nX:", X)
print("Y:", Y)
print("Z:", Z)

Escalar_AB = A.dot(B)
print("\nProduto Escalar A*B: ", Escalar_AB)

Escalar_BC = B.dot(C)
print("Produto Escalar B*C: ", Escalar_BC)

Escalar_AC = A.dot(C)
print("Produto Escalar A*C: ", Escalar_AC)