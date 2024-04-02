# Definindo as variáveis
nome_maquina = input("Digite o nome da máquina: ")
tempo_uso = int(input("Digite o tempo de uso (em anos): "))
ligado = bool(input("A máquina está ligada? (True/False): "))

# Exibindo os valores lidos e seus tipos
print(f"Nome da máquina: {nome_maquina} (Tipo: {type(nome_maquina)})")
print(f"Tempo de uso: {tempo_uso} anos (Tipo: {type(tempo_uso)})")
print(f"Ligado: {ligado} (Tipo: {type(ligado)})")