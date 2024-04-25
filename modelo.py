class Modelo:
    def __init__(self):#inicializar los atributos de uso de la calculadora (los parametros para calcular la energia)
        self.masa = 0
        self.altura = 0
        self.velocidad = 0
        self.energia_cinetica = 0
        self.energia_potencial = 0
        self.energia_total = 0

    def calcular_energia(self):#calcular las diferentes energias dentro del sistema
        self.energia_cinetica = 0.5 * self.masa * self.velocidad**2  #ec=1/2 * m * v^2 
        self.energia_potencial = self.masa * 9.8 * self.altura #ep= m * g * h
        self.energia_total = self.energia_cinetica + self.energia_potencial # ep + ec
