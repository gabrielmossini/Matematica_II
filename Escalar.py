import numpy as np

X = [1, -1, 6]
Y = [2, 0, -1]
Z = [2, 2, 2]

A = np.array(X)
B = np.array(Y)
C = np.array(Z)

print("X:", X)
print("Y:", Y)
print("Z:", Z)

Escalar_AB = A.dot(B)
print("Produto Escalar A*B: ", Escalar_AB)

Escalar_BC = B.dot(C)
print("Produto Escalar B*C: ", Escalar_BC)

Escalar_AC = A.dot(C)
print("Produto Escalar A*C: ", Escalar_AC)