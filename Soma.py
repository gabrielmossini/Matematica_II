import numpy as np

X = [10,20, 5]
Y = [5, 7, 1]
Z = [1, 2, 8]

vetorA = np.array(X)
vetorB = np.array(Y)
vetorC = np.array(Z)

print("Vetor A:", vetorA)
print("Vetor B:", vetorB)
print("Vetor C:", vetorC)

vetor_ab = vetorA + vetorB
print("Adicao de dois vetores, A+B:", vetor_ab)

vetor_ac = vetorA + vetorC
print("Adicao de dois vetores, A+C:", vetor_ac)

vetor_bc = vetorB + vetorC
print("Adicao de dois vetores, B+C:", vetor_bc)