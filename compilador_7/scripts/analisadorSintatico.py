"""
Henrique Camacho Farias
201711310031
"""

import sys

class AnalisadorSintatico():

  def __init__(self):
    self.currentLine = 0
    self.currentItem = 0
    self.currentLexema = 0
    self._allTokens = [[]]
    self.amountLines = 0
    self.amountLexema = 0
    self.tokens = [[]]
    self.dic = {}
    self.tokens_warning = []
  
  def setTokens(self, generatedTokens):
    self._allTokens = generatedTokens
    self.amountLines = len(self._allTokens)
    self.amountLexema = sum([ len(lineTokens) for lineTokens in self._allTokens])
    self.tokens = self._allTokens[0] if self.amountLines > 0 else [[]]
    #for i in self._allTokens:
    #    for ii in i:
    #        if ii[1] not in self.dic.keys():
    #            self.dic[ii[1]] = ii[0]
    #APAGAR
    #print(self.dic)
  

    for l in self._allTokens:
        for ll in l:
            if ll[0] == 'identf':
                self.tokens_warning.append(ll[1])

  def print_data(self):
    print(" - Dados - ")
    print("Total linhas : ", self.amountLines)
    print("Total lexemas : ", self.amountLexema)

  def _isEmptyLine(self, line):
    return len(line) == 0

  def _nextToken(self):
    
    if(self.currentLexema <= self.amountLexema):

      self.currentItem += 1
      if(self.currentItem == len(self.tokens)):
          self.currentItem = 0
          self.currentLine += 1

          if(self.currentLine < self.amountLines):
            self.tokens = self._allTokens[self.currentLine]

            while(self._isEmptyLine(self.tokens) and self.currentLine < self.amountLines):
              self.currentItem = 0
              self.currentLine += 1
              if(self.currentLine < self.amountLines):
                self.tokens = self._allTokens[self.currentLine]

      self.currentLexema += 1
    else :
      print(" *** [tokensesgotados] *** ")
  
  def _currentToken(self):
    
    if(len(self.tokens) > 0):

      #Apagar
      #self.dic[(self.tokens[self.currentItem])[1] ] = (self.tokens[self.currentItem])[0]
      
      return self.tokens[self.currentItem]
    
    return []

  def _getCurrentTokenKey(self):
    return (self._currentToken()[0] if len(self._currentToken())> 0 else 'erroReadKey')

  def _getCurrentTokenValue(self):
    return  (self._currentToken()[1] if len(self._currentToken())> 0 else 'erroReadToken')

  def lookAhead(self):
    nextItem = self.currentItem + 1
    auxCurrentLine = self.currentLine
    auxTokens = self.tokens
    
    if(self.currentLexema+1 < self.amountLexema):
      if(nextItem >= len(self.tokens)):
          nextItem = 0
          auxCurrentLine += 1

          if(auxCurrentLine <= self.amountLines):
            auxTokens = self.allTokens[auxCurrentLine]

            while(self._isEmptyLine(auxTokens) and auxCurrentLine < self.amountLines):
              nextItem = 0
              auxCurrentLine += 1
              if(auxCurrentLine < self.amountLines):
                auxTokens = self.allTokens[auxCurrentLine]
      
      return auxTokens[nextItem]
    else :
      return []

  def match(self, item, value):
    if(item != value): 
      print(f"Erro -> esperava {value}")
      sys.exit()

    return True

# --- --- --- --- --- Analisador Sintatico --- --- --- --- ---

  def analyse(self):
    print("\n Executando --Analisador Sintatico-- ############ \n")
    self._Programa ()
  

  def _Programa(self):
    if(self._getCurrentTokenValue() == 'program'):
      self._nextToken()
    
      if(self._getCurrentTokenKey() == 'identf'):
        self._nextToken()
        self._Corpo()
      else:
        print("[Programa]- Erro esperava um identificador válido ")
        self._Erro()
    else :      
      print("[Programa]- Erro esperava program ")
      self._Erro()


  def _Corpo(self):
    self._Dc()

    if(self._getCurrentTokenValue() == 'begin'):
      self._nextToken()
      self._Comandos()
          
      if(self._getCurrentTokenValue() == 'end.'):
        self._SuccessCode ()
      else:
        print("--Corpo-- --->> ERRO esperava 'end.' " )
        self._Erro()
    else:
      print("--Corpo-- --->> Erro esperava 'begin' ")
      self._Erro()


  def _Dc(self):
    if(self._getCurrentTokenValue() == 'procedure'):
      self._Dc_p()
      self._Mais_dc()
    elif(self._getCurrentTokenValue() in ['real','integer']):
      self._Dc_v()
      self._Mais_dc()
    else:
      self._Vazio()


  def _Mais_dc(self):
    if(self._getCurrentTokenValue() == ';'):
      self._nextToken()
      self._Dc()
    else:
      self._Vazio()
    
  def _Dc_v(self):
    if(self._getCurrentTokenValue() in ['real','integer']):
      self._nextToken()

      if self._getCurrentTokenValue() == ":":
        self._nextToken()
        #Analise Semantica, checa se a variavel com o mesmo nome ja existe
        if self._getCurrentTokenValue() in list(self.dic.keys()) and self._getCurrentTokenKey() == 'identf':
            print("Variavel com nome repetido "+ self._getCurrentTokenValue() ) 
            self._Erro()
        
        else:
            #print(self._getCurrentTokenValue()) 
            self.dic[self._getCurrentTokenValue()] = self._getCurrentTokenKey()
            self._Variaveis()

      else: 
        print("--Dc_v-- --->> ERRO esperava ':' " )
    else:
      print("--Dc_v-- --->> Erro esperava 'real ou integer' ")
    

  def _Tipo_var(self):
    if(self._getCurrentTokenValue() in ['real', 'integer']):
      self._nextToken()
    else:
      print("--Tipo_var-- --->> Erro esperava 'real' ou 'integer'")
      self._Erro()


  def _Variaveis(self):
    if(self._getCurrentTokenKey() == 'identf'):   
        self._nextToken()
        self._Mais_var()
    
    else:
      if self._getCurrentTokenValue() in ["var", "integer", "real", "if", "then", "while", "do", "write", "read", "begin", "end", "end.", "program", "procedure"]:
        print("--Variaveis'' --->> Erro, nome do identificador não pode ser palavra reservada --> "+self._getCurrentTokenValue() )  
        self._Erro()
      else:
        print("--Variaveis-- --->> Erro esperava 'identificador' ")
        self._Erro()


  def _Mais_var(self):   
    if(self._getCurrentTokenValue() == ','):
      self._nextToken()
      if self._getCurrentTokenValue() in list(self.dic.keys()) and self._getCurrentTokenKey() == 'identf':
        print("Variavel com nome repetido "+ self._getCurrentTokenValue() ) 
        self._Erro()
      else:
      #print(self._getCurrentTokenValue()) 
        self.dic[self._getCurrentTokenValue()] = self._getCurrentTokenKey()  
        self._Variaveis()
    else:
      self._Vazio()


  def _Dc_p(self):
    if(self._getCurrentTokenValue() == 'procedure'):
      self._nextToken()

      if(self._getCurrentTokenKey() == 'identf'):
        self._nextToken()
        self._Parametros()
        self._Corpo_p()
      else:
        print("--Dc_p-- --->> Erro esperava identificador")
        self._Erro()
    else:
      print("--Dc_p-- --->> Erro esperava 'procedure'")
      self._Erro()
      


  def _Parametros(self):
    if(self._getCurrentTokenValue() == '('):
      self._nextToken()
      self._Lista_par()
      
      if(self._getCurrentTokenValue() == ')'):
        self._nextToken()
      else:
        print("--Parametros-- --->> Erro esperava ')'")
        self._Erro()
    else:
      print("--Parametros-- --->> Erro esperava '('")
      self._Erro()


  def _Lista_par(self):
    self._Variaveis()
    
    if(self._getCurrentTokenValue() == ':'):
      self._nextToken()
      self._Tipo_var()
      self._Mais_par()
    else:
      print("---Lista_par-- --->> Erro esperava ':'")
      self._Erro()


  def _Mais_par(self):
    if(self._getCurrentTokenValue() == ';'):
      self._nextToken()
      self._Lista_par()
    else:
      self._Vazio()


  def _Corpo_p(self):
    self._Dc_loc()
    
    if(self._getCurrentTokenValue() == 'begin'):
      self._nextToken()
      self._Comandos()
    else : 
      print("--Corpo_p-- --->> Erro esperava 'begin'")
      self._Erro()

    if(self._getCurrentTokenValue() == 'end'):
      self._nextToken()
    else:
      print("--Corpo_p-- --->> Erro esperava 'end'")
      self._Erro()
  
      

  def _Dc_loc(self):
    if(self._getCurrentTokenValue() in ['real','integer']):
      self._Dc_v()
      self._Mais_dcloc()
    else :
      self._Vazio()


  def _Mais_dcloc(self):
    if(self._getCurrentTokenValue() == ';'):
      self._nextToken()
      self._Dc_loc()
    else :
      self._Vazio()


  def _Lista_arg(self):
    if(self._getCurrentTokenValue() == '('):
      self._nextToken()
      self._Argumentos()
      
      if(self._getCurrentTokenValue() == ')'):
        self._nextToken()
      else:
        print("--Lista_arg-- --->> Erro esperava ')'")
        self._Erro()
    else:
      self._Vazio()


  def _Argumentos(self):
    #print("Argumentos "+self._getCurrentTokenValue())
    if(self._getCurrentTokenKey()  == 'identf'):
      self._nextToken()
      self._Mais_ident()
    else:
      print("--Argumentos-- --->> Erro esperava 'identificador'")
      self._Erro()


  def _Mais_ident(self):
    #print("Mais_ident "+self._getCurrentTokenValue())
    if(self._getCurrentTokenValue() == ';'):
      self._nextToken()
      self._Argumentos()
    else:
      self._Vazio()


  def _PFalsa(self):
    if(self._getCurrentTokenValue() == 'else'):
      self._nextToken()
      self._Comandos()
    else:
      self._Vazio()


  def _Comandos(self):
    self._Comando()
    self._Mais_comandos()


  def _Mais_comandos(self):
    if(self._getCurrentTokenValue() == ';'):
      self._nextToken()
      self._Comandos()
    else: 
      self._Vazio()


  def _Comando(self):
    itemKey = self._getCurrentTokenKey()
    itemValue = self._getCurrentTokenValue()
    if(itemValue == 'read' or itemValue == 'write' ):
      self._nextToken()
      
      if(self._getCurrentTokenValue() == '('):
        self._nextToken()
        if self._getCurrentTokenValue() not in self.dic.keys():
            print("--Comando-- --->> Erro variável não declarada "+self._getCurrentTokenValue())
            self._Erro()
        else:    
            self._Variaveis()
        
        if(self._getCurrentTokenValue() == ')'):
          self._nextToken()
        else :
          print("--Comando-- --->> Erro esperava ')'")
          self._Erro()
      else:
        print("--Comando-- --->> Erro esperava '('")
        self._Erro()

    elif(itemValue == 'if'):
      self._nextToken()
      self._Condicao()

      if(self._getCurrentTokenValue() == 'then'):
        self._nextToken()
        self._Comandos()
        self._PFalsa()
        
        if(self._getCurrentTokenValue() == '$'):
          self._nextToken()
        else :
          print("--Comando-- --->> Erro esperava '$'")
          self._Erro()
      else:
        print("--Comando-- ---> Erro esperava 'then'")
        self._Erro()


    elif(itemValue == 'while'):
      self._nextToken()
      self._Condicao()

      
      if(self._getCurrentTokenValue() == 'do'):
        self._nextToken()
        self._Comandos()
        
        if(self._getCurrentTokenValue() == '$'):
          self._nextToken()
        else :
          print("--Comando-- --->> Erro esperava '$'")
          self._Erro()
      else:
        print("--Comando-- --->> Erro esperava 'do'")
        self._Erro()

    elif(itemKey == 'identf'):
      aux = itemValue
      self._nextToken()
      if aux not in self.dic.keys() and self._getCurrentTokenValue() == ":=":
        print("--_Comando-- --->> Erro variável não declarada "+ aux)
        self._Erro()
      else:
        self._Resto_ident()

    else:
      print("--Comando-- --->> Erro esperava 'comando' ou 'identificador'")
      self._Erro()


  def _Resto_ident(self):
    item = self._getCurrentTokenValue()
    if(item == ':='):
      self._nextToken()
      self._Expressao()
    elif(item == '(') :
      #print("_Resto_ident "+self._getCurrentTokenValue() )
      #self._nextToken()
      self._Lista_arg()
    else:
      print("--Resto_ident-- --->> Erro esperava ':=' ou '(' ")
      self._Erro()


  def _Condicao(self):
    self._Expressao()
    self._Relacao()
    self._Expressao()


  def _Relacao(self):
    if(self._getCurrentTokenValue() in ["=",">","<",">=","<=","<>"]):
      self._nextToken()
    else:
      print("--Relacao-- --->> Erro esperava 'simbolo de relacao'")
      self._Erro()


  def _Expressao(self):
    self._Termo()
    self._Outros_termos()


  def _Op_un(self):
    if(self._getCurrentTokenValue() in ["+",'-']):
      self._nextToken()
    else:
      self._Vazio()


  def _Outros_termos(self):
    if(self._getCurrentTokenValue() in ['+', '-']):
      self._Op_ad()
      self._Termo()
      self._Outros_termos()
    else :
      self._Vazio()


  def _Op_ad(self):
    if(self._getCurrentTokenValue() in ['+', '-']):
      self._nextToken()
    else:
      print("--Op_ad-- --->> Erro esperava '+' ou '-'")
      self._Erro()


  def _Termo(self):
    self._Op_un()
    self._Fator()
    self._Mais_fatores()


  def _Mais_fatores(self):
    if(self._getCurrentTokenValue() in ['*','/']):
      self._Op_mul()
      self._Fator()
      self._Mais_fatores()
    else:
      self._Vazio()


  def _Op_mul(self):
    if(self._getCurrentTokenValue() in ['*','/']):
      self._nextToken()
    else:
      print("--Op_mul-- --->> Erro esperava '*' ou '/'")
      self._Erro()



  def _Fator(self):
    if(self._getCurrentTokenValue()=="("):
      self._nextToken()
      self._Expressao()
      
      if(self._getCurrentTokenValue() ==")"):
        self._nextToken()
      else : 
        print("Erro esperava ')'")   
        self._Erro()
    elif(self._getCurrentTokenKey() in ['identf','numero_int', 'numero_float']):
        #print(self._getCurrentTokenValue())
        if self._getCurrentTokenKey() == 'identf':
            if self._getCurrentTokenValue() not in self.dic.keys():
                print("--Op_Fator-- --->> Erro variável não declarada "+ self._getCurrentTokenValue())
                self._Erro()
            else:
                self._nextToken()
        else:
            self._nextToken()
    else:
      print("--Fator-- --->> Erro esperava '(', 'identificador' ou 'numero'")
      self._Erro()


  def _Vazio (self) :
    # print('vazio')
    pass

  def _Erro (self):
    print("linha -> ", self.currentLine+1)
    print('\nEncerrando programa... \n')
    sys.exit()
    
  def _Warning_unused(self):
    import collections
    counter = collections.Counter(self.tokens_warning[1:])
    counter = dict(counter)
    for variavel in counter.keys():
        if counter[variavel]<=1:
            print("Warning variavel declarada mas não usada "+variavel)

  def _SuccessCode(self):
    #print(self.dic)
    #print(self.tokens_warning)
    self._Warning_unused()
    print('--AnalisadorSintatico-- --->> Terminou \n' )
