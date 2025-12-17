# Classe mãe

class Veiculo:
    def __init__(self, marca, ano, cor):
        self.marca = marca # Atributo público
        self._cor = cor  # Atributo protegido
        self.__ano = ano # Atributo privado
    @property
    def ano(self):
        #retornar o ano do veículo (getter)
        return self.__ano
    #setter atributo privado
    @ano.setter
    def ano(self, novo_ano):
        try:
            if novo_ano > 1886:
                self.__ano = novo_ano
                print("Ano atualizado para:", self.__ano)
            else:
                raise ValueError("Ano inválido para um veículo.")
        except ValueError as e:
                print(e)
                
    def exibir_info(self):
        print("Marca: ", self.marca, "Cor: ", self._cor, "Ano: ", self.__ano)

# Classe filha
class Carro(Veiculo):
    def __init__(self, marca, ano, cor, modelo):
        super().__init__(marca, ano, cor)
        self.modelo = modelo # Atributo público da classe filha

    def exibir_info(self):
        print("Marca: ", self.marca, "Modelo: ", self.modelo, "Cor: ", self._cor, "Ano: ", self.ano)
            
class Moto(Veiculo):
    def __init__(self, marca, ano, cor, tipo):
        super().__init__(marca, ano, cor)
        self.tipo = tipo # Atributo público da classe filha
        
    def exibir_info(self):
        print("Marca: ", self.marca, "Tipo: ", self.tipo, "Cor: ", self._cor, "Ano: ", self.ano)
        
veiculo1 = Veiculo("Toyota", 2020, "Branco")
carro1 = Carro("Honda", 2019, "Preto", "Civic")
moto1 = Moto("Yamaha", 2021, "Vermelho", "Esportiva")

veiculo1.exibir_info()
carro1.exibir_info()
moto1.exibir_info()

veiculo1.ano = 2022  # Usando o setter para atualizar o ano
carro1.ano = 1800    # Tentando definir um ano inválido
moto1.ano = 2023    # Usando o setter para atualizar o ano

veiculo1.exibir_info()
carro1.exibir_info()
moto1.exibir_info()