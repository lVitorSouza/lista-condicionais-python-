# Classifica a temperatura

temp = float(input("Digite a temperatura em °C: "))

if temp < 18:
    print("Clima frio")
elif temp <= 28:
    print("Clima agradável")
else:
    print("Clima quente")