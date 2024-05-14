import os

nome_arquivo = input("Digite o nome do arquivo que deseja excluir: ")

try:
    os.remove(nome_arquivo)
    print(f"O arquivo '{nome_arquivo}' foi excluído com sucesso.")
except FileNotFoundError:
    print("Arquivo não encontrado.")
except Exception as e:
    print("Ocorreu um erro ao excluir o arquivo:", e)
