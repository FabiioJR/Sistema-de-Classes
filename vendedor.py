from funcionario import Funcionario

class Vendedor(Funcionario):
  def __init__(self, nome, rg, salario, registro, comissão, numero_vendas):
    super().__init__(nome, rg, salario, registro)
    self._comissão = comissão
    self._numero_vendas = numero_vendas

  def Calcular_salario(self):
    print (f'O salario anual é de {self._salario * 12}')

  def Comissão(self):
    return self._comissão * self._numero_vendas
