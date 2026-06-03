# Aprovação de empréstimo

salario = float(input("Digite o salário: "))
parcela = float(input("Digite o valor da parcela: "))

if parcela <= salario * 0.30:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")