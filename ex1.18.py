
# Crie um programa que peça ao usuário para digitar o valor da medida de um ângulo em radianos. Em seguida, o programa deve calcular e mostrar o valor desse ângulo em graus.
 
angulo_radianos = float(input("Digite o valor do ângulo em radianos: "))

angulo_graus = angulo_radianos * (180 / 3.14159)

print("O ângulo em graus é:", angulo_graus)
