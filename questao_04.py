# Programa para mostrar o dia da semana com base no número de 1 a 7
numero_dia = int(input("Digite um número de 1 a 7: "))

if numero_dia == 1:
    print("Domingo")
elif numero_dia == 2:
    print("Segunda-feira")
elif numero_dia == 3:
    print("Terça-feira")
elif numero_dia == 4:
    print("Quarta-feira")
elif numero_dia == 5:
    print("Quinta-feira")
elif numero_dia == 6:
    print("Sexta-feira")
elif numero_dia == 7:
    print("Sábado")
else:
    print("Número inválido. Digite um número entre 1 e 7.")