from random import randint
barra = "="
barra2 = "-"
habilidadeInicial = (randint(1,6)) + 6
energiaInicial = (randint(1,6)) + (randint(1,6)) + 12
sorteInicial = (randint(1,6)) + 6

config = {
    "sistema" : True,
    "start" : True
}

personagem = {
    "nome" : "sem nome",
    "habilidade" : habilidadeInicial,
    "energia" : energiaInicial,
    "sorte" : sorteInicial,
    "ouro" : 0,
    "forcaAtaque" : 0,
    "magia" : 0
}

magias = {
    "fogo" : 0,
}

giro = {
    "giro1" : 0,
    "giro2" : 0,
}