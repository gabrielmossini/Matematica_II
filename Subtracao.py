import numpy as np
#Valor dos vetores
X = [10,20, 5]
Y = [1, 2, 3]
Z = [1, 1, 1]

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