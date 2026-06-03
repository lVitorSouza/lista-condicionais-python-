# Calcula idade e verifica voto

from datetime import datetime

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = datetime.now().year

idade = ano_atual - ano_nascimento

print("Idade:", idade)

if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar")