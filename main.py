from pessoa import Pessoa
from funcionario import Funcionario
from vendedor import Vendedor
from consultor import Consultor
from gerente import Gerente

Gerente = Gerente('',1,5000,2)
print(Gerente.Calcular_Salario())
print(Gerente.Bonificacao())

Consultor = Consultor('',1,1000,2,8,5)
print(Consultor.Valor_Hora())

Vendedor = Vendedor('',1,1000,2,10,50)
print(Vendedor.Comissão())
