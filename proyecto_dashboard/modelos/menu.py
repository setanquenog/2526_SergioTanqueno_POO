class Menu:
    """
    Modelo que representa las unidades disponibles en el dashboard
    """
    def __init__(self):
        self.unidades = {
            '1': 'Unidad 1',
            '2': 'Unidad 2'
        }

    def obtener_unidades(self):
        return self.unidades