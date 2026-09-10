class empresa():

    def __init__(self, marca, ano_fundação, fundador, objetivos, meta):

        self.marca = marca
        self.ano_fundação = ano_fundação
        self.fundador = fundador
        self.objetivos = objetivos
        self.meta = meta

    def descreva(self):

        print(f"\nA marca da empresa é: {self.marca}")
        print(f"O ano que a empresa foi fundada foi: {self.ano_fundação}")
        print(f"Quem é o fundador da empresa: {self.fundador}")
        print(f"Quais são os objetivos da empresa: {self.objetivos}")
        print(f"Qual é a meta financeira da empresa: R${self.meta}")

    def registrar_Lucro(self, Lucro):

        self.meta += Lucro

        print(f"\nEmpresa: {self.marca}")
        print(f"O lucro registrado dessa empresa é de: (+R$) {Lucro}")
        print(f"A meta/saldo da empresa agora é: R${self.meta}")

        return f"{self.objetivos} A empresa lucrou R${Lucro} (+R$)!"

    def registrar_Prejuizos(self, Prejuizos):

        self.meta -= Prejuizos

        print(f"\nEmpresa: {self.marca}")
        print(f"O prejuízo registrado dessa empresa é de: (-R$) {Prejuizos}")
        print(f"A meta/saldo da empresa agora é: R${self.meta}")

        return f"{self.objetivos} A empresa teve prejuízo de R${Prejuizos} (-R$)!"

    def mostrar_situacao_financeira(self):

        print(f"\nEmpresa: {self.marca}")
        print(f"Saldo financeiro: R${self.meta}")

        if self.meta > 0:
            print("A empresa está com saldo positivo: LUCRO (+R$)!")

        elif self.meta < 0:
            print("A empresa está com saldo negativo: PREJUÍZO (-R$)!")

        else:
            print("A empresa está com saldo zerado!")

def setor_empresa(self):
    print("Empresas de Tecnologia: Microsoft, Apple e Samsung.")

class Microsoft(empresa):

    def setor_empresa(self):
        print("Setor: Inteligência artificial e computação em nuvem.")

class Apple(empresa):

    def setor_empresa(self):
        print("Setor: Dispositivos eletrônicos e software.")

class Samsung(empresa):

    def setor_empresa(self):
        print("Setor: Eletrônicos de consumo e semicondutores.")

def main():
    Empresa1 = Microsoft(
        "MICROSOFT",
        "4 de abril de 1975",
        "Bill Gates e Paul Allen",
        "Expansão da inteligência artificial e infraestrutura em nuvem.",
        865858695
    )

    Empresa2 = Apple(
        "APPLE",
        "1 de abril de 1976",
        "Steve Jobs, Steve Wozniak e Ronald Wayne",
        "Desenvolvimento de produtos tecnológicos e inovação.",
        687768800
    )

    Empresa3 = Samsung(
        "SAMSUNG",
        "1 de março de 1938",
        "Lee Byung-chul",
        "Desenvolvimento de produtos eletrônicos e inovação.",
        500000000
    )

    Empresa1.descreva()
    Empresa1.setor_empresa()

    Empresa2.descreva()
    Empresa2.setor_empresa()

    Empresa3.descreva()
    Empresa3.setor_empresa()


if __name__ == "__main__":
    main()
    



