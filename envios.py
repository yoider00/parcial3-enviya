# envias/envios.py -- version 2.0.0 refactorizada (Parte 6)
# Codigo estudiantil 0182320076: PMAX=45, L1=4 (incluido), L2=10 (incluido),
# RR=25 %, RN=40 %, V=10 %, S=$2.000 | E impar: finde despues de descuentos
# | B par: solo el mayor descuento | F par: cupon inexistente se ignora

from abc import ABC, abstractmethod

# ---- Constantes de negocio (antes numeros magicos) ----
PESO_MAXIMO = 45            # PMAX = 30 + 5*A
TARIFA_TRAMO1 = 6000        # R3
TARIFA_TRAMO2 = 9000        # R3
EXTRA_POR_KG_SOBRE_L2 = 800  # R3, proporcional
COSTO_MINIMO = 5000         # R8
REDONDEO = 100              # R8, multiplo
DESC_FRECUENTE = 0.05       # R6
DESC_CUPON_ENVIO10 = 0.10   # R6
FIN_DE_SEMANA = (6, 7)      # sabado y domingo (R5)

CONFIG = {
    "L1": 4,                  # 2 + (B mod 3) = 2 + 2
    "L2": 10,                 # 10 + C = 10 + 0
    "RECARGO_RURAL": 0.25,    # 10 + 5*(E mod 4) = 25 %
    "RECARGO_NACIONAL": 0.40, # 40 + 5*(F mod 3) = 40 %
    "DESC_VIP": 0.10,         # 10 + 5*(A mod 3) = 10 %
    "RECARGO_FINDE": 2000,    # 2000 + 500*(C mod 4) = $2.000
}


# ---- Patron Estrategia: recargo por zona (antes if/elif encadenados) ----

class RecargoZona(ABC):
    @abstractmethod
    def aplicar(self, costo):
        """Devuelve el costo con el recargo de la zona."""


class ZonaUrbana(RecargoZona):
    def aplicar(self, costo):
        return costo


class ZonaRural(RecargoZona):
    def aplicar(self, costo):
        return costo + costo * CONFIG["RECARGO_RURAL"]


class ZonaNacional(RecargoZona):
    def aplicar(self, costo):
        return costo + costo * CONFIG["RECARGO_NACIONAL"]


ESTRATEGIA_ZONA = {
    "urbana": ZonaUrbana(),
    "rural": ZonaRural(),
    "nacional": ZonaNacional(),
}


def _validar_entradas(p, z, d):
    """R1 y R2: peso, zona y dia."""
    if p <= 0 or p > PESO_MAXIMO:
        raise ValueError("peso invalido")
    if z not in ESTRATEGIA_ZONA:
        raise ValueError("zona invalida")
    if not (1 <= d <= 7):
        raise ValueError("dia invalido")


def _tarifa_base(p):
    """R3: tramos segun L1 y L2 (ambos incluidos segun mi regla D par)."""
    if p <= CONFIG["L1"]:
        return TARIFA_TRAMO1
    if p <= CONFIG["L2"]:
        return TARIFA_TRAMO2
    return TARIFA_TRAMO2 + (p - CONFIG["L2"]) * EXTRA_POR_KG_SOBRE_L2


def _descuento_maximo(c, cup):
    """R6 con mi regla B par: solo el mayor de los descuentos disponibles."""
    descuento = 0.0
    if c == "frecuente":
        descuento = max(descuento, DESC_FRECUENTE)
    elif c == "vip":
        descuento = max(descuento, CONFIG["DESC_VIP"])
    if cup == "ENVIO10":  # mi regla F par: cupon inexistente se ignora
        descuento = max(descuento, DESC_CUPON_ENVIO10)
    return descuento


def _aplicar_finde(costo, d):
    """R5 con mi regla E impar: el recargo va despues de los descuentos."""
    if d in FIN_DE_SEMANA:
        return costo + CONFIG["RECARGO_FINDE"]
    return costo


def _con_minimo_y_redondeo(costo):
    """R8: minimo $5.000 y redondeo al multiplo de $100 con $50 hacia arriba."""
    if costo < COSTO_MINIMO:
        costo = COSTO_MINIMO
    return int(costo / REDONDEO + 0.5) * REDONDEO


def calc(p, z, c, d, cup=None):
    """Calcula el costo de un envio segun la especificacion R1-R8."""
    _validar_entradas(p, z, d)
    costo = _tarifa_base(p)
    costo = ESTRATEGIA_ZONA[z].aplicar(costo)
    costo = costo * (1 - _descuento_maximo(c, cup))
    costo = _aplicar_finde(costo, d)
    return _con_minimo_y_redondeo(costo)
