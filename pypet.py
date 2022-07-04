from threading import Thread, Timer
from time import sleep
import random
class Pypet:
  def __init__(self, A = None, nome = None, fome = 0 , saude = 0, idade = 0, idadeR = None, humor = None, lvlUP = None, qtd = None, x = None, death = None):
    
    # não gravei o erro que estava dando aqui em cima -
    # Non-default argument follows default argument, corrigi colacando None em todos
    self.nome = nome   
    self.__fome = fome
    self.__saude = saude
    self.__idade = idade
    self.__idadeR = idadeR
    self.__humor = humor
    self.__lvlUP = lvlUP
    self.__death = death
    self.qtd = qtd
    self.__x = x
    self.__A = A
    
  @property
  def nome (self):
    return self.__nome
  @nome.setter
  def nome (self,nome):
    self.__nome = nome

  @property
  def humor (self):
    return self.__humor
  @nome.setter
  def humor (self,humor):
    self.__humor = humor

  @property
  def death (self):
    return self.__death
  @death.setter
  def death (self,death):
    self.__death = death

  @property
  def fome(self):
    return self.__fome
  @fome.setter 
  def fome (self,fome):
    self.__fome, fome = 0
    a = 0
    while a == 0:
      i = [15,25,35,45,60,75,85,100]
      self.__fome = random.choice(i)
      a += 1
    if self.__fome > 100:
      self.__fome = 100 
    if self.__fome < 0:
      self.__fome = 0
    return self.__fome
      
  @property
  def saude(self):
    return self.__saude
  @saude.setter
  def saude(self, saude):
    self.__saude, saude = 0
    a = 0
    while a == 0:
      j = [15,25,35,45,60,75,85,100]
      self.__saude = random.choice(j)
      a += 1
    if self.__saude > 100:
      self.__saude = 100 
    if self.__saude < 0:
      self.__saude = 0
    return self.__saude
  
  @property
  def idade(self):
    return self.__idade  
  @idade.setter
  def idade(self, idade):
    idade = 0
    if idade > 0:
      self.__idade = idade  
    if idade < 0:
      self.__idade = 0

  @property
  def lvlUP (self):
    return self.__lvlUP
  @lvlUP.setter
  def lvlUP (self, lvlUP):
    self.__lvlUP = 0
    if self.__idade == 25:
      self.__lvlUP = lvlUP = lvlUP + 1
    if self.__idade == 50:
      self.__lvlUP = lvlUP = lvlUP + 1
    if self.__A == 1:
      self.__lvlUP = lvlUP = lvlUP + 1
      self.__A = self.__A - 1
    return self.__lvlUP

  def Reaper (self):
    if self.__idade >= 70:
      list = [*range(70,101,1)] 
      self.__idadeR = random.choice(list)
    if self.__idade == self.__idadeR:
      self.__death = self.__death + 1
      self.__A = self.__A + 1
      
  def altnome (self):
    nome = input('Digite o novo nome de seu Pypet:')
    self.__nome = nome

  def timer(self, saude, fome, idade):
      i = 0
      while i == 0:
        self.__idade = self.__idade + 1
        sleep(60)
        self.Threading
      while i == 0:
        self.__saude = self.__saude - 10
        self.__fome = self.__fome - 10
        sleep(20)
        self.Threading
      if self.__fome == 0:
        sleep(180)
        self.__death = self.__death + 1
        self.Threading
      if self.__saude == 0:
        sleep(180)
        self.__death = self.__death + 1
        self.Threading
  
  def Threading(self):    
      Thread(target=self.timer).start()    
      
  def checkH(self, humor):
    i = 0
    while i == 0:  
      if self.__saude and self.__fome == 100:
        self.__x = 1
        if self.__x == 1:
          self.__humor = 'Super Alegre!'
          return self.__humor
      if self.__saude and self.__fome >= 75:
        self.__x = 2
        if self.__x == 2:
          self.__humor = 'Feliz'
          return self.__humor
      if self.__saude and self.__fome < 75 and self.__saude and self.__fome > 50:
        self.__x = 3
        if self.__x == 3:
          self.__humor = 'Contente'
          return self.__humor
      if self.__saude and self.__fome < 50 and self.__saude and self.__fome > 25:
        self.__x = 4
        if self.__x == 4:
          self.__humor = 'Triste'
          return self.__humor
      if self.__saude and self.__fome < 25:
        self.__x = 5
        if self.__x == 5:
          self.__humor = 'Com Depressão'
          return self.__humor
          
  def mostrar(self):
    return self.__nome + " têm " + str(self.__idade) + "anos, está com " + str(self.__fome) + "de fome," + str(self.__saude) + "de saúde e está" + str(self.__humor) 
    # Fazer o método aparecer ao apertar um botão