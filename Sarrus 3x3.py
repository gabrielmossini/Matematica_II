import numpy as np

# produto vetorial
# |a11 a12 a13|
# |a21 a22 a23|
# |a31 a32 a33|

#Regra de Sarrus
# |a11 a12 a13| a11 a12|
# |a21 a22 a23| a21 a22|
# |a31 a32 a33| a31 a32|

a11 = 2
a12 = 1
a13 = -1
a21 = 1
a22 = 3
a23 = -1
a31 = 5
a32 = -2
a33 = 10

def det2x2(m):
  return m[0][0] * m[1][1] - m[0][1] * m[1][0]

matrix = [
          [a11, a12, a13],
          [a21, a22, a23],
          [a31, a32, a33]
]

print("Matix: ")
for array in matrix: print(array)

print()

a,b,c = matrix[0]

efhi = [x[1:] for x in matrix[1:]]

dfgi = [x[::2]for x in matrix [1:]]

degh = [x[0:2]for x in matrix[1:]]

det = (
    a* det2x2(efhi)
    - b * det2x2(dfgi)
    + c * det2x2(degh)
)

print(f"Determinante da matrix seguindo a Regra de Sarrus é: {det}")