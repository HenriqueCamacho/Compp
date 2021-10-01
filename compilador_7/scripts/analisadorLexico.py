"""
Henrique Camacho Farias
201711310031
"""
import re

class AnalisadorLexico () :
  _RESERVED_WORDS = ["var", "integer", "real", "if", "then", "while", "do", "write", "read", "begin", "end", "end.", "program", "procedure"]
  _SYMBOLS = [',', ':', ':=', ';', '$', '(', ')', '{', '}']
  _OPERATORS = ['>', '>=','<','<=', '+', '-', '/', '*', '<>']
  _NAMESPACES = {
    'RESERVED' : 'reserv',             
    'IDENT' : 'identf',                
    ':=' : 'atribt',                    
    ',' : 'virgul',                    
    ':' : '2ponto',                    
    ';' : 'pntvir',                    
    '+' : 'somavl',                   
    '*' : 'multvl',                    
    '(' : 'abre_parent',               
    ')' : 'fecha_parent',              
    '$' : 'fecha_comand',   
    '=' : 'equalvl',   
    'NUMBER_INT' : 'numero_int',       
    'NUMBER_FLOAT' : 'numero_float',   
    'OPERATOR' : 'operador',
  }

  position = 0

  # Resultados
  identfiers = []
  reservedWords = []
  tokens = []
  codes = []
  table = []

  def __init__(self):
    pass

  def _nextPosition(self):
    self.posisition += 1

  def _printLineError(self, lineError):
    print(f"Error in line {lineError}")

  def _parseLine(self, line):

    usedSymbols = self._SYMBOLS + ['+', '-', '/', '*', '=']
    for symbol in usedSymbols:
      line = line.replace(symbol, f" {symbol} ")

    line = line.replace('*  /', ' */ ')
    line = line.replace('/  *', ' /* ')
    line = line.replace(':  =', ' := ')
    line = line.replace('<  >', ' <> ')
    line = line.replace('> =', ' >= ')
    line = line.replace('< =', ' <= ')
    line = line.replace('end .', ' end. ')

    return line
    

  def _isNewComment(self, item):
    return  item in ['{', '/*']

  def _isCloseComment(self, item):
    return  item in ['}', '*/']

  def _addToken(self, chave, valor):
    auxToken = []
    auxToken.append(chave)
    auxToken.append(valor)
    self.tokens.append(auxToken)

  def _auxTokenAddLine(self, chave, valor):
    auxToken = []
    auxToken.append(chave)
    auxToken.append(valor)

    return auxToken

  def _addLineTokens(self, tokensLine):
    self.tokens.append(tokensLine)

  def _isReservedWord(self, item):
    return item in self._RESERVED_WORDS 

  def _isValidIdentifier(self, item):
    return re.match("^[A-Za-z0-9_-]*$", item) and item[0].isalpha()
      
  def _isIdentifier(self, item):
    return item in self.identfiers 
  
  def _isNumber(self, item):                
    try:
        float(item)
        return True
    except ValueError:
        return False
  
  def _isSymbol(self, item):
    return item in self._SYMBOLS
        
  def _isOperator(self, item):
    return item in self._OPERATORS

  def printAll (self) :
    print ("\n------------------------------------- \n")
    print('- [IDENTIFICADORES] - ')
    for i in self.identfiers:
        print(i)


    print('\n - [ TOKENS ] - ')
    for j in self.tokens:
        print(j,end=',\n')
    
    
    print ("\n - [ TABELA_DE_SIMBOLOS] - ")
    for linha in self.table:
        print(linha)
    print ("\n------------------------------------- \n")

  def analyse(self, filename) :
    print("\n Executando --Analisador Lexico-- ############ \n")

    line = 0
    text = []
    findError = False
    isComment = False
    

    with open(filename) as file:
      text = file.readlines()
     
    while (not findError  and line < len(text)): 
      parsedLine = self._parseLine(text[line]).split()

      auxLineTokens = []

      for item in parsedLine :

        
        if(isComment) :
          if(self._isCloseComment(item)):
            isComment = False
        else:
          if(self._isNewComment(item)):
            isComment = True
        

          else :
            
            if(self._isReservedWord(item)):
              auxLineTokens.append(self._auxTokenAddLine( self._NAMESPACES['RESERVED'], item))
            elif(self._isIdentifier(item)):
              auxLineTokens.append(self._auxTokenAddLine( self._NAMESPACES['IDENT'], item))
            elif(self._isOperator(item)):   
              auxLineTokens.append(self._auxTokenAddLine(self._NAMESPACES["OPERATOR"], item))
            elif(self._isSymbol(item)):  
              auxLineTokens.append(self._auxTokenAddLine(self._NAMESPACES[item], item))
            elif(self._isNumber(item)):                
              if('.' in item):
                  auxLineTokens.append(self._auxTokenAddLine(self._NAMESPACES['NUMBER_FLOAT'], item))
              else :
                  auxLineTokens.append(self._auxTokenAddLine( self._NAMESPACES['NUMBER_INT'], item))

            else :
              if(self._isValidIdentifier(item)):
                auxLineTokens.append(self._auxTokenAddLine(self._NAMESPACES['IDENT'], item))
              else :
                self._printLineError(line+1)
                print(f"In AnalisadorLexico -> {item}")
                findError = True
                #####  Adicionando Numeros

      self._addLineTokens(auxLineTokens)
      line += 1
    print("--AnalisadorLexico-- --->> Terminou")

    if(findError):
      return False
    return True


  def getGeneratedTokens(self):
    return self.tokens

# an = LexicalAnalyzer()
# an.analyse('input.txt')
# an.printAll()
