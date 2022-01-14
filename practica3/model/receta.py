class Receta:
    def __init__(self, nombre, ingrediente, origen, tipo, dificultad, dieta, precio, tiempo, herramienta, tecnica, temporada):
        self.nombre=nombre
        self.ingrediente=ingrediente
        self.origin=origen
        self.tipo=tipo
        self.dificultad=dificultad
        self.dieta=dieta
        self.precio=precio
        self.tiempo=tiempo
        self.herramienta=herramienta
        self.tecnica=tecnica
        self.temporada=temporada

    def get_dimension(self, dimension):
        if dimension.equals("ingredient"):
            return self.ingrediente
        elif dimension.equals("origin"):
            return self.origin
        elif dimension.equals("tipo"):
            return self.tipo
        elif dimension.equals("dificultad"):
            return self.dificultad
        elif dimension.equals("dieta"):
            return self.dieta
        elif dimension.equals("precio"):
            return self.precio
        elif dimension.equals("tiempo"):
            return self.tiempo
        elif dimension.equals("herramienta"):
            return self.herramienta
        elif dimension.equals("tecnica"):
            return self.tecnica
        elif dimension.equals("temporada"):
            return self.temporada
        else:
            return []

    def __str__(self):
        return self.nombre

    def get_recipe(self, value):
        return ""

    def get_values(self, recipe):
        return ""