import numpy as np

#Regra de Sarrus
# |a11 a12 a13| a11 a12|
# |a21 a22 a23| a21 a22|
# |a31 a32 a33| a31 a32|

print("\nPosições: ")
a11 = (int(input('Valor de a11:')))
a12 = (int(input('Valor de a12:')))
a13 = (int(input('Valor de a13:')))
a21 = (int(input('Valor de a21:')))
a22 = (int(input('Valor de a22:')))
a23 = (int(input('Valor de a23:')))
a31 = (int(input('Valor de a31:')))
a32 = (int(input('Valor de a32:')))
a33 = (int(input('Valor de a33:')))

def det3x3(m):
  return m[0][0] * m[1][1] - m[0][1] * m[1][0]

matrix = [
          [a11, a12, a13],
          [a21, a22, a23],
          [a31, a32, a33]
]

print("\nMatrix ")
for array in matrix: print(array)

print()

a,b,c = matrix[0]

efhi = [x[1:] for x in matrix[1:]]

dfgi = [x[::2]for x in matrix [1:]]

degh = [x[0:2]for x in matrix[1:]]

det = (
    a* det3x3(efhi)
    - b * det3x3(dfgi)
    + c * det3x3(degh)
)

print(f"Determinante da matrix seguindo a Regra de Sarrus é: {det}")
