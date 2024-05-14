# Escreva um programa que peça ao usuário para inserir uma faixa etária e, em seguida, utilize a estrutura match..case para sugerir um filme adequado para essa idade. Você pode categorizar as faixas etárias e sugerir diferentes tipos de filmes para cada categoria, como filmes infantis para crianças, ação para adolescentes, drama para adultos etc.




faixa_etaria = input("Digite a faixa etária (criança, adolescente, adulto): ")


match faixa_etaria.lower():
    case "criança":
        print("Sugestão de filme: Toy Story")
    case "adolescente":
        print("Sugestão de filme: Harry Potter e a Pedra Filosofal")
    case "adulto":
        print("Sugestão de filme: O Poderoso Chefão")
    case _:
        print("Faixa etária inválida")
