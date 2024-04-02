#Classe é uma estrutura que define um tipo de objeto, encapsulando dados (atributos) e comportamentos (métodos) relacionados a esse tipo
#Classes permitem organizar o código de forma estruturada, tornando-o mais legível e fácil de manter
#Uma vez criada, uma classe pode ser usada para criar múltiplos objetos, promovendo a reutilização de código
#Um paradigma de programação é um modelo ou estilo para resolver problemas de programação
#Python é multiparadigma. Ele suporta programação orientada a objetos, funcional e procedural
#A flexibilidade do Python permite que você escolha o paradigma mais adequado para cada tarefa

class Carro:
    def __init__(self, nome, marca):
        self._nome = nome
        self._marca = marca

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_marca(self):
        return self._marca

    def set_marca(self, nova_marca):
        self._marca = nova_marca

# Exemplo de uso:
meu_carro = Carro(nome="BMW IX", marca="BMW")
print(f"Nome do carro: {meu_carro.get_nome()}")
print(f"Marca do carro: {meu_carro.get_marca()}")