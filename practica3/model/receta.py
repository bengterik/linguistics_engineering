class Receta:
    def __init__(self, nombre, ingrediente, origen, tipo, dificultad, dieta, precio, tiempo, herramienta, tecnica, temporada):
        self.nombre = nombre
        self.ingrediente = ingrediente
        self.origen = origen
        self.tipo = tipo
        self.dificultad = dificultad
        self.dieta = dieta
        self.precio = precio
        self.tiempo = tiempo
        self.herramienta = herramienta
        self.tecnica = tecnica
        self.temporada = temporada

    def get_dimension(self, dimension):
        if dimension == "nombre":
            return self.nombre
        elif dimension == "ingrediente":
            return self.ingrediente
        elif dimension == "origen":
            return self.origen
        elif dimension == "tipo":
            return self.tipo
        elif dimension == "dificultad":
            return self.dificultad
        elif dimension == "dieta":
            return self.dieta
        elif dimension == "precio":
            return self.precio
        elif dimension == "tiempo":
            return self.tiempo
        elif dimension == "herramienta":
            return self.herramienta
        elif dimension == "tecnica":
            return self.tecnica
        elif dimension == "temporada":
            return self.temporada
        else:
            return []

    def __str__(self):
        return self.nombre[0]

    def get_recipe(self, value):
        return ""

    def get_values(self, recipe):
        return ""
