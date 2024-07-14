from enum import Enum, auto

class TipoEntrada(Enum):
    BEBE = 0
    NIÑO = 14
    ADULTO = 23
    JUBILADO = 18
    

class Entrada:
    def __init__(self, edad: int):
        self.__validate_edad(edad)
        self.__edad = edad
        
        if edad <= 2:
            self.tipo = TipoEntrada.BEBE
            self.precio = 0
        elif edad < 13:
            self.tipo = TipoEntrada.NIÑO
            self.precio = 14
        elif edad < 65:
            self.tipo = TipoEntrada.ADULTO
            self.precio = 23
        else:
            self.tipo = TipoEntrada.JUBILADO
            self.precio = 18

    def __validate_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no debe ser negativa")

class Grupo_Entrada:
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        self.tipos_entrada = {
            TipoEntrada.BEBE: {"candidad": 0, "precio": 0},
            TipoEntrada.NIÑO: {"candidad": 0, "precio": 14},
            TipoEntrada.ADULTO: {"candidad": 0, "precio": 23},
            TipoEntrada.JUBILADO: {"candidad": 0, "precio": 18}   
        }

    def add_entrada(self, edad):
        """
        En funcion de la edad, crear una entrada y incrementar el contador de entradas
        Con el precio de la entrada nueva incrementar el total
        """
        nueva_entrada = Entrada(edad)
        self.num_entradas += 1
        self.total += nueva_entrada.precio

        self.tipos_entrada[nueva_entrada.tipo]["candidad"] += 1

    def cantidad_entradas_por_tipo(self, tipo: TipoEntrada) -> int:
        return self.tipos_entrada[tipo]["candidad"]
    
    def subtotal_tipo(self, tipo: TipoEntrada) -> int:
        return self.tipos_entrada[tipo]["candidad"] * self.tipos_entrada[tipo]["precio"]