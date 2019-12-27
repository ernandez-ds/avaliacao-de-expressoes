class Menu:
  """ Classe que imprime menus do programa principal, menu posfixa e menu prefixa
  """
  
  @classmethod
  def mostraMenuPrincipal(cls, texto=''):
    ''' metodo de classe que imprime o menu principal'''

    print("\n=========== MENU PRINCIPAL ===========")
    if texto !='':
      print("     Expressao Infixa:",texto)
    
    if texto =='':
      print("(d) Digitar Expressão Infixa")
    else:
      print("(d) Inserir nova Expressão Infixa")
    print("(p) Converter para pós-fixa")
    print("(i) Converter para pre-fixa")
    print("(a) Associar valores aos operandos")
    print("(s) Sair")
    print("==========================")
 
  @classmethod
  def mostraMenuPosFixa(cls):
    '''metodo de classe que imprime o meno posfixa'''
    print("\n=========== MENU Pos-Fixa ===========")
    print("Conversão para pós-fixa")
    print('(a) > Na tela')
    print('(b) > Em arquivo texto')
    print("(s) Sair")
    print("==========================")

  @classmethod
  def mostraMenuPreFixa(cls):
    '''metodo de classe que imprime o menu pre fixa'''
    print("\n=========== MENU Pré-Fixa ===========")
    print("Conversão para pré-fixa")
    print('(a) > Na tela')
    print('(b) > Em arquivo texto')
    print("(s) Sair")
    print("==========================")
