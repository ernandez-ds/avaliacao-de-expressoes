# -*- coding: utf-8 -*-

from Pilha import *

class Expressao:
  """Classe que serve para instanciar objetos com atributo denominado exp, que recebe uma string, expressao InFixa"""

  def __init__(self,exp=""):
    """ Construtor padrão da Classe Expressao com um argumento que pode ser passado ou não"""
    self.__exp=exp

  def getExpressao(self):
    """ Metodo que retorna o valor do atributo do objeto """
    return self.__exp

  def setExpressao(self,exp):
    """ Metodo que insere novo valor no atributo do objeto """
    self.__exp=exp
  
  def __str__(self):
    """ Metodo que retorna o atributo quando a função print é chamada"""
    return f'Expressão Infixa: {self.__exp}'
  
  def __prioridade (self,op):
    """Essa função retorna o número de prioridade dos operadores
    """
    if op=="(" :
      return 1
    elif op=="+" or op=="-" :
      return 2
    elif op=="*" or op=="/"  :
      return 3
    elif op=="^":
      return 4
    else :
      return 0

  def __ehOperando(self,op):
    """ Testa se um elemento é membro da seqüência. Retorna True se encontra e, False se não encontra.
    """
    import string
    A=list(string.ascii_letters)
    return op in A
  
  def __ehOperador(self,op):
    """ Testa se um elemento é membro da seqüência. Retorna True se o encontra, e False se não o encontra.
    """
    B=["+","-","*","/","^"]
    return op in B
  
  def posFixa(self):
    """Recebe uma expressão infixa válida e retorna espressão PosFixa
    """
    saida=[]
    p=Pilha()
    for i in range (len(self.__exp)):
      if (self.__ehOperando(self.__exp[i])):
        saida.append(self.__exp[i])
      if (self.__ehOperador(self.__exp[i])):
        while (p.estaVazia() == False) and self.__prioridade(p.topo()) >= self.__prioridade(self.__exp[i]) :
          saida.append(p.desempilha())
        p.empilha(self.__exp[i])
      if (self.__exp[i]== '('):
        p.empilha(self.__exp[i])
      if (self.__exp[i]== ')'):
        while p.topo() != '(' :
          saida.append(p.desempilha())
        x=p.desempilha()
    
    while (p.estaVazia() == False) :
      saida.append(p.desempilha())
    
    saida=''.join(saida)
    return(saida)
  
  def posFixaExibicao(self,salvar=''):
    """Exibe o processo de conversao da expressao infixa para posFixa
    """
    saida=[]
    p=Pilha()
    
    if salvar=='a':
      arq=""
      sair='ok'
      op='n'
    else:
      print() # pula linha
      sair='' 
    ############################ Tratando a entrada
    while sair != 'ok':
      try:
        op=(input("Deseja visualizar o passo a passo da conversão (s/n): "))
        if (op=='s' or op=='S' or op=='n' or op=='N'):
          sair='ok'
        assert op=='s' or op=='S' or op=='n' or op=='N'
      except AssertionError:
        print('Opção inválida. Escolha (s/n).')
      except KeyboardInterrupt:
        print('\nOpção inválida. Escolha (s/n).')
    
    if op=='s' or op=='S':
      print('\n>>>>> Tecle Enter para cada iteração!!!!')

    if salvar=='a':
      arq+='\nExpressão infixa: '
      arq+=self.__exp
    else: 
      print('\nExpressão infixa: ',end='')
      print(self.__exp)
    
    l1=['Símbolo','Pilha','Saída']
    l2=['-------','------------------','-----------']
    if salvar=='a':
      arq+='\n{:<7}    {:<18}    {:<11}'.format(*l1)
      arq+='\n{:<7}    {:<18}    {:<11}'.format(*l2)
    else:
      print('{:<7}    {:<18}    {:<11}'.format(*l1))
      print('{:<7}    {:<18}    {:<11}'.format(*l2))

    for i in range (len(self.__exp)):
      if (self.__ehOperando(self.__exp[i])):
        saida.append(self.__exp[i])
      if (self.__ehOperador(self.__exp[i])):
        while (p.estaVazia() == False) and self.__prioridade(p.topo()) >= self.__prioridade(self.__exp[i]) :
          saida.append(p.desempilha())
        p.empilha(self.__exp[i])
      
      if (self.__exp[i]== '('):
        p.empilha(self.__exp[i])
      
      saidaParcial=''.join(saida)
      l3=[self.__exp[i],p.imprimePilha(),saidaParcial]
      if salvar=='a':
        arq+='\n{:<7}    {:<18}    {:<11}'.format(*l3)
      else:
        print('{:<7}    {:<18}    {:<11}'.format(*l3))
      
      if op=='s' or op=='S': 
        try:
          prox=input()
        except KeyboardInterrupt:
          print()
          
      if (self.__exp[i]== ')'):
        while p.topo() != '(' :
          saida.append(p.desempilha())
        x=p.desempilha()
        
    while (p.estaVazia() == False) :
      saida.append(p.desempilha())
    
    saida=''.join(saida)
    if salvar=='a':
      arq+='\n--------------------------------------------'
      arq+='\nExpressão pós-fixa: '
      arq+=saida
      return arq
    else:
      print('--------------------------------------------')
      print('Expressão pós-fixa:', saida)
      print()

  def preFixa(self):
    """Recebe uma expressão infixa válida e retorna espressão Prefixa
    """
    exp=self.__exp[::-1]
    saida=[]
    p=Pilha()
    for i in range (len(exp)):
      if (self.__ehOperando(exp[i])):
        saida.insert(0,exp[i])
      if (self.__ehOperador(exp[i])):
        while (p.estaVazia() == False) and self.__prioridade(p.topo()) > self.__prioridade(exp[i]) :
          saida.insert(0,p.desempilha())
        p.empilha(exp[i])
      if (exp[i]== ')'):
        p.empilha(exp[i])
      if (exp[i]== '('):
        while p.topo() != ')' :
          saida.insert(0,p.desempilha())
        x=p.desempilha()
    
    while (p.estaVazia() == False) :
      saida.insert(0,p.desempilha())
    
    saida=''.join(saida)
    return(saida)

  def preFixaExibicao(self,salvar=''):
    '''
      Exibe o processo de conversão da expressão infixa para prefixa
    '''
    exp=self.__exp[::-1]
    saida=[]
    p=Pilha()
    
    if salvar=='a':
      arq=""
      sair="ok"
      op='n'
    else:
      print()
      sair=''
        
    ############################ Tratando a entrada
    while sair != 'ok':
      try:
        op=(input("Deseja visualizar o passo a passo da conversão (s/n): "))
        if (op=='s' or op=='S' or op=='n' or op=='N'):
          sair='ok'
        assert op=='s' or op=='S' or op=='n' or op=='N'
      except AssertionError:
        print('Opção inválida. Escolha (s/n).')
      except KeyboardInterrupt:
        print('\nOpção inválida. Escolha (s/n).')
    
    if op=='s' or op=='S':
      print('\n>>>>> Tecle Enter para cada iteração!!!!')
      
    if salvar=='a':
      arq+='\nExpressão infixa: '
      arq+=self.__exp
    else: 
      print('\nExpressão infixa: ',end='')
      print(self.__exp)
    
    l1=['Símbolo','Pilha','Saída']
    l2=['-------','------------------','-----------']
    if salvar=='a':
      arq+='\n{:<7}    {:<18}    {:<11}'.format(*l1)
      arq+='\n{:<7}    {:<18}    {:<11}'.format(*l2)
    else:
      print('{:<7}    {:<18}    {:<11}'.format(*l1))
      print('{:<7}    {:<18}    {:<11}'.format(*l2))

    
    for i in range (len(exp)):
      if (self.__ehOperando(exp[i])):
        saida.insert(0,exp[i])
      if (self.__ehOperador(exp[i])):
        while (p.estaVazia() == False) and self.__prioridade(p.topo()) > self.__prioridade(exp[i]) :
          saida.insert(0,p.desempilha())
        p.empilha(exp[i])
      if (exp[i]== ')'):
        p.empilha(exp[i])
      
      saidaParcial=''.join(saida)
      l3=[self.__exp[i],p.imprimePilha(),saidaParcial]
      if salvar=='a':
        arq+='\n{:<7}    {:<18}    {:<11}'.format(*l3)
      else:
        print('{:<7}    {:<18}    {:<11}'.format(*l3))
      
      if op=='s' or op=='S': 
        try:
          prox=input()
        except KeyboardInterrupt:
          print()

      if (exp[i]== '('):
        while p.topo() != ')' :
          saida.insert(0,p.desempilha())
        x=p.desempilha()
    
    while (p.estaVazia() == False) :
      saida.insert(0,p.desempilha())
    
    saida=''.join(saida)
    if salvar=='a':
      arq+='\n--------------------------------------------'
      arq+='\nExpressão pre-fixa: '
      arq+=saida
      return arq
    else:
      print('--------------------------------------------')
      print('Expressão pre-fixa:', saida)
      print()

  def associarValores(self):
    """ Associa um valor float a cada operando da expressão e retorna o resultado da expressão em Float, utilizando a expressao no formato PosFixo
    """
    lista1=self.extrairOperandos()# guarda os operandos
    lista2=[] # guarda os valores dos respesctivos operandos
    for i in lista1:
      sair=''
      while sair != 's' :
        try:
          lista2.append(float(input(f'\nValor de {i} : ')))
        except ValueError: 
          print('> Você não digitou um algarismo. Digite apenas algarismos !!!')
        except KeyboardInterrupt:
          print('> Você não digitou um algarismo. Digite apenas algarismos !!!')
        else: 
          sair='s'
      
    exp2=self.posFixa()# gera a PosFixa do argumento 'exp'
    p=Pilha()
    for i in exp2:
      if self.__ehOperando(i):
        i=i.upper()
        if i in lista1:
          pos=lista1.index(i)# posicao do elemento i na lista1
          p.empilha(lista2[pos])# empilha o respectivo da lista2 
      if self.__ehOperador(i):
        x=p.desempilha()
        y=p.desempilha()
        if i=='+':
          p.empilha(y+x)
        elif i=='-':
          p.empilha(y-x)
        elif i=='*':
          p.empilha(y*x)
        elif i=='/':
          p.empilha(y/x)
        elif i=='^':
          p.empilha(y**x)
    print ('Resultado da expressão:',p.topo())
  ############## Fim da Função AssociarValores

  def extrairOperandos(self):
    """ Retorna a lista de operandos de uma expressão
    """
    operandos=[]
    for i in self.__exp:
      i=i.upper()
      if self.__ehOperando(i) and len(operandos)==0:
        operandos.append(i)
      else:
        if self.__ehOperando(i) and not(i in operandos):
          operandos.append(i)  
    return (operandos)
  # Fim da Função ExtrairOperandos

  def __expressaoValida(self):
    """ Checar se o atributo expressão é válido ou não(retorno True ou False)
    """
    C=['(',')']
    controle=[]
    
    for i in self.__exp:
      if self.__ehOperando(i) or self.__ehOperador(i) or (i in C):
        controle.append(True)
      else:
        controle.append(False)
      
    if self.__exp=='':
      return False
      
    if False in controle:
      return False
    else:
      return True
  
  def __balanceamentoParenteses(self):
    """ Metodo que analisa o balanceamento de parenteses da expressão infixa, retorna True se as condições forem atendidas ou False se não forem atendidas
    """
    p=Pilha()
    ok=1 ## condição "BEM balançeada" já pre determinada
    for i in self.__exp:
      if i=='(':
        p.empilha(i) 
      elif i==')':
        if p.estaVazia()==True:
          p.empilha(i)
        else:
          x=p.desempilha()
          if x != '(' and i==')':
            ok=0
    if p.estaVazia()==False:
      ok=0
    return True if ok==1 else False

  
  def lerExpressao(self):
    """ Metodo que realiza a leitura da expressao infixa e insere no atributo caso esta seja válida  """
    while True: ### Leitura da "EXPRESSAO" inFixa
      try:
        if self.__expressaoValida() and self.__balanceamentoParenteses() or self.__exp=='':
          guarda=self.__exp
        self.__exp=input("\nDigite a expressão na forma infixa (quit: sair): ") # Atribuindo a expressao
        if self.__exp=='quit':
          self.__exp=guarda
          break
        if self.__expressaoValida() and self.__balanceamentoParenteses():
          print('\nOK: Expressão válida!')
          break
        assert self.__expressaoValida() and self.__balanceamentoParenteses()
      except AssertionError:
        print('Expressão inválida. Tente Novamente.')
      except KeyboardInterrupt:
        print('\nExpressão inválida. Tente Novamente.')    
