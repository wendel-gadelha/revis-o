def calcular():
    print("---------------------")
    print("Calculadora simples")
    print("---------------------")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - divisão")
    print("0 - sair")
    print("---------------------")

    opcao = int(input("Digite a opção desejada: "))
    if(opcao > 4 or opcao <0):
        print("Opção inválida")

    else:
        primeiro_numero = float(input("Digite o primeiro número: "))
        segundo_numero = float(input("Digite o segundo número: "))

        if(opcao == 1):
            soma = primeiro_numero + segundo_numero
            print("A soma de ", primeiro_numero, "por", segundo_numero, " é: ", soma)
        elif(opcao == 2): 
            subtracao = primeiro_numero - segundo_numero
            print("A subtração de ", primeiro_numero, "por", segundo_numero, " é : ", subtracao)

        elif(opcao == 3):
            multiplicacao = primeiro_numero * segundo_numero
            print("A multiplicação de ", primeiro_numero, "por", segundo_numero, "é: ", multiplicacao)

        elif(opcao == 4):
            divisao = primeiro_numero / segundo_numero
            print("A divisao de ", primeiro_numero, "por", segundo_numero, "é: ", divisao)

        elif(opcao == 0):
            print("Obrigado por utilizar a calculadora!")

calcular()
