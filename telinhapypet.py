import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from pypet import Pypet

class TelinhaPypet:
  def __init__(self,janelinha):
    pypet = Pypet()
    janelinha.title('Pypet Game!')
    self.frame = tk.Frame(janelinha)
    self.frame.pack()

    if self.__idade <= 10:
      self.frame1 = tk.Frame(janelinha, width = 40, height = 40)
      self.frame1.pack()
      self.imgpypet = ImageTk.PhotoImage(Image.open("NewBorn Pypet.jpg"))
      self.label_imagem = tk.Label(self.frame,image= self.imgpypet)
      self.label_imagem['width'] = 140
      self.label_imagem.pack(padx=20,pady=20)
      self.label_imagem.pack()

    if self.__idade >= 10 and self.__fome < 50 and self.__saude  < 50:
      self.frame1 = tk.Frame(janelinha, width = 40, height = 40)
      self.frame1.pack()
      self.imgpypet = ImageTk.PhotoImage(Image.open("NeedyPypet.jpg"))
      self.label_imagem = tk.Label(self.frame,image= self.imgpypet)
      self.label_imagem['width'] = 140
      self.label_imagem.pack(padx=20,pady=20)
      self.label_imagem.pack()

    if self.__idade >= 10 and self.__humor == 'Triste' or self.__humor == 'Com depressão':
      self.frame1 = tk.Frame(janelinha, width = 40, height = 40)
      self.frame1.pack()
      self.imgpypet = ImageTk.PhotoImage(Image.open("BoredorStandbyPypet.jpg"))
      self.label_imagem = tk.Label(self.frame,image= self.imgpypet)
      self.label_imagem['width'] = 140
      self.label_imagem.pack(padx=20,pady=20)
      self.label_imagem.pack()
      
    else:
      self.frame1 = tk.Frame(janelinha, width = 40, height = 40)
      self.frame1.pack()
      self.imgpypet = ImageTk.PhotoImage(Image.open("defaultPypet.jpg"))
      self.label_imagem = tk.Label(self.frame,image= self.imgpypet)
      self.label_imagem['width'] = 140
      self.label_imagem.pack(padx=20,pady=20)
      self.label_imagem.pack()


    self.lvlup = tk.Button(self.frame, text= 'Ver Level')
    self.lvlup['bg'] = 'blue'
    self.lvlup['fg'] = 'white'
    self.lvlup.bind('<Button-1>',self.lvl)
    self.lvlup.pack()
    
    self.play = tk.Button(self.frame, text= 'Brincar')
    self.play['bg'] = 'yellow'
    self.play.bind('<Button-1>', self.playtime)
    self.play.pack()

    self.hunger = tk.Button(self.frame, text= 'Alimentar')
    self.hunger['bg'] = 'green'
    self.hunger['fg'] = 'white'
    self.hunger.bind('<Button-1>', self.killHunger)
    self.hunger.pack()

    self.heal = tk.Button(self.frame, text= 'Curar +')
    self.heal['bg'] = 'red'
    self.heal['fg'] = 'white'
    self.heal.bind('<Button-1>', self.healing)
    self.heal.pack()
    
  def lvl(self,event):
    msg = 'Seu level é:' + str(self.__lvlUP)
    messagebox.showinfo("Level:", msg)
  
  def killHunger(self,event):
    self.txt2 = tk.Label(self.frame, text = ('Informe a quantidade que deseja alimentar seu Pypet:'))
    self.informHunger = tk.Entry(self.frame,border=2)
    self.informHunger['width'] = 10
    self.informHunger.pack(padx=10,pady=10)
    self.pypet.fome = self.informHunger.get()


  def healing(self,event):
    self.txt3 = tk.Label(self.frame, text = ('Informe o quanto deseja curar seu pet:'))
    self.informHealing = tk.Entry(self.frame,border=2)
    self.informHealing['width'] = 10
    self.informHealing.pack(padx=10,pady=10)
    if self.informHealing > 100:
        return 'Você quer matar o coitado com tanta comida usuário!!?? (ง︡'-'︠)ง'
    if self.informHealing < 0:
        return 'Isso não deveria ser possível usuário, além de ser muita maldade. Como você fez isso??'
    self.pypet.saude += self.informHealing.get()
      
  def playtime(self,event):
    i = 0
    while i == 0:
      self.txt4 = tk.Label(self.frame, text = ('Como pretende brincar? [1] - Ver TV (melhora baixa) [2] - Jogar bola (melhora mediana) [3] - Jogar Video-Game (Melhora muito)'))
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
