# Imprime sobrenome

nome = input("Digite seu nome.: ")
sobrenome = nome.split()

if len(sobrenome) > 1:
    print("O sobrenome digitado é .: " , sobrenome[-1])
else:
    print("Não foi digitado nome com sobrenomes")