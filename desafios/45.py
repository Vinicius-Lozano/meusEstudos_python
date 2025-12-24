from random import choice 
from cores import cores

print(cores["verde"] + "-=" * 50)
print(f"{' Pedra Papel ou Tesoura ':=^100}")
print("-=" * 50 + cores["limpa"])

Jogo = ["pedra", "papel", "tesoura"]

ply = input(cores["azul"] + "Pedra, Papel ou Tesoura?: " + cores["verde"]).lower()

if ply not in Jogo:
    print(cores["vermelho"], "Escolha invalida Tente: pedra, papel ou tesoura", cores["limpa"])
    
npc = choice(Jogo)
#print("NPC Roll: " + npc)

print(cores["azul"])
print("O Player escoclheu: " + cores["verde"] + ply + cores["azul"] + " O computador escolheu: " + cores["verde"] + npc + cores["azul"] + " Portanto ")

if ply == "pedra":
    if npc == "papel":
        print("Player Perde")
    elif npc == "tesoura":
        print("Player Ganha")
    else:
        print("Draw")

if ply == "papel":
    if npc == "tesoura":
        print("Player Perde")
    elif npc == "pedra":
        print("Player Ganha")
    else:
        print("Draw")

if ply == "tesoura":
    if npc == "pedra":
        print("Player Perde")
    elif npc == "papel":
        print("Player Ganha")
    else:
        print("Draw")