def add(n1: float, n2: float) -> float:
    return n1 + n2

def divide(n1: float, n2: float) -> float:
    if n2 != 0:
        return n1 / n2
    return "Não é possível dividir por zero."