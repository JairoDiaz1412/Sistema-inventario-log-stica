import pytest
from inventario import INVENTARIO, consultar_stock, retirar_stock


@pytest.fixture(autouse=True)
def reiniciar_inventario():
    INVENTARIO.clear()
    INVENTARIO.update({"guantes": 100, "mascarillas": 50, "jeringas": 25})


def test_consultar_stock():
    assert consultar_stock("guantes") == 100


def test_producto_inexistente():
    assert consultar_stock("desconocido") == 0


def test_retirar_stock():
    assert retirar_stock("guantes", 10) == 90


def test_stock_insuficiente():
    with pytest.raises(ValueError):
        retirar_stock("guantes", 101)


def test_cantidad_invalida():
    with pytest.raises(ValueError):
        retirar_stock("guantes", -1)
