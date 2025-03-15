from random import randint
from xml.dom.minidom import ProcessingInstruction

from dados import *

def start():
    on = True
    while on == True:
        print(barra*25)
        print("    A cidadela do caos")
        print("--------BEM-VINDO--------")
        print("[1] START")
        print("[2] EXIT")
        config["start"] = int(input("Opção: "))

        if config["start"] == True or config["start"] == False:
            if config["start"] == 1:
                on = False
            else:
                config["sistema"] = False
        print(barra*25)

def definicaoInicial():
    print(barra*25)
    print("Primeiro temos que definir\na sua habilidade, energia e sorte")
    print("Para definir a habilidade\nTem que jogar um dado\ne somar o valor com 6\nesse será a sua habilidade")
    print(barra2*25)
    print("vamos gira o dado de habilidade")
    girarDado()
    print("dado:",giro["giro1"])
    defInicial["habiInicial"] = giro["giro1"] + 6
    print("HABILIDADE:",defInicial["habiInicial"])

def folhaAventuras():
    print(barra*20)
    print("NOME:",personagem["nome"],"\n" + barra2*20)
    print("HABILIDADE:",personagem["habilidade"])
    print("ENERGIA:",personagem["energia"])
    print("SORTE:",personagem["sorte"],"\n" + barra2*20)
    print("OURO:",personagem["ouro"])
    print("MAGIA:",personagem["magia"])
    print(barra*20)
    print()

def girarDado():
    on = True
    while on:
        print(barra*25)
        dado = int(input("[1] para jogar 1 dado\n[2] para jogar 2 dados\nDigite a opção:"))
        print(barra*25)
        print()
        if dado == 1 or dado == 2:
            giro1 = randint(1,6)
            giro2 = randint(1, 6)
            if dado == 1:
                giro["giro1"] = giro1
                giro["giro2"] = 0
            elif dado == 2:
                giro["giro1"] = giro1
                giro["giro2"] = giro2
            on = False
        else:
            pass

def combate():
    print(barra*25)
    print("Para começar a batalha 1°\nvamos definir a força de ataque:")
    print("Para definir a força de ataque você deve\ngirar dois dados, e somar esses valores\njuntos com a sua habilidade atual")
    print(barra2*25)
    print("vamos gira os dados ")
    girarDado()
    personagem["forcaAtaque"] = giro["giro2"] + giro["giro2"] + personagem["habilidade"]

def fim():
    print("FIM DE JOGO")



