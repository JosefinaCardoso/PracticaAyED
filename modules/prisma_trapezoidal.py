class PrismaTrapezoidal:
    def __init__ (self,base_mayor, base_menor, lado, altura_trapecio, altura_prisma):
        if base_mayor <= 0:
            raise ValueError("La base_mayor debe ser positivo")
        self.__base_mayor = base_mayor

        if base_menor <= 0:
            raise ValueError("La base_menor debe ser positivo")
        self.__base_menor = base_menor

        if lado <= 0:
            raise ValueError("La lado debe ser positivo")
        self.__lado = lado

        if altura_trapecio <= 0:
            raise ValueError("La altura_trapecio debe ser positivo")
        self.__altura_trapecio = altura_trapecio

        if altura_prisma <= 0:
            raise ValueError("La altura_prisma debe ser positivo")
        self.__altura_prisma = altura_prisma   
        

    @property
    def base_mayor(self):
            return self.__base_mayor

    @property
    def altura_prisma(self):
            return self.__altura_prisma

    @base_mayor.setter
    def base_mayor(self, nueva_base_mayor):
            if nueva_base_mayor <=0:
                raise ValueError("La base mayor debe  ser positiva")
                self.__base_mayor = nueva_base_mayor

    @altura_prisma.setter
    def altura_prisma(self, nueva_altura_prisma):
        if nueva_altura_prisma <=0:
            raise ValueError("La altura debe  ser positiva")
        self.__altura_prisma = nueva_altura_prisma      

    def volumen(self):
        volumen=(((self.__base_menor+self.__base_mayor)*self.__altura_trapecio)/2)*self.__altura_prisma
        return volumen

    def area_superficial(self):
        pb=self.__base_menor+self.__base_mayor+ 2*self.__lado
        area_superficial=(self.__base_menor+self.__base_mayor)*self.__altura_trapecio+(pb*self.__altura_prisma)
        return area_superficial













































# class PrismaTrapezoidal:
#     def __init__(self, base_mayor, base_menor, lado, altura_trapecio, altura_prisma):
#         if base_mayor <= 0 or base_menor <= 0 or lado <= 0 or altura_trapecio <= 0 or altura_prisma <= 0:
#             raise ValueError("Todos los valores deben ser positivos")
#         self.base_mayor = base_mayor
#         self.base_menor = base_menor
#         self.lado = lado
#         self.altura_trapecio = altura_trapecio
#         self.altura_prisma = altura_prisma
    
#     def volumen(self):
#         return (((self.base_mayor + self.base_menor) / 2) * self.altura_trapecio) * self.altura_prisma
    
#     def area_superficial(self):
#         return (self.base_mayor + self.base_menor) * self.altura_trapecio + (self.base_mayor + self.base_menor + 2 * self.lado) * self.altura_prisma