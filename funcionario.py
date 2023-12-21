from pessoa import Pessoa

class Funcionario(Pessoa):
  def __init__(self, nome, rg, salario, registro):
    super().__init__(nome, rg)
    self._salario = salario
    self._registro = registro

  def Cadastrar(self):
    pass

  def Calcular_Salario(self):
    return self._salario * 12

  def Demitir(self):
    pass
