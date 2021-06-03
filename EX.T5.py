def ficha(nome,gols):
    fic = nome+gols
    print(f'O nome do Jogador é: {nome} e a quantidade de gols feitos no campeonato é : {gols} gols')  

n=input('Digite o nome do Jogador: ')
g= input('Digite a quantidade de gols: ')

ficha(n,g)