#PROJETO DA DISCIPLINA PROGRAMAÇÃO E ESTRUTURA DE DADOS#
##Conversão e Avaliação de Expressões Infixas em Pós-fixas e Pré-fixas##
##2018.2##

**1. Apresentação**

A representação de expressões aritméticas que seja conveniente do ponto de vista computacional é assunto de interesse, por exemplo, na área de compiladores. A notação tradicional é ambígua e, portanto, obriga ao preestabelecimento de regras de prioridade. Naturalmente, isso torna a tarefa computacional menos simples. 

Vimos em nossas aulas que a representação pós-fixada é uma alternativa para transformação das expressões infixas. O objetivo deste projeto é colocar em prática os ensinamentos e técnicas abordados no decorrer do curso, utilizando a linguagem Python e o Paradigma Orientado a Objeto, para o desenvolvimento de uma Estrutura de Dados que dê suporte à análise, verificação e execução de expressões pós-fixas usando uma Pilha.

**2. A Equipe**

O desenvolvimento do projeto de disciplina poderá ser feito em equipe de no máximo 2 (dois) alunos(as), sendo necessária a apresentação e discussão do código. A nota do projeto pode ser diferenciada entre os membros da equipe, visto que serão avaliados in loco o conhecimento do código e capacidade de responder a questionamentos pontuais e segurança na discussão sobre a lógica adotada.

**3. A Estrutura de Dados**

O projeto, em si, consiste em empacotar uma estrutura de dados bem-definida que atenda aos requisitos a seguir discriminados:

(a) Permitir que uma expressão no formato infixa seja convertida em pós-fixa;

(b) Permitir que uma expressão no formato infixa seja convertida em pré-fixa;

Nas conversões (a) e (b), um argumento adicional deve ser previsto para controlar a exibição do passo-a-passo da conversão. Isto é, se o usuário deseja que o processamento de cada símbolo só avance com o pressionar da tecla ENTER.

Caso o argumento de controle não esteja definido para a exibição passo-a-passo, todo o processamento será realizado de uma única vez. Para os dois tipos de conversão (pré-fixa e pós-fixa), será retornada a string resultante da transformação.

(c) Checar se uma expressão infixa passada por argumento é válida (retorno True ou False)

(d) Checar se o balanceamento dos parênteses da expressão de entrada está correto. Por exemplo, cada parêntese de abertura deve ter o seu correspondente parêntese de fechamento.

(e) Definir um método que seja capaz de extrair os operandos de uma expressão infixa

(f) Executar uma expressão traduzida para o formato pós-fixo ou pré-fixo, retornando o seu valor como tipo float.

(g) Permitir que o passo-a-passo da execução possa ser direcionado para um arquivo texto.

A decisão de codificar os métodos de conversão como de instância ou de classe é uma escolha de cada equipe. Da mesma forma, métodos públicos ou privados devem ser pensados com coerência. Obviamente, outros métodos de apoio podem surgir, de acordo com a estrutura de projeto de cada equipe, para auxiliar no funcionamento das operações supracitadas. 


**4. Informações Adicionais**

* Cada operando é representado por uma única letra do alfabeto (A..Z ou a..z) ou por um número inteiro;

* Os operadores válidos são +, -, *, / e ^;

* A operação de verificação de validade de uma expressão infixa deve assegurar se a expressão é válida em termos do uso correto dos parênteses e uso operadores/operandos, considerando que os operadores são binários;

* A expressão aritmética pode conter operandos repetidos;

* O layout da apresentação do programa que testa a(s) classe(s) e suas funcionalidades é de livre decisão da equipe. Entretanto, devem ser observadas as seguintes situações:

1. No programa principal, o usuário deve digitar a expressão no formato infixo;

2. O usuário deve interagir com a biblioteca informando se deseja visualizar o passo-a-passo da transformação;

3. Antes de executar a transformação, deve ser verificado se a expressão infixa é válida ou não. Se for válida, executa a transformação. Se não for, mensagens de erro apropriadas devem ser apresentadas ao usuário de forma que possa 
iniciar uma nova digitação da expressão;

4. Após a conversão da expressão, se houver alguma dependência (exemplo: a expressão contém operandos que não tem valores associados) o usuário deve digitar o valor de cada operando identificado. Cada operando deve ser identificado automaticamente, de modo que o usuário da aplicação associe apenas um valor numérico (float) a cada operando;

5. Por fim, a expressão pós-fixada ou pré-fixada é executada e o valor final (float) decorrente da avaliação da expressão é exibido ao usuário.

6. O usuário pode executar o mesmo processo (passos de 1 a 5) quantas vezes desejar.

**5. O  Menu Principal**

O menu principal deve contemplar acesso (envio de mensagem) aos principais métodos da estrutura de dados desenvolvida, provendo ao menos as seguintes funcionalidades:

(p) Converter para pós-fixa

    > Na tela
    > Em arquivo texto

(i) Converter para pré-fixa

    > Na tela
    > Em arquivo texto

(a) Associar valores aos operandos

(e) Executar expressão

(s) Sair


**6. Requisitos não-funcionais**

Os seguintes requisitos não funcionais deverão pautar todo o projeto de desenvolvimento do software:

* Documentação da estrutura de dados na forma de docstrings em Python;

* Modularização;

* Encapsulamento das funcionalidades da(s) classe(s);

* Nomes sugestivos para os métodos;

* Interação programa/usuário na exibição das mensagens do sistema (de erro ou de orientação);

* Apresentação de dados de forma organizada, na tela;

* Tratamento de erros;

* Utilizar Pilha e Fila no projeto
