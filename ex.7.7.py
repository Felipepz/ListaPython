import os

nome_diretorio = "temp"

try:
    os.makedirs(nome_diretorio)

    caminho_arquivo = os.path.join(nome_diretorio, "temp.txt")

    with open(caminho_arquivo, 'w'):
        pass  

    print(f"Diretório '{nome_diretorio}' e arquivo 'temp.txt' criados com sucesso.")
except FileExistsError:
    print(f"Diretório '{nome_diretorio}' já existe.")
except Exception as e:
    print("Ocorreu um erro ao criar o diretório e o arquivo:", e)
