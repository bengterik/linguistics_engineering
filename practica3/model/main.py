import os

import receta
import question


def cargar_recetas():
    files = os.listdir('/home/bengterik/git/linguistics_engineering/practica3/dimensiones/')
    recetas = []
    for filename in files:
        with open('/home/bengterik/git/linguistics_engineering/practica3/dimensiones/' + filename) as f:
            lines = f.readlines()
        cleaned_lines = [[l1.strip() for l1 in l.split(',')] for l in lines]

        recetas.append(receta.Receta(cleaned_lines[0],
                                     cleaned_lines[1],
                                     cleaned_lines[2],
                                     cleaned_lines[3],
                                     cleaned_lines[4],
                                     cleaned_lines[5],
                                     cleaned_lines[6],
                                     cleaned_lines[7],
                                     cleaned_lines[8],
                                     cleaned_lines[9],
                                     cleaned_lines[10]))
    return recetas


def cargar_preguntas():
    files = os.listdir('/home/bengterik/git/linguistics_engineering/practica3/preguntas/')
    preguntas = []

    for filename in files:
        with open('/home/bengterik/git/linguistics_engineering/practica3/preguntas/' + filename) as f:
            lines2 = f.readlines()

        variants = [line.strip('\n') for line in lines2][1:]
        dom_range = lines2[0].split('-')
        domain = dom_range[0].strip('\n')
        range = dom_range[1].strip('\n')
        preguntas.append(question.Question(variants, domain, range))
    return preguntas


if __name__ == '__main__':
    recetas = cargar_recetas()
    preguntas = cargar_preguntas()

    exit_loop = False
    print("Bienvenido, aquí puede preguntar sobre sobre recetas")
    while not exit_loop:
        respuesta="No hay respuesta por esa pregunta"
        query = input("Ponga tu pregunta>")
        for p in preguntas:
            match, pregunta = p.match(query)
            if match:
                respuesta = pregunta.responder(query, recetas)
        print(respuesta)
    "¿Hay una receta con <ingrediente>?     ingrediente->receta"
    "¿Hay una receta con carne?"

    """
    for recipe in recipes:
        salteado_de_carne.<dominio>("<ingrediente>")
        salteado_de_carne.ingrediente
        salteado_de_carne.origen("<origen")

    print(salteado_de_carne)
"""


