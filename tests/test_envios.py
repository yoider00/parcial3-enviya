# Pruebas automatizadas (Parte 5) contra el CODIGO HEREDADO v1.0.0
# Reglas propias del estudiante (codigo 0182320076):
#   D=0 (par): tramo 1 incluye el limite -> peso <= 4
#   E=7 (impar): recargo finde DESPUES de los descuentos
#   B=2 (par): solo el MAYOR descuento
#   F=6 (par): cupon inexistente SE IGNORA
#   PMAX=45, L1=4, L2=10, RR=25%, RN=40%, V=10%, S=$2000

import pytest
from envios import calc


# ------------------------------------------------------------------
# EJEMPLOS de la tecnica "valores limite" y "particion de equivalencia".
# COMPLETA aqui tu matriz de minimo 20 casos de la Parte 3,
# con ID, y comentando el requisito y la tecnica de cada uno.
# ------------------------------------------------------------------

def test_CN_01_peso_en_L1_tramo1():  # limite L1=4, D par -> incluido, tramo 1
    assert calc(4, "urbana", "normal", 3) == 6000


def test_CN_02_sabado_tiene_recargo_finde():  # R5: sabado (d=6) y domingo (d=7)
    # esperado: 9000 + 2000 = 11000 (finde DESPUES de descuentos; sin descuentos da igual)
    assert calc(5, "urbana", "normal", 6) == 11000


def test_CN_03_solo_mayor_descuento():  # R6, regla B par: VIP 10% vs cupon 10% -> solo uno
    assert calc(4, "urbana", "vip", 3, cup="ENVIO10") == 5400  # 6000*0.90 = 5400


def test_CN_04_peso_sobre_PMAX_error():  # R1: PMAX = 45, no 50
    with pytest.raises(ValueError):
        calc(45.5, "urbana", "normal", 3)


def test_CN_05_zona_invalida_error():  # R2: zona no valida -> error
    with pytest.raises(ValueError):
        calc(5, "lunar", "normal", 3)


def test_CN_06_dia_invalido_error():  # R2: dia fuera de 1..7 -> error
    with pytest.raises(ValueError):
        calc(5, "urbana", "normal", 9)


def test_CN_07_cupon_inexistente_se_ignora():  # R7, regla F par
    assert calc(4, "urbana", "normal", 3, cup="BIENVENIDA") == 6000
