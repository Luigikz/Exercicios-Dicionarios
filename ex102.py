print("Bem-vindo ao programa!")
print()

pessoas = []

for i in range(10):
    nome = input(f"Informe o nome da pessoa {i + 1}: ")
    idade = int(input(f"Informe a idade de {nome}: "))

    pessoa = {"nome": nome, "idade": idade}
    pessoas.append(pessoa)

print()
print("Pessoas menores de 18 anos:")

for pessoa in pessoas:
    if pessoa["idade"] < 18:
        print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']}")

print()
print("Pessoas com 18 anos ou mais:")

for pessoa in pessoas:
    if pessoa["idade"] >= 18:
        print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']}") 