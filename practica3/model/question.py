class Question:
    def __init__(self, question_variants, domain, q_range):
        self.question_variants = question_variants
        self.domain = domain
        self.q_range = q_range

    def responder(self, query, recetas):
        if self.q_range == "receta":
            return self.sacar_receta(query,recetas)
        else:
            return self.sacar_dimension(query,recetas)

    def sacar_receta(self, query, recetas):
        for r in recetas:
            for d in r.get_dimension(self.domain):
                if d in query:
                    return "Receta: " + r.__str__()
        return "No hay receta"

    #def sacar_dimension(self):


    def match(self, query):
        """Para ver si la pregunta es un 'match' se subtrae las palabras del query de la pregunta,
        y si solo queda una palabra de la pregunta se asumen corresponder"""
        palabras_query = set(query.strip('¿?').split(' '))
        print(palabras_query)
        for pregunta in self.question_variants:
            palabras_pregunta = set(pregunta.strip('¿?').split(' '))
            print(palabras_pregunta)
            diferencia = palabras_pregunta.difference(palabras_query)
            print(diferencia)
            if len(diferencia) == 1:
                return True, self
        return False, self

    def __str__(self):
        return self.question_variants[0]

""""
    def palabra_clave(self, query, pregunta, receta):
        palabras_query = set(query.strip('¿?').split(' '))
        palabras_pregunta = set(pregunta.strip('¿?').split(' '))
        ingredient = palabras_query.difference(palabras_pregunta)
        dimension_name = next(iter(palabras_pregunta.difference(palabras_query))).strip('<>')
        dimension = receta.get_dimension(dimension_name)

        for  in dimension:
            if ingredient
"""





