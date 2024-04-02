# Import the Carro class from questao_07
from questao_07 import Carro

# Create an instance of Carro
meu_carro = Carro(nome="BMW IX", marca="BMW")

# Print the car's name and brand
print(f"Nome do carro: {meu_carro.get_nome()}")
print(f"Marca do carro: {meu_carro.get_marca()}")