def calculate(expression: str) -> float:
    """
    Evalúa una expresión matemática con suma, resta, multiplicación o división.
    Ejemplo de uso: '5 + 2', '10 / 2'
    """

    import re

    if not expression or expression.strip() == "":
        raise ValueError("Expresión vacía")

    # Validar solo números, operadores y espacios
    if not re.fullmatch(r"[0-9\.\s\+\-\*/]+", expression):
        raise ValueError("Caracteres inválidos")

    # Validar expresiones mal formadas como '* 5' o '4 /'
    if re.search(r"(^[\+\-\*/]|\s[\+\-\*/]\s*$|[\+\-\*/]{2,})", expression):
        raise SyntaxError("Sintaxis inválida")

    try:
        resultado = eval(expression, {"__builtins__": None}, {})
        return resultado
    except ZeroDivisionError:
        raise ZeroDivisionError("División entre cero no permitida.")
    except Exception as e:
        raise ValueError(f"Error en la expresión: {e}")

# Ejemplos:
print(calculate("5 + 2"))     # ➜ 7
print(calculate("10 - 3"))    # ➜ 7
print(calculate("4 * 2"))     # ➜ 8
print(calculate("8 / 2"))     # ➜ 4.0
