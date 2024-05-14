# Implemente um generator chamado "pega_palavras" que receba um texto e retorne, a cada iteração, uma palavra desse texto (considerando que as palavras são separadas por espaço). Teste seu generator com uma frase à sua escolha.


def pega_palavras(texto):
    palavras = texto.split()
    for palavra in palavras:
        yield palavra

frase = "Python é uma linguagem de programação boa"
gerador = pega_palavras(frase)

for palavra in gerador:
    print(palavra)
