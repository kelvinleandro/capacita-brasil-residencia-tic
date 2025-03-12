lista = ["maçã", "banana", "uva"]

for idx, item in enumerate(lista):
  print(f"{idx} - {item}")

lista_pares = [num for num in range(1, 11) if num % 2 == 0]
print(f"Pares entre 1 e 10: {lista_pares}")

lista = [1, 2, 3, 4]
multiplicacao = list(map(lambda x: x * 3, lista))
print(multiplicacao)

lista = [2, 4, 6]
tuplas = [(idx, num**2) for idx, num in enumerate(lista)]
print(tuplas)