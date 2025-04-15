import re

def calculate(expression: str) -> float:
    if not expression or expression.strip() == "":
        raise ValueError("Expresión vacía")

    # Validar caracteres permitidos
    if not re.fullmatch(r"[0-9\.\-\*\s]+", expression):
        raise ValueError("Caracteres inválidos")

    # Validar sintaxis incorrecta como: "5 * " o "* 3"
    if re.search(r"(^\s*\*|\*\s*$|\*\s*\*)", expression):
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
