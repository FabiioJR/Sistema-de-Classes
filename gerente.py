from funcionario import Funcionario

class Gerente(Funcionario):
  def __init__(self, nome, rg, salario, registro):
    super().__init__(nome, rg, salario, registro)

  def Calcular_salario(self):
    super().Calcular_Salario()
  
  def Bonificacao(self):
    return self._salario * 12 * 0.1
