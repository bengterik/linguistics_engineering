from xml import dom
from difflib import SequenceMatcher
import unidecode

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def flatten(t):
    return [item for sublist in t for item in sublist]


class Question:
    def __init__(self, question_variants, domain, q_range):
        self.question_variants = question_variants
        self.domain = domain
        self.q_range = q_range

    def responder(self, query, recetas):
        palabras_claves = self.palabras_claves(query)
        if self.q_range == "receta":
            return self.sacar_receta(query, recetas, palabras_claves)
        elif self.q_range == "nombre":
            return self.sacar_recetas(recetas)
        else:
            return self.sacar_dimension(query, recetas, palabras_claves)

    def sacar_recetas(self, recetas):
        respuestas = []
        for r in recetas:
            respuestas.append("Receta: " + r.__str__())
        return '\nRecetas: \n--------------------------------\n' + '\n-------------------------------- \n'.join(respuestas) + '\n--------------------------------\n'

    def sacar_receta(self, query, recetas, palabras_claves):
        respuestas = []
        for r in recetas:
            for d in r.get_dimension(self.domain):
                domain_wordset = set(self.formatear(d).split(' '))
                if (palabras_claves-domain_wordset == set()):
                    respuestas.append(
                        "Receta: " + r.__str__() +
                        "\nDominio: " + self.domain +
                        "\nPalabra(s) de busqueda: " + palabras_claves.__str__().strip('{}'))

        if not respuestas:
            respuestas = [("No se ha encontrado una receta con las palabras de busqueda: " +
                           palabras_claves.__str__().strip('{}'))]

        return '--------------------------------\n' + '\n-------------------------------- \n'.join(respuestas) + '\n--------------------------------\n'

    def sacar_dimension(self, query, recetas, palabras_claves):
        respuestas = []
        for r in recetas:
            domain_wordset = set(flatten([self.formatear(s).split(' ') for s in r.get_dimension(self.domain)]))
            if (palabras_claves-domain_wordset == set()):
                respuestas.append(
                    r.__str__() + "\n" +
                    self.q_range.capitalize() + ": " + str(r.get_dimension(self.q_range)).strip('[]') +
                    "\nPalabra(s) de busqueda: " + palabras_claves.__str__().strip('{}'))

        if not respuestas:
            respuestas = [("No se ha encontrado una receta con las palabras de busqueda: " +
                           palabras_claves.__str__().strip('{}'))]
        return '--------------------------------\n' + '\n-------------------------------- \n'.join(respuestas) + '\n--------------------------------\n'

    def match(self, query):
        """Para ver si la pregunta es un 'match' se subtrae las palabras del query de la pregunta,
        y si solo queda una palabra de la pregunta se asumen corresponder"""
        palabras_query = set(self.formatear(query).split(' '))
        for pregunta in self.question_variants:
            palabras_pregunta = set(self.formatear(pregunta).split(' '))
            diferencia = palabras_pregunta.difference(palabras_query)
            if len(diferencia) == 1:
                return True, self
        return False, self

    def __str__(self):
        return self.question_variants[0]

    def palabras_claves(self, query):
        "Todos las palabras de las preguntas son subtraidas del query"
        palabras_query = set(self.formatear(query).split(' '))
        palabras_preguntas = set(flatten(
            [self.formatear(pregunta).split(' ') for pregunta in self.question_variants]))
        return palabras_query.difference(palabras_preguntas)

    def similaridad(self, query):
       preg_sim = []
       for q in self.question_variants:
           preg_sim.append((similar(query,q), q))
       return sorted(preg_sim, key=lambda x: x[0], reverse=True)[0]


    def formatear(self, pregunta):
        respuesta=unidecode.unidecode(pregunta).strip('¿?').lower()
        return respuesta