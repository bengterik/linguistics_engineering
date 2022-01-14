class Question:
    def __init__(self, question_variants, domain, q_range):
        self.question_variants = question_variants
        self.domain = domain
        self.range = q_range

    def answer(self, query, dimension, dimensions):
        for r in recetas:
            for d in dimensions.get_domain(dimension):
                if query.contains(d):
                    return "si"

    def match(self, question):
        for q in self.question_variants:
            if q.equals(question):
                return True, q
        return False, q

    def __str__(self):
        return self.question_variants[0]
