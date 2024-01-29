import unittest

class TestSuma(unittest.TestCase):

    def test_suma_positiva(self):
        self.assertEqual((2 + 3), 5)

    def test_suma_negativa(self):
        self.assertEqual((-1 + 1), 0)

    def test_suma_cero(self):
        self.assertEqual((0 + 0), 0)


def funciones_codigos_retorno_division(numerador, denominador):
    if(denominador == 0):
        return -404
    
    return numerador / denominador

print(funciones_codigos_retorno_division(20, 0))
print(funciones_codigos_retorno_division(20, 5))

def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador 
        print(resultado)

    except ZeroDivisionError:
        print("Error!! No puedes dividir entre cero.")

    except Exception as e:
        print(f"Error inesperado!!! {e}")

dividir(10, 2) 
dividir(5, 0)
dividir(8, 'dos')


unittest.main()
