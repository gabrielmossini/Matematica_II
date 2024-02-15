import numpy as np
#Valor dos vetores
K = (int(input('Valor de K:')))

x1 = int(input("\ndigite o número de X1: "))
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

#Definicao dos Vetores
A = np.array(X)
B = np.array(Y)
C = np.array(Z)

#Vetores
print("\nVETORES")
print("Vetor A:", A)
print("Vetor B:", B)
print("Vetor C:", C)

#CTE
print("\nRESULTADO DA MULTIPLICAÇÃO")
print("Multiplicacao por um CTE, K*A:", K * A)
print("Multiplicacao por um CTE, K*B:", K * B)
print("Multiplicacao por um CTE, K*C:", K * C)
