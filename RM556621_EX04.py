# Solicitar entrada do usuário para tipo de investimento, valor resgatado e dias investidos
tipo = int(input("Digite o tipo de investimento (1 para CDB, 2 para LCI, 3 para LCA): "))
valor = float(input("Digite o valor a ser resgatado: R$ "))
dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

# Validar o tipo de investimento
if tipo == 1:  # CDB
    if dias <= 180:
        aliquota_ir = 0.225  # 22,5%
    elif dias <= 360:
        aliquota_ir = 0.20  # 20%
    elif dias <= 720:
        aliquota_ir = 0.175  # 17,5%
    else:
        aliquota_ir = 0.15  # 15%
    imposto_renda = valor * aliquota_ir
    print(f"Imposto de Renda a ser pago: R$ {imposto_renda:.2f}")
elif tipo == 2 or tipo == 3:  # LCI ou LCA (isentos de IR)
    print("Investimento isento de Imposto de Renda.")
else:
    print("Tipo de investimento inválido.")
