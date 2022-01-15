def flatten(t):
    return [item for sublist in t for item in sublist]


class Question:
    def __init__(self, question_variants, domain, q_range):
        self.question_variants = question_variants
        self.domain = domain
        self.q_range = q_range

    def responder(self, query, recetas):
        palabra_clave = self.palabra_clave(query)
        if self.q_range == "receta":
            return self.sacar_receta(query,recetas, palabra_clave)
        else:
            return self.sacar_dimension(query,recetas, palabra_clave)

    def sacar_receta(self, query, recetas, palabra_clave):
        for r in recetas:
            for d in r.get_dimension(self.domain):
                if palabra_clave in d:
                    return \
                        "Receta: " +r.__str__() + "\nPalabra clave: " + palabra_clave
        return "No ha encontrado una receta"

    def sacar_dimension(self, query, recetas):
        #receta = recetas.
        #dimension = r.get_dimension(self.domain)
        return ""


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

    def palabra_clave(self, query):
        "Todos las palabras de las preguntas son subtraidas del query"
        palabras_query = set(query.strip('¿?').split(' '))
        palabras_preguntas = set(flatten([pregunta.strip('¿?').split(' ') for pregunta in self.question_variants]))
        return next(iter(palabras_query.difference(palabras_preguntas)))




