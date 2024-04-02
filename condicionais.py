def maior_de_idade():
    idade = int(input('Informe sua idade: '))
    if(idade >= 18):
        print("Você é maior de idade!")
    else:
        print("Você é menor de idade.")
maior_de_idade()

def par_ou_impar():
    n1 = float(input('Digite um número: '))
    resto = n1 % 2
    if(resto == 0):
        print('O número informado é par!')
    else:
        print('O número informado é ímpar')
par_ou_impar()