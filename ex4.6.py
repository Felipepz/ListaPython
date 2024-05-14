# Crie um programa que peça ao usuário para inserir dois números complexos e calcule a soma e o produto desses números.



print("Insira o primeiro número complexo:")
real1 = float(input("Parte real: "))
imag1 = float(input("Parte imaginária: "))

print("\nInsira o segundo número complexo:")
real2 = float(input("Parte real: "))
imag2 = float(input("Parte imaginária: "))

soma_real = real1 + real2
soma_imag = imag1 + imag2

prod_real = real1 * real2 - imag1 * imag2
prod_imag = real1 * imag2 + imag1 * real2

print("\nA soma dos números complexos é:", soma_real, "+", soma_imag, "i")

print("O produto dos números complexos é:", prod_real, "+", prod_imag, "i")
