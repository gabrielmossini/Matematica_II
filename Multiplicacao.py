import numpy as np
#Valor dos vetores
K = (int(input('Valor de K:')))

X = [1, 2, 3]
Y = [4, 5, 6]
Z = [-7, -8, -9]

#Definicao dos Vetores
A = np.array(X)
B = np.array(Y)
C = np.array(Z)

#Vetores
print("Vetor A:", A)
print("Vetor B:", B)
print("Vetor C:", C)

#CTE
print("\nMultiplicacao por um CTE, K*A:", K * A)
print("Multiplicacao por um CTE, K*B:", K * B)
print("Multiplicacao por um CTE, K*C:", K * C)
