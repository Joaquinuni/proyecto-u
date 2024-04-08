class Salario:
    def __init__(self, nombre,  salario_hora, horas, dias):
        self.nombre = nombre
        self.salario_hora = salario_hora
        self.horas = horas
        self.dias = dias
    
    def salario(self):
        print("Nombre del trabajador")
        print("Salario por hora")
        print("Horas trabajadas al dia")
        print("Dias a la semana")

