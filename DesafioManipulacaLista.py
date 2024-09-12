# Apenda e remove

frutas = ["maca", "banana", "laranja"]

adicionar = input("Que fruta deseja adicionar? ")

frutas.append(adicionar)

print(frutas)

remover = input("Qual fruta deseja remover? ")

if remover in frutas:
    frutas.remove(remover)
    print("Item removido da lista. Lista atualizada: " , frutas)
else:
    print("Fruta nao existe na lista")
