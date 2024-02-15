import numpy as np

print("Defina o produto vetorial de uXv e vXu")
print("\nPosições: ")
u11 = (int(input('Valor de u11:')))
u12 = (int(input('Valor de u12:')))
u13 = (int(input('Valor de u13:')))
v21 = (int(input('\nValor de v21:')))
v22 = (int(input('Valor de v22:')))
v23 = (int(input('Valor de v23:')))

u = [u11, u12, u13]
v = [v21, v22, v23]

prod_uXv = np.cross(u, v)

print("\nu•uXv")
pendu = u * prod_uXv
print("Resultado:", prod_uXv)
print("Perpendicular:", pendu)

print("\nv•vXu")
pendv = v * prod_uXv
print("Resultado:", prod_uXv)
print("Perpendicular:", pendv)
