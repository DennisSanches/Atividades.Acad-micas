dias_semana_escolhidos = []
contagem_max = 0
elementos_mais_repetidos = []
colaboradores_qtde = int(input("Quantos colaboradores irão participar da votação? \n"))
for i in range(1, colaboradores_qtde + 1):
    print(
        "Qual dia da semana é o melhor para realização das lives?"
        "\n1. Segunda-Feira\n2. Terça-Feira\n3. Quarta-Feira\n4. Quinta-feira\n5. Sexta-Feira\n")

    while True:  # Loop até obter uma entrada válida
        try:
            dia_semana = int(input("Digite o número correspondente ao dia: \n"))
            if dia_semana < 1 or dia_semana > 5:
                print("Por favor, digite um número válido entre 1 e 5.")
            else:
                break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Por favor, digite um número válido entre 1 e 5.")

    dias_semana_escolhidos.append(dia_semana)

for elemento in dias_semana_escolhidos:
    contagem_atual = dias_semana_escolhidos.count(elemento)
    if contagem_atual > contagem_max:
        contagem_max = contagem_atual
        elementos_mais_repetidos = [elemento]
    elif contagem_atual == contagem_max and elemento not in elementos_mais_repetidos:
        elementos_mais_repetidos.append(elemento)

print("Segundo a votação:")

if len(elementos_mais_repetidos) > 1:
    print("Os dias", end=" ")
    for idx, dia in enumerate(elementos_mais_repetidos):
        if dia == 1:
            print("Segunda-Feira", end="")
        elif dia == 2:
            print("Terça-Feira", end="")
        elif dia == 3:
            print("Quarta-Feira", end="")
        elif dia == 4:
            print("Quinta-Feira", end="")
        elif dia == 5:
            print("Sexta-Feira", end="")

        if idx < len(elementos_mais_repetidos) - 2:
            print(",", end="")
        elif idx == len(elementos_mais_repetidos) - 2:
            print(" e ", end="")

    print(" foram os mais votados!")
else:
    dia_escolhido = elementos_mais_repetidos[0]
    if dia_escolhido == 1:
        print("Segunda-Feira foi escolhida para realizar a live.")
    elif dia_escolhido == 2:
        print("Terça-Feira foi escolhida para realizar a live.")
    elif dia_escolhido == 3:
        print("Quarta-Feira foi escolhida para realizar a live.")
    elif dia_escolhido == 4:
        print("Quinta-Feira foi escolhida para realizar a live.")
    elif dia_escolhido == 5:
        print("Sexta-Feira foi escolhida para realizar a live.")
