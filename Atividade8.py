# Calcula aumento salarial

salario = float(input("Digite o salário: R$ "))

if salario <= 2000:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10

novo_salario = salario + aumento

print("Novo salário: R$", novo_salario)