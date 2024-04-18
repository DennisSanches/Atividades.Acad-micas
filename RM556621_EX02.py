# Solicitar o valor do carro ao usuário
valor_carro = float(input("Digite o valor do carro: R$ "))

# Calcular preço final com desconto à vista (20% de desconto)
preco_final_avista_com_desconto = valor_carro * 0.2

# Definir quantidade de parcelas e percentual de acréscimo
parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
percentuais_acrescimo = [0.03, 0.06, 0.09, 0.12, 0.15, 0.18, 0.21, 0.24, 0.27, 0.30]

# Exibir a tabela de parcelamento para ambos os casos (com e sem desconto)
print("Tabela de Parcelamento:")
print(
    "Parcelas\tPreço Final (c/ Desconto)\tValor da Parcela (c/ Desconto)\t "
    "Preço Final (s/ Desconto)\tValor da Parcela (s/ Desconto)")
print("---------------------------------------------------------------------------------------------------------------")

for i in range(len(parcelas)):
    qtd_parcelas = parcelas[i]
    percentual_acrescimo = percentuais_acrescimo[i]

    # Calcular preço final parcelado com desconto
    preco_final_parcelado_com_desconto = preco_final_avista_com_desconto * (1 + percentual_acrescimo)

    # Calcular valor da parcela com desconto
    valor_parcela_com_desconto = preco_final_parcelado_com_desconto / qtd_parcelas

    # Calcular preço final parcelado sem desconto
    preco_final_parcelado_sem_desconto = valor_carro * (1 + percentual_acrescimo)

    # Calcular valor da parcela sem desconto
    valor_parcela_sem_desconto = preco_final_parcelado_sem_desconto / qtd_parcelas

    # Exibir os resultados formatados na tabela
    print(
        f"{qtd_parcelas:2d}         | R$ {preco_final_parcelado_com_desconto:.2f}           "
        f"\t\t\t| R$ {valor_parcela_com_desconto:.2f}                 "
        f"\t\t| R$ {preco_final_parcelado_sem_desconto:.2f}          "
        f"\t\t| R$ {valor_parcela_sem_desconto:.2f}                  ")
