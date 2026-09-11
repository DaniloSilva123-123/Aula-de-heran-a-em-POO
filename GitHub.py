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


class funcionario():

    def __init__(self, nome, idade, cargo, salario, empresa):

        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.__salario = salario
        self.empresa = empresa

    def descreva_funcionario(self):

        print(f"\nNome do funcionário: {self.nome}")
        print(f"Cargo do funcionário: {self.cargo}")
        print(f"Salário do funcionário: R${self.__salario}")

    def registrar_aumento(self, aumento):
        if aumento > 0:
            self.__salario += aumento
            print(f"O funcionário {self.nome} recebeu um aumento de R${aumento}. Novo salário: R${self.__salario}")

        else:
            print(f"Erro: O aumento não pode ser negativo. Valor fornecido: R${aumento}")
            return f"Erro: O aumento não pode ser negativo. Valor fornecido: R${aumento}"

        self.__salario += aumento

        print(f"\nFuncionário: {self.nome}")
        print(f"O aumento registrado desse funcionário é de: (+R$) {aumento}")
        print(f"O salário atual do funcionário agora é: R${self.__salario}")

        return f"{self.nome} recebeu um aumento de R${aumento} (+R$)!"
    

    def registrar_desconto(self, desconto):
        if desconto < 0:
            self.__salario -= desconto
            print(f"O funcionário {self.nome} teve um desconto de R${desconto}. Novo salário: R${self.__salario}")
            print(f"\nFuncionário: {self.nome}")
            print(f"O desconto registrado desse funcionário é de: (-R$) {desconto}")
            print(f"O salário atual do funcionário agora é: R${self.__salario}")

            return f"{self.nome} teve um desconto de R${desconto} (-R$)!"

    def calcular_salário_anual(self):
        salario_anual = self.__salario * 12
        print(f"\nFuncionário: {self.nome}")
        print(f"O salário anual do funcionário é: R${salario_anual}")
        return salario_anual

def main():
    empresa1 = Microsoft("Microsoft", 1975, "Bill Gates", "Inovação tecnológica", 1000000)
    empresa2 = Apple("Apple", 1976, "Steve Jobs", "Design e inovação", 2000000)
    empresa3 = Samsung("Samsung", 1938, "Lee Byung-chul", "Eletrônicos de consumo", 1500000)

    empresa1.descreva()
    empresa1.setor_empresa()
    empresa1.registrar_Lucro(50000)
    empresa1.mostrar_situacao_financeira()

    empresa2.descreva()
    empresa2.setor_empresa()
    empresa2.registrar_Prejuizos(30000)
    empresa2.mostrar_situacao_financeira()

    funcionario1 = funcionario("João Silva", 30, "Desenvolvedor de Software", 5000, empresa1)
    funcionario1.descreva_funcionario()
    funcionario1.registrar_aumento(1000)

    funcionario2 = funcionario("Maria Oliveira", 28, "Analista de Marketing", 4500, empresa2)
    funcionario2.descreva_funcionario() 
    funcionario2.registrar_aumento(800)

    for empresa in [empresa1, empresa2, empresa3]:
        empresa.descreva()
        empresa.setor_empresa()
        empresa.mostrar_situacao_financeira()

        funcionario1 = funcionario("João Silva", 30, "Desenvolvedor de Software", 5000, empresa)
        funcionario1.descreva_funcionario()
        funcionario1.registrar_aumento(1000)
        funcionario1.calcular_salário_anual()
        funcionario1.registrar_desconto(500)

        funcionario2 = funcionario("Maria Oliveira", 28, "Analista de Marketing", 4500, empresa)
        funcionario2.descreva_funcionario()
        funcionario2.registrar_aumento(800)
        funcionario2.calcular_salário_anual()
        funcionario2.registrar_desconto(300)

if __name__ == "__main__":
    main()