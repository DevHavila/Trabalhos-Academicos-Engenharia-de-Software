print("Calculo de IMCs\n")
peso = float(input("Qual o ser Peso: "))
altura = float(input("Qual a sua Altura: "))

IMC = peso / (altura ** 2.0)

print(f'Resultado do IMC: {IMC:.2f}\n')

if IMC < 18.5:
    print("Estado: Magreza")
elif IMC < 24.9:
    print("Estado: Normal")
elif IMC < 29.9:
    print("Estado: Sobrepeso")
elif IMC < 34.9:
    print("Estado: Obesidade grau I")
elif IMC < 39.9:
    print("Estado: Obesidade grau II")
elif IMC < 40:
    print("Estado: Obesidade grau III")            