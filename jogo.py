from funcoes import *
from dados import *
from random import randint


definicaoInicial()
folhaAventuras()


if personagem["habilidade"] > dInicial["habiInicial"]:
    while personagem["habilidade"] != dInicial["habiInicial"]:
        print(personagem["habilidade"]) #linha usada para teste
        personagem["habilidade"] = personagem["habilidade"] - 1
