# Método de Acrescentar

with open("Texto1.txt", "a", encoding="utf-8") as arquivo:
    conteudo = arquivo.write("\nMUNDÃO")
    print(conteudo)