import math

#Módulo de um vetor
#v=(x1, y1) // Definição de Valores
X = float(input('Entre com o valor de X: '))
Y = float(input('Entre com o valor de Y: '))

#|v|√=x²+y² // Pitágoras
V = (X ** 2 + Y ** 2)

print("\nO resultado do modulo de é: |v| = ","√",V)

num = float(V)
raiz = math.sqrt(num)

print("\nA Raiz Quadrada é:", raiz)