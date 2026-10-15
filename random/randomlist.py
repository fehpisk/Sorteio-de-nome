import random

participantes = ["Amanda", "Bruna", "Carlos", "Danilo", "Eliana"]

print("Participantes do sorteio:")
for nome in participantes:
 print("-", nome)

while True:
 resposta = input("\n Deseja adicionar um novo participante? ")

 if resposta in ["não", "Não"]:
        break
    
 if resposta in ["sim", "Sim"]:
        novo_nome = input("Digite o nome do participante: ")

participantes.append ( novo_nome )

print("Participantes do sorteio:")
for nome in participantes:
 print("-", nome)


sorteado = random.choice(participantes)

print("\nResultado do sorteio:")
print("E o participante sorteado foi...", sorteado)