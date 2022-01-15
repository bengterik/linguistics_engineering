from xml import dom


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
        else:
            return self.sacar_dimension(query, recetas, palabras_claves)

    def sacar_receta(self, query, recetas, palabras_claves):
        respuestas = []
        for r in recetas:
            for d in r.get_dimension(self.domain):
                domain_wordset = set(d.split(' '))
                if palabras_claves == domain_wordset:
                    respuestas.append(
                        "Receta: " + r.__str__() + "\nPalabra(s) de busqueda: " + palabras_claves.__str__().strip('{}'))

        if not respuestas:
            respuestas = [("No se ha podido encontrar ninguna receta con las palabras de busqueda: " +
                           palabras_claves.__str__().strip('{}'))]

        return '--------------------------------\n' + '\n-------------------------------- \n'.join(respuestas) + '\n--------------------------------\n'

    def sacar_dimension(self, query, recetas, palabras_claves):
        respuestas = []
        for r in recetas:
            domain_wordset = set(r.__str__().split(' '))
            if (palabras_claves-domain_wordset == set()):
                respuestas.append(
                    self.q_range.capitalize() + ": " + str(r.get_dimension(self.q_range)).strip('[]') +
                    "\nPalabra(s) de busqueda: " + palabras_claves.__str__().strip('{}'))

        if not respuestas:
            respuestas = [("No se ha podido encontrar ninguna receta con las palabras de busqueda: " +
                           palabras_claves.__str__().strip('{}'))]
        return '--------------------------------\n' + '\n-------------------------------- \n'.join(respuestas) + '\n--------------------------------\n'

    def match(self, query):
        """Para ver si la pregunta es un 'match' se subtrae las palabras del query de la pregunta,
        y si solo queda una palabra de la pregunta se asumen corresponder"""
        palabras_query = set(query.strip('¿?').split(' '))
        for pregunta in self.question_variants:
            palabras_pregunta = set(pregunta.strip('¿?').split(' '))
            diferencia = palabras_pregunta.difference(palabras_query)
            if len(diferencia) == 1:
                return True, self
        return False, self

    def __str__(self):
        return self.question_variants[0]

    def palabras_claves(self, query):
        "Todos las palabras de las preguntas son subtraidas del query"
        palabras_query = set(query.strip('¿?').split(' '))
        palabras_preguntas = set(flatten(
            [pregunta.strip('¿?').split(' ') for pregunta in self.question_variants]))
        return palabras_query.difference(palabras_preguntas)
