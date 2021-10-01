"""
Henrique Camacho Farias
201711310031
"""

import os
from analisadorLexico import AnalisadorLexico
from analisadorSintatico import  AnalisadorSintatico

class Compiler():

  def __init__(self):
    self.lexical = AnalisadorLexico()
    self.syntatic = AnalisadorSintatico()
    self.tokens = []

  def analisadorLexico(self, inputFile):
    if(self.lexical.analyse(inputFile)):
      self.tokens = self.lexical.getGeneratedTokens()
      #print(self.tokens)
    else :
      print("Erro ao fazer a análise léxica .... ")

  def analisadorSintatico(self):
    self.syntatic.setTokens(self.tokens)
    self.syntatic.analyse()

  def printTokens(self):
    for line in self.lexical.getGeneratedTokens():
      print(line)
    

ARQ = 'entrada6.txt'

CAMINHO = 'entradas/' + ARQ

#CAMINHO = os.getcwd()+'/src/input/' + ARQ

compilador = Compiler()
compilador.analisadorLexico(CAMINHO)
compilador.analisadorSintatico()
