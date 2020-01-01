# -*- coding: utf-8 -*-

from Pilha import *
from ClasseExpressao import *
from Menu import *

expressao=Expressao('')

M=''
while M !='s':
  try:
    if expressao.getExpressao()=='' :
      Menu.mostraMenuPrincipal()
    else:
      Menu.mostraMenuPrincipal(expressao.getExpressao())

    M=input("Opção do Menu: ") # atribuindo à variável M
    assert M=='p' or M=='P' or M=='i' or M=='I' or M=='a' or M=='A' or M=='s' or M=='S' or M=='d' or M=='D'
  except AssertionError:
    print('\nOpção inválida. Tente uma opção do menu!')
  except KeyboardInterrupt:
    M=''
    print('\nOpção inválida. Tente uma opção do menu!')

  if M == "d" or M == "D": # opção para Ler um expressão infixa
    expressao.lerExpressao()      
  
  if M == "p" or M == "P": # opção para Converter para Pos-Fixa (Menu Principal)
    if expressao.getExpressao()=='':
      print('Não há expressão InFixa definida. Primeiro escolha a opção D ')
      
    else:
      op1='' # Variável controle do Menu Pos-Fixa
      while op1!='s':
        try: ### Lendo a opção no MenuPosFixa
          Menu.mostraMenuPosFixa()
          op1=input("Opção do Menu: ") # atribuindo à variável op1
          assert op1=='a' or op1=='A' or op1=='b' or op1=='B' or op1=='s' or op1=='S' 
        except AssertionError:
          print('\nOpção inválida. Tente uma opção do menu!')
        except KeyboardInterrupt:
          op1=''
          print('\nOpção inválida. Tente uma opção do menu!')

        if op1 == "a" or op1 == "A": # opção para mostrar na tela (Menu Pos-Fixa)
          expressao.posFixaExibicao()
          
        if op1 == "b" or op1 == "B": # opção para salvar em arquivo (Menu Pos-Fixa)
          with open("ArquivoPosFixa.txt","w") as arq:
            temp=expressao.posFixaExibicao("a")
            arq.write(str(temp))
        
          print('\nSalvo no arquivo Arquivo.txt !!')
          try:
            prox=input()
          except KeyboardInterrupt:
            pass
        
        if op1 == "S": #Fim do Loop Menu PosFixa
          op1='s'

  if M == "i" or M == "I": # opção para Converter para Pre-Fixa (Menu Principal)
    if expressao.getExpressao()=='':
      print('Não há expressão InFixa definida. Primeiro escolha a opção D ')
    else:
      op1='' # Variável controle do Menu Pre-Fixa
      while op1!='s':
        try: ### Lendo a opção no Menu PreFixa
          Menu.mostraMenuPreFixa()
          op1=input("Opção do Menu: ") # atribuindo à variável op1
          assert op1=='a' or op1=='A' or op1=='b' or op1=='B' or op1=='s' or op1=='S' 
        except AssertionError:
          print('\nOpção inválida. Tente uma opção do menu!')
        except KeyboardInterrupt:
          op1=''
          print('\nOpção inválida. Tente uma opção do menu!')

        if op1 == "a" or op1 == "A": # opção para mostrar na tela (Menu Pre-Fixa)
          expressao.preFixaExibicao()
          
        if op1 == "b" or op1 == "B": # opção para salvar em arquivo (Menu Pre-Fixa)
          with open("ArquivoPreFixa.txt","w") as arq:
            temp=expressao.preFixaExibicao("a")
            arq.write(str(temp))
        
          print('\nSalvo no arquivo Arquivo.txt !!')
          try:
            prox=input()
          except KeyboardInterrupt:
            pass
        
        if op1 == "S": #Fim do Loop Menu Pre-Fixa
          op1='s'

  if M == "a" or M == "A": # opção para Associar Valores (Menu Principal)
    if expressao.getExpressao()=='':
      print('Não há expressão InFixa definida. Primeiro escolha a opção D ')
    else:
      print('\nExpressão pos-Fixa:',expressao.posFixa())
      expressao.associarValores()
      print("\nTecle Enter para voltar ao menu Principal!!")
      try:
        prox=input()
      except KeyboardInterrupt:
        pass

  if M=="S": # Fim do Loop do Menu Principal
    M="s"

print("\nPrograma Fechado corretamente") # fim do while (principal)
