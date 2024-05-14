def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo:", e)

ler_arquivo("arquivo.txt")

ler_arquivo("arquivo_inexistente.txt")
