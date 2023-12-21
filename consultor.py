from funcionario import Funcionario

class Consultor(Funcionario):
  def __init__(self, nome, rg, salario, registro, horas_trabalhadas, valor_hora):
    super().__init__(nome, rg, salario, registro)
    self._horas_trabalhadas = horas_trabalhadas
    self._valor_horas = valor_hora

  def Calcular_salario(self):
    print (f'O salario anual é de {self._salario * 12}')

  def Valor_Hora(self):
    return self._horas_trabalhadas * self._valor_horas
