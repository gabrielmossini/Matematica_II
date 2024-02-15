import numpy as np
import math
import os

print("Math II.")
print("Program for Vector Implementation I.")
print("**Program not entirely translated.**")
print("Gabriel Mossini - CC/2.\n")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("Menu")
    print("1. Vector Module")
    print("2. Vector Addition")
    print("3. Vector Subtraction")
    print("4. Rule of Sarrus")
    print("5. Scalar Multiplication")
    print("6. Vector Multiplication")
    option = input("\nWhat's the programming language you want to learn? \nSelect an Option (1-7) or 0 to exit. ")
    
    if option == "1":
        clear()
        print("Vector Module")
        print("v=(x1, y1)")
        while True:
            try:
                X = float(input('\nInput the value of X: '))
                Y = float(input('Input the value of Y: '))
                break
            except ValueError:
                print ("Invalid input. Please enter a valid number.")

        print("\n|v|√=x²+y²")
        V = (X ** 2 + Y ** 2)

        print("\nThe output is: |v| = ","√",V)

        num = float(V)
        raiz = math.sqrt(num)

        print("\nSquare Root:", raiz)
        
    elif option == "2":
        clear()
        print('Vector Addition 3x3')
        while True:
            try:
                x1 = int(input("Input the number of X1: "))
                x2 = int(input("Input the number of X2: "))
                x3 = int(input("Input the number of X3: "))

                y1 = int(input("\nInput the number of Y1: "))
                y2 = int(input("Input the number of Y2: "))
                y3 = int(input("Input the number of Y3: "))

                z1 = int(input("\nInput the number of Z1: "))
                z2 = int(input("Input the number of Z2: "))
                z3 = int(input("Input the number of Z3: "))
                break
            except ValueError:
                print ("Invalid input. Please enter a valid number.")


        X = [x1, x2, x3]
        Y = [y1, y2, y3]
        Z = [z1, z2, z3]

        vetorA = np.array(X)
        vetorB = np.array(Y)
        vetorC = np.array(Z)

        print("\nVetor A:", vetorA)
        print("Vetor B:", vetorB)
        print("Vetor C:", vetorC)

        vetor_ab = vetorA + vetorB
        print("\nA+B:", vetor_ab)

        vetor_ac = vetorA + vetorC
        print("A+C:", vetor_ac)

        vetor_bc = vetorB + vetorC
        print("B+C:", vetor_bc)
    
    elif option == "3":
        clear()
        print("Vector Subtraction")
        while True:
            try:
                x1 = int(input("Input the value of X1: "))
                x2 = int(input("Input the value of X2: "))
                x3 = int(input("Input the value of X3: "))

                y1 = int(input("\nInput the value of Y1: "))
                y2 = int(input("Input the value of Y2: "))
                y3 = int(input("Input the value of Y3: "))

                z1 = int(input("\nInput the value of Z1: "))
                z2 = int(input("Input the value of Z2: "))
                z3 = int(input("Input the value of Z3: "))
                break
            except ValueError:
                print ("Invalid input. Please enter a valid number.")

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
        print("A-B:", vetor_ab)

        vetor_ac = vetorA - vetorC
        print("A-C:", vetor_ac)

        vetor_bc = vetorB - vetorC
        print("B-C:", vetor_bc)

    elif option == "4":
        clear()
        print("Rule of Sarrus")
        print("\n|a11 a12 a13| a11 a12|")
        print("|a21 a22 a23| a21 a22|")
        print("|a31 a32 a33| a31 a32|") 

        print("\nPositions: ")
        while True:
            try:
                a11 = (int(input('Value in a11: ')))
                a12 = (int(input('Value in a12: ')))
                a13 = (int(input('Value in a13: ')))
                a21 = (int(input('\nValue in a21: ')))
                a22 = (int(input('Value in a22: ')))
                a23 = (int(input('Value in a23: ')))
                a31 = (int(input('\nValue in a31: ')))
                a32 = (int(input('Value in a32: ')))
                a33 = (int(input('Value in a33: ')))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

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
    
    elif option == "5":
        clear()
        print("Scalar Multiplication")
        while True:
            try:
                x1 = int(input("\nInput the value of X1: "))
                x2 = int(input("Input the value of X2: "))
                x3 = int(input("Input the value of X3: "))

                y1 = int(input("\nInput the value of Y1: "))
                y2 = int(input("Input the value of Y2: "))
                y3 = int(input("Input the value of Y3: "))

                z1 = int(input("\nInput the value of Z1: "))
                z2 = int(input("Input the value of Z2: "))
                z3 = int(input("Input the value of Z3: "))
                break
            except ValueError:
                print ("Invalid input. Please enter a valid number.")
        
        
        X = [x1, x2, x3]
        Y = [y1, y2, y3]
        Z = [z1, z2, z3]
        
        A = np.array(X)
        B = np.array(Y)
        C = np.array(Z)
        
        print("\nX:", X)
        print("Y:", Y)
        print("Z:", Z)
        
        Escalar_AB = A.dot(B)
        print("\nProduto Escalar, A*B: ", Escalar_AB)
        
        Escalar_BC = B.dot(C)
        print("Produto Escalar, B*C: ", Escalar_BC)
        
        Escalar_AC = A.dot(C)
        print("Produto Escalar, A*C: ", Escalar_AC)

    elif option == "6":
        clear()
        print("Vector Multiplication")
        
        while True:
            try:
                K = (int(input('\nValue for K:')))
                
                x1 = int(input("\nInput the value of X1: "))
                x2 = int(input("Input the value of X2: "))
                x3 = int(input("Input the value of X3: "))
                
                y1 = int(input("\nInput the value of Y1: "))
                y2 = int(input("Input the value of Y2: "))
                y3 = int(input("Input the value of Y3: "))
                
                z1 = int(input("\nInput the value of Z1: "))
                z2 = int(input("Input the value of Z2: "))
                z3 = int(input("Input the value of Z3: "))
                break
            except ValueError:
                print ("Invalid input. Please enter a valid number.")


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
    

    elif option == "0":
        print ("\n\nThanks for using my Program!!\n\n")
        break;

    else:
        print ("Invalid Option!!!")
    input("Press ENTER to continue...")
    clear()