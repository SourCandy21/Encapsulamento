#Classe Publico Tipo_de_Jogo 
class Tipo_de_Jogo:
  def __init__(self, nome, empresa, jogo):
    self.nome = nome
    self.empresa = empresa
    self.jogos = jogo

  def get_nome(self):
    return self.nome

  def get_empresa(self):
    return self.empresa

  def get_jogos(self):
    return self.jogos



#Classe Privado Tipo_de_Jogo 
class Tipo_de_Jogo:
  def __init__(self, nome, empresa, jogo):
    self.__nome = nome
    self.__empresa = empresa
    self.__jogos = jogo

  def get_nome(self):
    return self.nome

  def get_empresa(self):
    return self.empresa

  def get_jogos(self):
    return self.jogos



#Classe Protegido Tipo_de_Jogo 
class Tipo_de_Jogo:
  def __init__(self, nome, empresa, jogo):
    self._nome = nome
    self._empresa = empresa
    self._jogos = jogo

  def get_nome(self):
    return self.nome

  def get_empresa(self):
    return self.empresa

  def get_jogos(self):
    return self.jogos