def usuario():
    nome = input("Qual o seu nome? ")
    print("Seja bem-vindo,", nome,"!")
usuario()

def somar():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    soma = n1 + n2
    print('A soma dos dois números e: ', soma)

somar()

def multiplicar():
    n1 = int(input('Digite o primeiro número:' ))
    n2 = int(input('Digite o segundo número: '))
    res_mult = n1 * n2
    print('O produto dos números é: ', res_mult)

multiplicar()

def divisao_por_dois():
    n1 = float(input('Digite um número: '))
    divisao = n1 / 2
    print('A divisão do número', n1, 'por dois é: ', divisao)

divisao_por_dois()    