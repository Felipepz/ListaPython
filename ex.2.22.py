# Crie um programa que solicite ao usuário digitar uma descrição do clima (ensolarado, chuvoso, nublado etc.) e utilize a estrutura match..case para imprimir uma sugestão de roupa adequada para o dia (por exemplo, óculos de sol para ensolarado, guarda-chuva para chuvoso etc.).



clima = input("Digite a descrição do clima (ensolarado, chuvoso, nublado, etc.): ")

match clima.lower():
    case "ensolarado":
        print("Sugestão de roupa: Óculos de sol e roupas leves.")
    case "chuvoso":
        print("Sugestão de roupa: Guarda-chuva e capa de chuva.")
    case "nublado":
        print("Sugestão de roupa: Casaco leve e guarda-chuva (caso chova).")
    case _:
        print("Não foi possível determinar uma sugestão de roupa para este clima.")
