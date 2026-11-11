# envias/envios.py -- CODIGO HEREDADO version 1.0.0
# Este codigo es el mismo para todos. NO cambiar nada hasta la Parte 6.
# CONFIG lleno con los valores del codigo estudiantil 0182320076
# (A=3, B=2, C=0, D=0, E=7, F=6)

CONFIG = {
    "L1": 4,                  # 2 + (B mod 3) = 2 + 2
    "L2": 10,                 # 10 + C = 10 + 0
    "RECARGO_RURAL": 0.25,    # 10 + 5*(E mod 4) = 25 %
    "RECARGO_NACIONAL": 0.40, # 40 + 5*(F mod 3) = 40 %
    "DESC_VIP": 0.10,         # 10 + 5*(A mod 3) = 10 %
    "RECARGO_FINDE": 2000,    # 2000 + 500*(C mod 4) = $2.000
}


def calc(p, z, c, d, cup=None, flag=False):
    if p <= 0 or p > 45:
        raise ValueError("peso invalido")
    if z not in ("urbana", "rural", "nacional"):
        raise ValueError("zona invalida")
    if not (1 <= d <= 7):
        raise ValueError("dia invalido")
    if p <= CONFIG["L1"]:
        t = 6000
    elif p <= CONFIG["L2"]:
        t = 9000
    else:
        t = 9000 + (p - CONFIG["L2"]) * 800
    if z == "urbana":
        t = t
    elif z == "rural":
        t = t + t * CONFIG["RECARGO_RURAL"]
    elif z == "nacional":
        t = t + t * CONFIG["RECARGO_NACIONAL"]
    # fin de semana
    if d > 5:
        t = t + CONFIG["RECARGO_FINDE"]
    if c == "frecuente":
        t = t - t * 0.05
    if c == "vip":
        t = t - t * CONFIG["DESC_VIP"]
    if cup != None:
        if cup == "ENVIO10":
            t = t - t * 0.10
    if t < 5000:
        t = 5000
    if flag:
        print("costo:", t)
    return int(t / 100) * 100
