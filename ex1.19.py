# Crie um programa que peça ao usuário para digitar o comprimento de dois lados de um triângulo retângulo. Em seguida, o programa deve calcular e mostrar o comprimento da hipotenusa.

 
cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
cateto2 = float(input("Digite o comprimento do segundo cateto: "))


hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5

print("O comprimento da hipotenusa é:", hipotenusa)
