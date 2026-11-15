"""Inventario de demostración con datos ficticios."""

INVENTARIO = {"guantes": 100, "mascarillas": 50, "jeringas": 25}


def consultar_stock(producto):
    return INVENTARIO.get(producto, 0)


def retirar_stock(producto, cantidad):
    if type(cantidad) is not int or cantidad <= 0:
        raise ValueError("La cantidad debe ser un entero positivo")
    if producto not in INVENTARIO or INVENTARIO[producto] < cantidad:
        raise ValueError("Stock insuficiente")
    INVENTARIO[producto] -= cantidad
    return INVENTARIO[producto]


if __name__ == "__main__":
    for producto, cantidad in INVENTARIO.items():
        print(f"{producto}: {cantidad} unidades")
