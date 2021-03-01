from usuarie import Usuarie
from endereco import Endereco
from corrente import Corrente
from poupanca import Poupanca

class Cliente(Usuarie):

  endereco = Endereco()  #atributo endereço do tipo Endereço
  contas = []   #lista de contas e dentro dela teremos objetos do tipo Corrente ou Poupança


# tem que fazer isso para ter outro init na classe filha
  def __init__(self, cpf, nome, email, celular, renda):
    # inicializa os atributos da classe mae    
    super().__init__(cpf, nome, email, celular)  #metodo que chama o init da classe usuario
    # inicializa os atributos dessa classe  / classe filha    
    try:
      self.renda = float(renda)
    except ValueError:
      self.renda = 0.0
      print("Atenção! Renda inválida!")   