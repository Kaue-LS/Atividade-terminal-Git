# matriz=list()

# for i in range(0,3):
#     lista=list()
#     lista.append(int(input("Informe um numero 1: ")))
#     lista.append(int(input("Informe um numero 2: ")))
#     lista.append(int(input("Informe um numero 3: ")))
#     matriz.append(lista[:])

# print(f"""
# {matriz[0]}
# {matriz[1]}
# {matriz[2]}

        
#         """)


# lista=[]

# for x in range(1,10):
#     num= float(input(f'Digite o {x}° numero: '))
#     lista.append(num)
    
# for linha in range(3):
#     print('')
#     for coluna in range(3):
#         print(f'[{lista[(linha+coluna) + (2*linha)]}]', end='')
# print('')



matriz=[[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f"Digite um valor:[{l},{c}] "))
        #se colocar no [] numero fixo, ele vai por na posição, assim ele vai em cada um

#print(matriz)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')# end nao pula linha
    print()#pula linha# o : cria formatação e o ^5 cria 5 espaços a cada linha e coluna, faz ficar bonito
    #todo print tem um barra invertida n implicito