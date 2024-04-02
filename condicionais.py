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

def media():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    resu_media = (nota1 + nota2) / 2
    if(resu_media >=7):
        print('Parabéns! Você foi aprovado!')
    else:
        print('Você está em recuperação.')

media()
