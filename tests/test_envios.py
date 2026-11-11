# Suite automatizada (Parte 5) - matriz de casos de caja negra + caja blanca
# Ejecutar contra el CODIGO HEREDADO v1.0.0 para revelar defectos.
# Especificacion propia (codigo 0182320076):
#   PMAX=45, L1=4 (incluido, D par), L2=10 (incluido), RR=25%, RN=40%, V=10%, S=$2000
#   E impar: finde DESPUES de descuentos | B par: solo el MAYOR descuento
#   F par: cupon inexistente SE IGNORA | R8: min $5000, redondeo a $100 (50 arriba)

import pytest

from envios import calc


# ---------------- Valores limite y particiones de peso (R1, R3) ----------------

def test_CN_01_peso2_tramo1():
    assert calc(2, "urbana", "normal", 3) == 6000

def test_CN_02_L1_incluido():
    assert calc(4, "urbana", "normal", 3) == 6000

def test_CN_03_L1_mas_epsilon():
    assert calc(4.01, "urbana", "normal", 3) == 9000

def test_CN_04_L2_incluido():
    assert calc(10, "urbana", "normal", 3) == 9000

def test_CN_05_proporcional_interior():
    assert calc(10.5, "urbana", "normal", 3) == 9400

def test_CN_06_PMAX_incluido_45kg():
    assert calc(45, "urbana", "normal", 3) == 37000

def test_CN_07_PMAX_mas_epsilon_error():
    with pytest.raises(ValueError):
        calc(45.01, "urbana", "normal", 3)

def test_CN_08_peso_cero_error():
    with pytest.raises(ValueError):
        calc(0, "urbana", "normal", 3)

def test_CN_09_peso_0_1():
    assert calc(0.1, "urbana", "normal", 3) == 6000

# ---------------- Particiones de zona (R4, R2) ----------------

def test_CN_10_zona_rural_25():
    assert calc(2, "rural", "normal", 3) == 7500

def test_CN_11_zona_nacional_40():
    assert calc(2, "nacional", "normal", 3) == 8400

def test_CN_12_zona_invalida_error():
    with pytest.raises(ValueError):
        calc(2, "lunar", "normal", 3)

# ---------------- Particiones de dia (R2, R5) ----------------

def test_CN_13_dia_cero_error():
    with pytest.raises(ValueError):
        calc(2, "urbana", "normal", 0)

def test_CN_14_dia_ocho_error():
    with pytest.raises(ValueError):
        calc(2, "urbana", "normal", 8)

def test_CN_15_sabado_con_finde():
    assert calc(2, "urbana", "normal", 6) == 8000

def test_CN_16_domingo_con_finde():
    assert calc(2, "urbana", "normal", 7) == 8000

def test_CN_26_domingo_vip_finde_despues():
    # regla E impar: finde DESPUES del descuento -> 6000*0.90 + 2000 = 7400
    assert calc(2, "urbana", "vip", 7) == 7400

# ---------------- Descuentos, cupon y finde (R5, R6, R7) ----------------

def test_CN_17_cliente_frecuente_5():
    assert calc(2, "urbana", "frecuente", 3) == 5700

def test_CN_18_cliente_vip_10():
    assert calc(2, "urbana", "vip", 3) == 5400

def test_CN_19_cupon_envio10():
    assert calc(2, "urbana", "normal", 3, cup="ENVIO10") == 5400

def test_CN_20_vip_mas_cupon_solo_el_mayor():
    # B par: solo el mayor -> 5400; el heredado encadena y activa el minimo
    assert calc(2, "urbana", "vip", 3, cup="ENVIO10") == 5400

def test_CN_21_frecuente_mas_cupon_el_mayor():
    assert calc(2, "urbana", "frecuente", 3, cup="ENVIO10") == 5400

def test_CN_22_sabado_vip_cupon():
    assert calc(2, "urbana", "vip", 6, cup="ENVIO10") == 7400

def test_CN_23_cupon_inexistente_se_ignora():
    assert calc(2, "urbana", "normal", 3, cup="BIENVENIDA") == 6000

# ---------------- Integracion y redondeo (R3, R4, R5, R6, R8) ----------------

def test_CN_24_caso_integracion_ejemplo():
    assert calc(4, "rural", "vip", 6, cup="ENVIO10") == 8800

def test_CN_25_redondeo_50_hacia_arriba():
    # 9000*1.25 = 11250 -> 11300 (R8); el heredado trunca a 11200
    assert calc(10, "rural", "normal", 3) == 11300

# ---------------- Caja blanca: cambio de interfaz (flag eliminado) ----------------

def test_CW_01_flag_eliminado_de_la_interfaz():
    # v2.0.0: el parametro flag fue eliminado del contrato de calc.
    # Enviarlo ahora debe fallar rapido (TypeError), no ignorarse en silencio.
    with pytest.raises(TypeError):
        calc(2, "urbana", "normal", 3, flag=True)

# ---------------- Solicitud de cambio 0: zona insular (CHG-001) ----------------
# Nueva zona insular (San Andres) con recargo del 70 %.
# Los envios insulares NO aceptan cupon (se ignora, coherente con F par).

def test_CN_27_zona_insular_recargo_70():
    # 6000 * 1.70 = 10200
    assert calc(2, "insular", "normal", 3) == 10200

def test_CN_28_insular_no_acepta_cupon():
    # el cupon se ignora: 6000 * 1.70 = 10200 (NO 9180)
    assert calc(2, "insular", "normal", 3, cup="ENVIO10") == 10200

def test_CN_29_insular_vip_sabado():
    # 9000*1.70 = 15300; vip 10% -> 13770; finde despues +2000 -> 15770; redondeo -> 15800
    assert calc(10, "insular", "vip", 6) == 15800
