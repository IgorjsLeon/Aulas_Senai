class Funcionario:
    def __init__(self, nome, salariobase):
        self.nome = nome
        self.salariobase = salariobase

    def calcular_salario(self):
        pass

class CLT(Funcionario):
    def add_CLT(self, nome, salariobase):
        funcionarioCLT = [{'CLT': 'sim','Nome': nome, 'Salário': salariobase}]
        funcionarios.append(funcionarioCLT)
        return 'Funcionario CLT cadastrado com sucesso', funcionarios

    def calcular_salario(self):
        return 'salario clt'
    
class Comissionado(Funcionario):
    def add_Comissionado(self, nome, salariobase= None):
        funcionarioComissionado = [{'Comissionado': 'sim', 'Nome': nome, 'Salário': salariobase}]
        funcionarios.append(funcionarioComissionado)
        return 'Funcionario Comissionado cadastrado com sucesso', funcionarios

    def calcular_salario(self):
        return 'salario comissionado'
    
class Estagiario(Funcionario):
    def add_Estagiario(self, nome, salariobase):
        funcioarioEstagiario = [{'Estagiario': 'sim','Nome': nome, 'Salário': salariobase/2}]
        funcionarios.append(funcioarioEstagiario)
        return 'Funcionario Estagiario cadastrado com sucesso', funcionarios
    
    def calcular_salario(self, salariobase):
        salEstag = salariobase / 2
        return f'O salario do estagiario é: {salEstag}'

funcionarios = []

nome = input("Digite o nome do funcionario: ")
salariobase = float(input("Digite o salario base da empresa: "))

opcao = input("Este funcionario é CLT(1), Comissionado(2) ou Estagiario(3)?: ")

if opcao == '3':
    estagiario = Estagiario(nome, salariobase)
    estagiario.add_Estagiario(nome, salariobase)
    print(estagiario.calcular_salario(salariobase))
    print(funcionarios)
elif opcao == '2':
    comissionado = Comissionado(nome, salariobase)
    comissionado.add_Comissionado(nome, salariobase)
    print(comissionado.calcular_salario())
    print(funcionarios)
elif opcao == '1':
    clt = CLT(nome, salariobase)
    clt.add_CLT(nome, salariobase)
    print(clt.calcular_salario())
    print(funcionarios)
else:
    print('Opção inválida!')