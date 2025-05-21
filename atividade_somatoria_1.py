# Este projeto é uma aplicação simples em Python que ajuda o usuário a monitorar sua saúde com base no cálculo do IMC (Índice de Massa Corporal).

#Receber o peso e a altura do usuário, calcular o IMC e exibir:
#O valor calculado
#Uma mensagem de orientação baseada no resultado

nome = input("Olá tudo bem? Me informe seu nome por gentiliza:")

peso = float(input("Vamos calcular seu IMC, para isso me informe seu peso (kg):"))

altura = float(input("Agora sua altura (m) por gentileza:"))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print(f"Sr {nome} o seu IMC é: {IMC}, Abaixo do peso")
elif 18.5 <= IMC <= 24.9:
    print(f"Sr {nome} o seu IMC é: {IMC}, Peso Normal") 
elif 25.0 <= IMC <= 29.9:
    print(f"Sr {nome} o seu IMC é: {IMC}, Tudo OK👌, Mas fique atento pois o senhor está com sobrepeso")
elif 30.0 <= IMC <= 34.9:
    print(f"Sr {nome} o seu IMC é: {IMC}, Obesidade Grau 1, Cuidado com sua saúde ⚠️")
elif 35.0 <= IMC <= 39.9:
    print(f"Sr {nome} o seu IMC é: {IMC}, Obesidade Grau II. O senhor tem que se cuidar mais")
else:
    print(f"Sr {nome} o seu IMC é: {IMC}, Obesidade grau 3 (mórbida). O senhor precisa iniciar um tratamento imediatamente")