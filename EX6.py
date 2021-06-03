# DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em
#  um dicionário e todos os dicionários em uma lista. No final, mostre:​
# A) Quantas pessoas estão cadastradas.​
# B) A média da idade.​
# C) Uma lista com as mulheres.​
# D) Uma lista com as idades que estão acima da média.​
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar
#  a resposta seja somente sim ou não.​

cadastro=dict()
preecher=list()
resp=str
resp=input("deseja começar: [Sim/Nao] ")
cont=0

somaidade=list()
Fem=list()
idadeac=list()

while resp=='sim' or resp=='Sim':
    cadastro['Nome']= str(input("Informe seu nome: ")).capitalize()
    
    cadastro['Sexo']= int(input("Informe seu sexo:[1=M/2=F]:  "))
    if cadastro['Sexo']==2:
         Fem.append(cadastro['Nome'])
    if not cadastro['Sexo']==1 and not cadastro['Sexo']==2:

        cadastro['Sexo']= int(input("Informe seu sexo:[1=M/2=F]  "))

    cadastro['idade']=int(input("Informe sua idade: "))
    somaidade.append(cadastro['idade'])
    
    cont+=1
    resp=input('deseja continuar?:[Sim/Nao] ')
    if resp=='Nao' or resp=='nao':
        break
    preecher.append(cadastro.copy())

for i in somaidade:
    soma=sum(somaidade)
    result=soma/len(somaidade)
    if i>result:
        somaidade.sort()
        idadeac.append(max(somaidade))

print(f"O total de pessoas cadastradas : {cont}")
print(f"A media de todas as idades é {result:.2f}")
print(f'As mulheres cadastradas foram: {Fem}')
print(f'As idade acima da media são {idadeac}')