import os

import receta
import question


def cargar_recetas():
    files = os.listdir(
        '/home/bengterik/git/linguistics_engineering/practica3/dimensiones/')
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
    files = os.listdir(
        '/home/bengterik/git/linguistics_engineering/practica3/preguntas/')
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

    exit_start_loop = False
    exit_question_loop = False

    print("\nBienvenido, aquí se puede hacer preguntas sobre recetas!")
    while not exit_start_loop:
        print("""\nA comenzar, coga uno de las siguientes opciones y pulse ENTER: 
        1. ver las recetas que son cargadas al programa
        2. ver las preguntas que puede contestar el programa
        3. empezar a preguntar
        """)
        query = input(">")

        if query == "1":
            print('\n' + '\n'.join([r.__str__() for r in recetas]))
        elif query == "2":
            print('\n' + '\n'.join([r.__str__() for r in preguntas]))
        else:
            exit_start_loop=True

    while not exit_question_loop:
        respuesta = '--------------------------------\n' + "El sistema no ha entendido su pregunta" + '\n--------------------------------\n'
        query = input("Ponga tu pregunta>")
        for p in preguntas:
            match, pregunta = p.match(query)
            if match:
                respuesta = pregunta.responder(query, recetas)
                break

        print(respuesta)
        if not match:
            preg_prepuestas = []
            for q in preguntas:
                preg_prepuestas.append((q.similaridad(query), q.__str__().strip('<>')))
            similaridad = sorted(preg_prepuestas, key=lambda x: x[0], reverse=True)
            print(f"""Las preguntas más similares a la hecha son:
          1. {similaridad[0][1]}
          2. {similaridad[1][1]}
          3. {similaridad[2][1]}
                          """
                  )
