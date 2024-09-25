"""Requisitos funcionais:
Menu principal:
Calculadora simples
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
s. Sair

Deve escolher a operação utilizadndo os números referentes à opção do menu e apertar ENTER.
Um vez escolhida a operação, a aplicação deverá solicitar dois números e xecutar a operação selecionada sobre eles.
IMPORTANTE: Precisamos nos atentar às divisẽs por zero.

Entrada:
"Primeiro número: "
"Segundo número: "

Saída:
O resultado da [Operação selecionada] é: [resultado]
Ex: "O resultado da operação SOMA é: 42"

Quando a operação for finalizada, deverá voltar ao menu principal.
Se o usuário pressionar s, o aplicativo deverá agradecer o usuário e sair. """
from symbol import continue_stmt


def calculadora(): #para definir a função
    while True: #O loop sempre vai executar
        print("Calculadora simples")
        print() #vai pular uma linha
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. Sair")
        operacao = input("Selecione uma opção do menu ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print("Obrigada por utilizar a calculadora simples!")
            break #BREAK finaliza a execução de qualquer loop não importa onde ele esteja

        if operacao not in ['1','2','3','4']: #Vai verificar se a opção digitada pelo usuáio não está dentro da coleção. Se não está ele deve mostrar uma mensagem e reiniciar"""
            print("Opção inválida! Tente novamente.")
            continue #Vai voltar no começo do loop.

        numero_1 = float(input("Primeiro número: "))
        numero_2 = float(input("Segundo número: "))

        if operacao =='1':
            resultado = numero_1 + numero_2
            print("O resultado da operação SOMA é: ", resultado)

        elif operacao == '2': #ELIF - caso contrário SE
            resultado = numero_1 - numero_2
            print("O resultado da operação SUBTRAÇÃO é: ", resultado)

        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("O resultado da operação MULTIPLICAÇÃO é: ", resultado)

        else:
            if numero_2 == 0:
                print("Divisões por zero não são possíveis. Tente novamente.")
                continue
            else:
                resultado = numero_1 / numero_2
                print("O resultado da operação DIVISÃO é: ", resultado)

calculadora() #para executar (chamar) a função