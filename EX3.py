# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo sa estrutura na tela. A média para aprovação é 7.
#  Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.

situacao=dict()
aluno=list()
for i in range(0,1):
    situacao['nome']=str(input("Informe o nome: "))
    situacao['media']=float(input('Informe a media final : '))
    if situacao['media']>=7:
        situacao.setdefault('situacao','Aprovado(a)') 
    elif 5<=situacao['media']<=6.9:
        situacao.setdefault('situação','Recuperação')
    else:
        situacao.setdefault('situação','reprovado(a)')
    aluno.append(situacao.copy())
print(situacao)