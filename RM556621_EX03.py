# Solicitar o valor da dívida ao usuário
valor_divida = float(input("Digite o valor da dívida: R$ "))

# Definir a tabela de quantidade de parcelas e percentuais de juros
parcelas_juros = {
    1: 0,
    3: 0.1,
    6: 0.15,
    9: 0.2,
    12: 0.25
}

# Exibir a tabela com os dados da dívida, juros, parcelas e valor da parcela
print("Tabela de Pagamento:")
print("Valor da Dívida | Juros (%) | Quantidade de Parcelas | Valor da Parcela")
print("-----------------------------------------------------------------------")

for parcelas, percentual_juros in parcelas_juros.items():
    valor_juros = valor_divida * percentual_juros
    valor_total_divida = valor_divida + valor_juros
    valor_parcela = valor_total_divida / parcelas

    print(
        f"R$ {valor_total_divida:.2f}        |   {percentual_juros * 100:.0f}%     |    {parcelas} parcelas   "
        f"       |    R$ {valor_parcela:.2f}")
