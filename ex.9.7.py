class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def tipo_triangulo(self):
        try:
            if self.lado1 <= 0 or self.lado2 <= 0 or self.lado3 <= 0:
                raise ValueError("Os lados do triângulo devem ter valores positivos.")
            elif self.lado1 + self.lado2 <= self.lado3 or self.lado1 + self.lado3 <= self.lado2 or self.lado2 + self.lado3 <= self.lado1:
                raise ValueError("Os lados do triângulo não formam um triângulo válido.")
            elif self.lado1 == self.lado2 == self.lado3:
                return "Triângulo equilátero"
            elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                return "Triângulo isósceles"
            else:
                return "Triângulo escaleno"
        except ValueError as e:
            return str(e)

triangulo1 = Triangulo(3, 3, 3)  
print(triangulo1.tipo_triangulo())

triangulo2 = Triangulo(3, 4, 4)  
print(triangulo2.tipo_triangulo())

triangulo3 = Triangulo(3, 4, 5)  
print(triangulo3.tipo_triangulo())

triangulo4 = Triangulo(0, 2, 3)  
print(triangulo4.tipo_triangulo())
