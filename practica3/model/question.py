class Question:
    def __init__(self, question_variants, answer_dimension):
        self.question_variants = question_variants
        self.answer_dimension = answer_dimension

    def answer(self):
        return ""

    def match(self, query):
        return self
