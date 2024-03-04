#   Matrix multiplication 

m1 = int(input("m1: "))
n1 = int(input("n1: "))

m2 = int(input("m2: "))
n2 = int(input("n2: "))

print("Birinchi matritsa elementlarini kiriting:")
matrix1 = []
for i in range(m1):
    row = []
    for j in range(n1):
        element = float(input(f"Element [{i+1},{j+1}]: "))
        row.append(element)
    matrix1.append(row)

print("Ikkinchi matritsa elementlarini kiriting:")
matrix2 = []
for i in range(m2):
    row = []
    for j in range(n2):
        element = float(input(f"Element [{i+1},{j+1}]: "))
        row.append(element)
    matrix2.append(row)
if n1 != m2:
    print("Ushbu matritsalarni ko'paytirish mumkin emas.")
else:
    kopaytirilgan_matrix = [[0 for _ in range(n2)] for _ in range(m1)]
    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                kopaytirilgan_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    print("Ko'paytirilgan matritsa:")
    for row in kopaytirilgan_matrix:
        print(row)
