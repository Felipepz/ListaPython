nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        num_linhas = sum(1 for linha in arquivo)
        print(f"O arquivo possui {num_linhas} linhas.")
except FileNotFoundError:
    print("Arquivo não encontrado.")
except Exception as e:
    print("Ocorreu um erro:", e)
