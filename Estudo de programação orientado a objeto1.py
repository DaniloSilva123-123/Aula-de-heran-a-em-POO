'''def area_retangulo(largura, altura):
    return largura * altura

def Responda():
    l = float(input('Digite o valor da largura:'))
    h = float(input('Digite o valor da altura:'))
    a = l * h
    print(f"A área do retângulo é de: {a}")

Responda()

def area_trapézio(B, b , h):
    return (B + b) * h/2

def Diga():
    B = int(input('Digite o valor da base maior do trapézio:'))
    b = int(input('Digite o valor da base menor do trapézio:'))
    h = float(input('Digite o valor da altura do trapézio:'))
    a = (B + b) * h/2
    print(f"A área do trapézio é de: {a}")

Diga()

def area_circulo(r, pi):
    return r**2 * pi

def Resolva():
    r = int(input('Digite o valor do raio do circulo:'))
    a = r**2 * 3.14
    print(f"A área do circulo é de: {a}")

Resolva()'''

'''def função_escolar():
        diga = input('Você é que profissional na escola? \nDigite 1 - Diretor: \nDigite 2 - Professor: \nDigite 3 - Funcionário(a): ')
        n = input('Digite o nome do novo membro da escola: ')

        if diga == "1" and n:
                print('Seja bem-vindo Diretor!!!')
                print(f"O nome do diretor é: {n}")

        elif diga == "2" and n:
                print('Seja bem-vindo Professor!!!')
                print(f"O nome do novo professor é: {n}")

        elif diga == "3" and n:
                print('Seja bem-vinda funcionária!!!')
                print(f"O nome do novo funcionário(a) é: {n}")

        else:
                print('Sinto muito você não passou na seleção da escola!!!')

        return diga, n

função_escolar()'''
                


'''def escola():
        u = input('Digite o nome de usuário do Professor: ')
        print(f"O perfil de usuário do professor é: {u}")

        senha = input('Digite a senha de acesso do Professor: ')
        print(f"A senha de acesso do professor é: {senha}")

        if u == "@Professor2543" and senha == 'Professor(a)62438454':
                        print('Acesso Permitido!')

        else:
                        print('Acesso Negado!')
        return u , senha


def Cadastro_Aluno():
        nome = input('Digite o nome do Aluno: ')
        print(f"O nome do Aluno é: {nome}")

        idade = int(input('Digite a idade do Aluno: '))
        print(f"A idade do aluno é de: {idade} anos")

        sexo = input('Digite o sexo do Aluno: ')
        print(f"O gênero do aluno é: {sexo}")

        altura = float(input('Digite a altura do Aluno: '))
        print(f"A altura do aluno é de: {altura}")

        cpf = input('Digite o número cpf do Aluno: ')
        print(f"O  CPF do aluno é: {cpf}")

        matricula = int(input('Digite o número de matrícula do Aluno: '))
        print(f"A matrícula do alumo é: {matricula}")
        return nome, idade, sexo, altura, cpf, matricula


def Boletim():
        N1 = float(input('Digite o valor da primeira nota do Aluno: '))
        print(f"O valor da primeira nota do aluno é: {N1}")

        N2 = float(input('Digite o valor da segunda nota do Aluno: '))
        print(f"O valor da segunda nota do aluno é: {N2}")

        N3 = float(input('Digite o valor da terceira nota do Aluno: '))
        print(f"O valor da terceira nota do aluno é: {N3}")

        N4 = float(input('Digite o valor da quarta nota do Aluno: '))
        print(f"O valor da quarta nota do aluno é: {N4}")

        Media = (N1 + N2 + N3 + N4)/4
        print(f"a média final do aluno é de: {Media}")

        if Media >= 7.5:
                            print('O aluno está Aprovado!')
                
        elif Media >= 6.5:
                            print('O aluno está de Recuperação!')
                
        else:
                            print('O aluno está Reprovado!')
        
                            print(f"A média final do aluno é de: {Media}")
        
        return N1, N2, N3, N4, Media

def Resultado():
        u, senha = escola()
        nome, idade , sexo, altura, cpf, matricula = Cadastro_Aluno()
        N1, N2, N3, N4, Media = Boletim()

Resultado()'''

'''class teste():
    y = 16

filho = teste()
print(filho.y)'''

'''class Escola():
    def função_escolar(self):
        diga = input('Você é que profissional na escola? \nDigite 1 - Diretor(a): \nDigite 2 - Professor(a): \nDigite 3 - Funcionário(a): ')
        n = input('Digite o nome do(a) novo(a) membro(a) da escola: ')

        if diga == "1" and n:
                print('Seja bem-vindo(a) Diretor(a)!!!')
                print(f"O nome do(a) diretor(a) é: {n}")

        elif diga == "2" and n:
                print('Seja bem-vindo(a) Professor(a)!!!')
                print(f"O nome do(a) novo(a) professor é: {n}")

        elif diga == "3" and n:
                print('Seja bem-vindo(a) funcionário(a)!!!')
                print(f"O nome do(a) novo(a) funcionário(a) é: {n}")

        else:
                print('Sinto muito você não passou na seleção da escola!!!')

        return diga, n

    def Gestão(self):

        while True:

            login = input('Digite o login de acesso do(a) diretor(a): ')

            try:
                pin = int(input('Digite a senha de acesso do(a) diretor(a): '))
            except ValueError:
                print('A senha deve conter apenas números!')
                continue

            if login == "Diretor(a).Gestor(a)683584@gmail.com" and pin == 735789707:
                print('Acesso permitido!')
                break
        

            else:
                print('Acesso Negado!')
                print('Tente Novamente!!!')


    def escola(self):
        u = input('Digite o nome de usuário do(a) Professor(a): ')
        print(f"O perfil de usuário do(a) professor(a) é: {u}")

        senha = input('Digite a senha de acesso do Professor(a): ')
        print(f"A senha de acesso do(a) professor(a) é: {senha}")
        
        if u == "@Professor(a)2543" and senha == 'Professor(a)62438454':
                print('Acesso Permitido!')
        
        else:
                print('Acesso Negado!')
    
        return u , senha

    def Cadastro_Aluno(self):
        nome = input('Digite o nome do(a) Aluno(a): ')
        print(f"O nome do(a) aluno(a) é: {nome}")

        idade = int(input('Digite a idade do(a) Aluno(a): '))
        print(f"A idade do(a) aluno(a) é de: {idade} anos")

        sexo = input('Digite o sexo do(a) Aluno(a): ')
        print(f"O gênero do(a) aluno(a) é: {sexo}")

        altura = float(input('Digite a altura do Aluno: '))
        print(f"A altura do(a) aluno(a) é de: {altura}")

        cpf = input('Digite o número do cpf do(a) (a): ')
        print(f"O  CPF do(a) aluno(a) é: {cpf}")

        matricula = int(input('Digite o número de matrícula do(a) Aluno(a): '))
        print(f"A matrícula do(a) aluno(a) é: {matricula}")
        return nome, idade, sexo, altura, cpf, matricula

    def Boletim(self):
        N1 = float(input('Digite o valor da primeira nota do(a) Aluno(a): '))
        print(f"O valor da primeira nota do aluno(a) é: {N1}")

        N2 = float(input('Digite o valor da segunda nota do(a) Aluno(a): '))
        print(f"O valor da segunda nota do aluno(a) é: {N2}")

        N3 = float(input('Digite o valor da terceira nota do(a) Aluno(a): '))
        print(f"O valor da terceira nota do aluno(a) é: {N3}")

        N4 = float(input('Digite o valor da quarta nota do(a) Aluno(a): '))
        print(f"O valor da quarta nota do(a) aluno(a) é: {N4}")

        Media = (N1 + N2 + N3 + N4)/4
        print(f"A média final do(a) aluno(a) é de: {Media}")

        if Media >= 7.5:
                        print('O(A) aluno(a) está Aprovado!')
                
        elif Media >= 6.5:
                        print('O(A) aluno(a) está de Recuperação!')

        else:
            print('O(A) aluno(a) está Reprovado!')
        
            (f"A média final do(a) aluno(a) é de: {Media}")
        
        return N1, N2, N3, N4, Media

E = Escola()
print(E.função_escolar(),E.Gestão(),E.escola(),E.Cadastro_Aluno(),E.Boletim())'''

'''class Empresa():

    def __init__(self, marca, ano_fundação, fundador, objetivos, meta):
        self.marca = marca
        self.ano_fundação = ano_fundação
        self.fundador = fundador
        self.objetivos = objetivos
        self.meta = meta

    def descreva(self):
        print(f"A marca da empresa é: {self.marca}")
        print(f"O ano que a empresa fundou foi de: {self.ano_fundação}")
        print(f"Quem é o fundador da empresa:{self.fundador}")
        print(f"Quais são os objetivos da empresa:{self.objetivos}")
        print(f"Qual é a meta da empresa:{self.meta}")


    def registrar_Lucro(self, Lucro):
    
        self.meta += Lucro

        print(f"\nEmpresa: {self.marca}")
        print(f"O lucro registrado dessa empresa é de: (+R$) {Lucro}")
        print(f"A meta da empresa foi de: {self.meta}")

        return f"{self.objetivos} a empresa lucrou {Lucro} (+R$)!"

    def registrar_Prejuízos(self, Prejuízos):

        self.meta += Prejuízos

        print(f"\nEmpresa: {self.marca}")
        print(f"O lucro registrado dessa empresa é de: (-R$) {Prejuízos}")
        print(f"A meta da empresa foi de: {self.meta}")   

        return f"{self.objetivos} a empresa teve prejuízo de: {Prejuízos} (-R$)!"

    def mostrar_situação_finançeira(self):
         
         print(f"\nEmpresa 1: {self.marca}")
         print(f"O saldo financeiro dessa empresa é de: {self.meta}")

         if self.meta > 0:
          print('A empresa ganhou Lucro (+R$)!')

         elif self.meta < 0:
             print('A empresa teve um prejuízo: (-R$)')

         else:
              print('As empresas estão no mesmo nível!')
              
def objetivo_Principal():
        Empresa1 = Empresa("MICROSOFT",
                           "A microsoft foi fundada em 4 de abril de 1975",
                           "Bill Gates e Paul Allen",
                           "Expansão da inteligência artificial e infraestrutura em nuvem.",
                        865858695)
        
        Empresa2 = Empresa("APPLE",
                            "Apple foi fundada 1 de abril de 1976",
                            "Steve Jobs, Steve Wozniak e Ronald Wayne",
                            "Desenvolvimento de produtos tecnológicos e inovação.",
                        687768800)

        return Empresa1 , Empresa2

# Criando dados da Empresa:
Empresa1, Empresa2 = objetivo_Principal()


Empresa1.descreva()
Empresa2.descreva()

#Meta da Empresa 1:
Empresa1.registrar_Lucro(500000)
Empresa1.registrar_Prejuízos(-9744999)

# meta da Empresa2:
Empresa2.registrar_Lucro(400000)
Empresa2.registrar_Prejuízos(-567439)

#Situação Financeira da Empresa:
Empresa1.mostrar_situação_finançeira()
Empresa2.mostrar_situação_finançeira()'''



