from main import sumar, restar, multiplicar, dividir
import pytest

def test_sumar():
    assert sumar(2, 3) == 5

def test_restar():
    assert restar(5, 3) == 2

def test_multiplicar():
    assert multiplicar(4, 3) == 12

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(5, 0)

