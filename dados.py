from random import randint
barra = "="
barra2 = "-"

defInicial = {
    "habiInicial" : 0,
    "enerInicial" : 0,
    "sortInicial" : 0,
    "ouroInicial" : 0
}

config = {
    "sistema" : True,
    "start" : True
}

personagem = {
    "nome" : "sem nome",
    "habilidade" : defInicial["habiInicial"],
    "energia" : defInicial["enerInicial"],
    "sorte" : defInicial["sortInicial"],
    "ouro" : defInicial["ouroInicial"],
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