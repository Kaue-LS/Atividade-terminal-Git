lista=[5,7,2,9,4,1,3]
print(lista)

print(f'O tamanho da lista: {len(lista)}')
print(f'O maior valor: {max(lista)}')
print(f'O maior valor: {min(lista)}')
print(f'A soma de todos os valores: {sum(lista)}')
print(f'Lista em ordem crescente{sorted(lista)}')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente{lista}')
