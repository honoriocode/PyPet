import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from pypet import Pypet

class TelinhaPypet:
  def __init__(self,janelinha):
    # gostaria de colocar todo o pypet e botões mais para cima
    # mas não sei como, imagino que tenha haver com esse frame
    # do construtor que recebe a window
    pypet = Pypet()
    janelinha.title('Pypet Game!')
    self.frame = tk.Frame(janelinha)
    self.frame.pack()

    self.name = tk.Label(self.frame, text = '')
    self.name.pack()
    
#############fotinhas#############
    if pypet.idade <= 10:
      self.frame1 = tk.Frame(width = 40, height = 40)
      self.frame1.pack()
      self.imgpypet = ImageTk.PhotoImage(Image.open("NewBorn Pypet.png"))
      self.label_imagem = tk.Label(self.frame,image= self.imgpypet)
      self.label_imagem['width'] = 140
      self.label_imagem.pack()
      
    if pypet.idade >= 10 and pypet.fome < 50 and pypet.saude  < 50:
      self.frame1 = tk.Frame(width = 40, height = 20)
      self.frame1.pack()
      self.imgpypet = ImageTk.PhotoImage(Image.open("NeedyPypet.png"))
      self.label_imagem = tk.Label(self.frame,image= self.imgpypet)
      self.label_imagem['width'] = 140
      self.label_imagem.pack()

    if pypet.idade >= 10 and pypet.humor == 'Triste' or pypet.humor == 'Com depressão':
      self.frame1 = tk.Frame(width = 40, height = 20)
      self.frame1.pack()
      self.imgpypet = ImageTk.PhotoImage(Image.open("BoredorStandbyPypet.png"))
      self.label_imagem = tk.Label(self.frame,image= self.imgpypet)
      self.label_imagem['width'] = 140
      self.label_imagem.pack()
      
    else:
      self.frame1 = tk.Frame(width = 40, height = 20)
      self.frame1.pack()
      self.imgpypet = ImageTk.PhotoImage(Image.open("defaultPypet.png"))
      self.label_imagem = tk.Label(self.frame,image= self.imgpypet)
      self.label_imagem['width'] = 140
      self.label_imagem.pack()
#############fotinhas#############

    self.n = tk.Button(self.frame, text = 'Nome')
    self.n['bg'] = 'black'
    self.n['fg'] = 'white'
    self.n.bind('<Button-1>',self.altnome)
    self.n.pack()
    
    
    self.lvlup = tk.Button(self.frame, text= 'Ver Level')
    self.lvlup['bg'] = 'blue'
    self.lvlup['fg'] = 'white'
    self.lvlup.bind('<Button-1>',self.lvl)
    self.lvlup.pack()

    self.hunger = tk.Button(self.frame, text= 'Alimentar')
    self.hunger['bg'] = 'green'
    self.hunger['fg'] = 'white'
    self.hunger.bind('<Button-1>', self.killHunger)
    self.hunger.pack()
    
    self.play = tk.Button(self.frame, text= 'Brincar')
    self.play['bg'] = 'yellow'
    self.play.bind('<Button-1>', self.playtime)
    self.play.pack()

    self.heal = tk.Button(self.frame, text= 'Curar +')
    self.heal['bg'] = 'red'
    self.heal['fg'] = 'white'
    self.heal.bind('<Button-1>', self.healing)
    self.heal.pack()

  def altnome (self, event):
    self.txt0 = 'Deseja adicionar ou mudar o nome de seu PyPet?'
    messagebox.askokcancel("Novo nome?", self.txt0)
    self.EnterName = tk.Entry(self.frame,border=2)
    self.EnterName['width'] = 10
    self.EnterName.pack(padx=10,pady=10)
    if self.EnterName == str:
      self.name = self.EnterName.get()
    
  def lvl(self,event):
    msg = 'Seu level é:' + str(self.pypet.lvlUP)
    # não tá pegando, fazendo com que clicar em ver level não     pegue
    messagebox.showinfo("Level:", msg)
  
  def killHunger(self,event):
    self.txt1 = 'Informe o quanto deseja alimentar seu Pypet:'
    messagebox.showinfo("Matar a fome", self.txt1)
    self.informHunger = tk.Entry(self.frame,border=2)
    self.informHunger['width'] = 10
    self.informHunger.pack(padx=10,pady=10)
    self.pypet.fome = self.informHunger.get()
    if self.informHunger > 100:
      self.txthunger0 = 'Você quer matar o coitado com tanta comida usuário!!?? (ง︡'-'︠)ง'
      messagebox.showinfo("-_-", self.txthunger0)
      self.pypet.fome = 100
    if self.informHunger < 0:
      self.txthunger1 = 'Isso não deveria ser possível usuário, além de ser muita maldade. Como você fez isso??'
      messagebox.showinfo("-_-", self.txthunger1)
      self.pypet.fome = 0


  def healing(self,event):
    self.txt2 = 'Informe o quanto deseja curar seu Pypet:'
    messagebox.showinfo("Aumentar Saúde", self.txt2)
    self.informHealing = tk.Entry(self.frame,border=2)
    self.informHealing['width'] = 10
    self.informHealing.pack(padx=10,pady=10)
    self.pypet.saude += self.informHealing.get()
    if self.informHealing > 100:
      self.txtheal0 = 'Você vai causar uma overdose no pobre Pypet usuário, você deveria cuidar dele!! (ง︡'-'︠)ง'
      messagebox.showinfo("-_-", self.txtheal0)
      self.pypet.saude = 100
    if self.informHealing < 0:
      self.txtheal1 = 'Isso não deveria ser possível usuário, além de ser muita maldade. Como você fez isso??'
      messagebox.showinfo("-_-", self.txtheal1)
      self.pypet.saude = 0
      
  def playtime(self,event):
    i = 0
    while i == 0:
      self.txt2 = 'Como pretende brincar? [1] - Ver TV (melhora baixa) [2] - Jogar bola (melhora mediana) [3] - Jogar Video-Game (Melhora muito)'
      messagebox.showinfo("  Brincar", self.txt3)
      self.informPlaying = tk.Entry(self.frame,border=2)
      self.informPlaying['width'] = 10
      self.informPlaying.pack(padx=10,pady=10)
      y = self.informPlaying.get()
      if y < 0:
        return 'Favor, escolher opção entre 1 e 3!'
      if y > 3:
        return 'Favor, escolher opção entre 1 e 3!'
      if y != int:
        return 'Escolha números e não letras usuário! Favor, respeitar as opções...'
      if y == 1:
        self.pypet.x += -1
      if y == 2:
        self.pypet.x += -2
      if y == 3:
        self.pypet.x += -3