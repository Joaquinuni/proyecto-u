class Salario:
    def __init__(self, nombre,  salario_hora, horas, dias):
        self.nombre = nombre
        self.salario_hora = salario_hora
        self.horas = horas
        self.weekdays = dias
    
    #accesadores
    def get_nombre(self):
        return self.nombre
    def get_salario_hora(self):
        return self.salario_hora
    def get_horas(self):
        return self.horas
    def get_weekdays(self):
        return self.weekdays

    #mutadores
    def set_dia(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def set_clientes(self, nuevo_salario):
        self.salario = nuevo_salario
    def set_ingresos(self, nuevo_horas):
        self.horas = nuevo_horas
    def set_gastos(self, nuevo_weekdays):
        self.weekdays = nuevo_weekdays
