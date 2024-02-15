import numpy as np
#Valor dos vetores
(print('Subtração 3x3'))
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

#Definicao dos Vetores
vetorA = np.array(X)
vetorB = np.array(Y)
vetorC = np.array(Z)

#Vetores
print("Vetor A: ", vetorA)
print("Vetor B: ", vetorB)
print("Vetor C: ", vetorC)

vetor_ab = vetorA - vetorB
print("Subtracao de dois vetores, A-B:", vetor_ab)

vetor_ac = vetorA - vetorC
print("Subtracao de dois vetores, A-C:", vetor_ac)

vetor_bc = vetorB - vetorC
print("Subtracao de dois vetores, B-C:", vetor_bc)