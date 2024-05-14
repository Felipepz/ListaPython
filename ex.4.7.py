# Crie um programa que peça ao usuário para digitar um nome de usuário e uma senha contendo apenas caracteres alfanuméricos e use uma expressão regular para fazer uma limpeza nos valores digitados, exibindo novamente para o usuário os valores processados.


import re

nome_usuario = input("Digite um nome de usuário: ")

senha = input("Digite uma senha: ")

padrao = re.compile(r'[^\w]')

nome_usuario_limpo = re.sub(padrao, '', nome_usuario)
senha_limpa = re.sub(padrao, '', senha)

print("\nNome de usuário processado:", nome_usuario_limpo)
print("Senha processada:", senha_limpa)
