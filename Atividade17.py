# Cálculo de energia elétrica

tipo = input("Tipo de instalação (R, C ou I): ").upper()
consumo = float(input("Consumo em kWh: "))

if tipo == "R":
    valor = consumo * 0.60
elif tipo == "C":
    valor = consumo * 0.48
elif tipo == "I":
    valor = consumo * 0.55
else:
    valor = 0
    print("Tipo inválido")

if valor > 0:
    print("Valor da conta: R$", valor)