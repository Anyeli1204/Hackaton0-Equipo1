import re

def calculate(expression: str) -> float:
    """
    Evalúa una expresión matemática segura (por ejemplo: '10 - 3').
    Lanza errores si la expresión está vacía, contiene caracteres inválidos o tiene sintaxis incorrecta.
    """

    if not expression or expression.strip() == "":
        raise ValueError("Expresión vacía")

    # Validar caracteres permitidos (números, espacios, punto decimal, operadores básicos)
    if not re.fullmatch(r"[0-9\.\-\+\*/\s]+", expression):
        raise ValueError("Caracteres inválidos")

    # Validar sintaxis incorrecta como: "* 3" o "5 *"
    if re.search(r"(^\s*[\+\-\*/]|\s*[\+\-\*/]\s*$|[\+\-\*/]{2,})", expression):
        raise SyntaxError("Expresión con sintaxis inválida")

    try:
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("División entre cero.")
    except SyntaxError:
        raise SyntaxError("Expresión con sintaxis inválida")
    except Exception:
        raise ValueError("Error de evaluación")
