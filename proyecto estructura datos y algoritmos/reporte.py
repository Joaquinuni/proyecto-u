class Reporte:
    def __init__(self, dia, clientes ,ingresos, gastos):
        self.__dia = dia
        self.__clientes = clientes
        self.__ingresos = ingresos
        self.__gastos = gastos

        #accesadores
    def get_dia(self):
        return self.__dia
    def get_clientes(self):
        return self.__clientes
    def get_ingresos(self):
        return self.__ingresos
    def get_gastos(self):
        return self.__gastos

    #mutadores
    def set_dia(self, nuevo_dia):
        self.__dia = nuevo_dia
    def set_clientes(self, nuevo_clientes):
        self.__clientes = nuevo_clientes
    def set_ingresos(self, nuevo_ingresos):
        self.__ingresos = nuevo_ingresos
    def set_gastos(self, nuevo_gastos):
        self.__gastos = nuevo_gastos