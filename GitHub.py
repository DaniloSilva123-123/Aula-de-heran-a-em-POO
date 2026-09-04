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


def objetivo_Principal():

    Empresa1 = empresa(
        "MICROSOFT",
        "4 de abril de 1975",
        "Bill Gates e Paul Allen",
        "Expansão da inteligência artificial e infraestrutura em nuvem.",
        865858695
    )

    Empresa2 = empresa(
        "APPLE",
        "1 de abril de 1976",
        "Steve Jobs, Steve Wozniak e Ronald Wayne",
        "Desenvolvimento de produtos tecnológicos e inovação.",
        687768800
    )

    return Empresa1, Empresa2


# Criando as empresas
Empresa1, Empresa2 = objetivo_Principal()

# Mostrando os dados
Empresa1.descreva()
Empresa2.descreva()

# Registrando lucro e prejuízo da Microsoft
Empresa1.registrar_Lucro(500000000)
Empresa1.registrar_Prejuizos(346547840)

# Registrando lucro e prejuízo da Apple
Empresa2.registrar_Lucro(300000000)
Empresa2.registrar_Prejuizos(549765654)

# Mostrando situação financeira
Empresa1.mostrar_situacao_financeira()
Empresa2.mostrar_situacao_financeira()

class Empresa_Tecnologia(empresa):
    def __init__(self, marca, ano_fundação, fundador, objetivos, meta):
        super().__init__(marca, ano_fundação, fundador, objetivos, meta)

Microsoft = Empresa_Tecnologia(
        "MICROSOFT",
        "4 de abril de 1975",
        "Bill Gates e Paul Allen",
        "Expansão da inteligência artificial e infraestrutura em nuvem.",
        865858695
 )

Microsoft.descreva()
Microsoft.registrar_Lucro(500000000)
Microsoft.registrar_Prejuizos(346547840)
Microsoft.mostrar_situacao_financeira()

class Empresa_Tecnológica(empresa):
    def __init__(self, marca, ano_fundação, fundador, objetivos, meta):
        super().__init__(marca, ano_fundação, fundador, objetivos, meta)

Apple = Empresa_Tecnológica(
        "APPLE",
        "1 de abril de 1976",
        "Steve Jobs, Steve Wozniak e Ronald Wayne",
        "Desenvolvimento de produtos tecnológicos e inovação.",
        687768800
)
Apple.descreva()
Apple.registrar_Lucro(300000000)
Apple.registrar_Prejuizos(549765654)
Apple.mostrar_situacao_financeira()

def Reunião_Empresarial(pauta):
    pauta.discurso()

    Reunião_Empresarial(empresa(), Empresa_Tecnologia(), Empresa_Tecnológica())



