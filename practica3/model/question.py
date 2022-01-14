class Question:
    def __init__(self, question_variants, domain, q_range):
        self.question_variants = question_variants
        self.domain = domain
        self.range = q_range

    def answer(self, query, recetas):
        for r in recetas:
            for d in r.get_dimension(self.domain):
                if d in query:
                    return "Sí, la receta " + r.__str__() + " contiene " + d
        return "No hay"

    def match(self, question):
        palabras_query = set(question.strip('¿').strip('?').split(' '))
        for q in self.question_variants:
            palabras_pregunta = set(q.strip('¿').strip('?').split(' '))
            diferencia = palabras_query.symmetric_difference(palabras_pregunta)
            if len(diferencia) == 1:
                return True, self
        return False, self

    def __str__(self):
        return self.question_variants[0]

    def palabra_clave(self, query, pregunta):
        palabras_query = set(query.strip('¿').strip('?').split(' '))
        palabras_pregunta = set(pregunta.strip('¿').strip('?').split(' '))
        diferencia = palabras_query.symmetric_difference(palabras_pregunta)

#palabras_query = set(querysplit(' '))