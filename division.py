from fractions import Fraction

def dividir_fracciones(frac1_str, frac2_str):
    try:
        # Convertimos las cadenas a fracciones
        frac1 = Fraction(frac1_str)
        frac2 = Fraction(frac2_str)
        
        # División de fracciones: frac1 ÷ frac2
        resultado = frac1 / frac2

        print(f"{frac1} ÷ {frac2} = {resultado}")
    
    except ZeroDivisionError:
        print("Error: No se puede dividir por una fracción con numerador 0.")
    except ValueError:
        print("Error: Entrada inválida. Usa el formato 'a/b' para las fracciones.")

# Ejemplo de uso
if __name__ == "__main__":
    fraccion1 = input("Ingresa la primera fracción (por ejemplo, 3/4): ")
    fraccion2 = input("Ingresa la segunda fracción (por ejemplo, 2/5): ")
    dividir_fracciones(fraccion1, fraccion2)