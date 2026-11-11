# Parcial 3 - Ingeniería de Software I - EnvíaYa

**Estudiante:** (tu nombre aquí)
**Código estudiantil:** 0182320076
**Grupo B1 · VI semestre · 2026-2 · Tercer corte**

---

## Mis parámetros

Últimos 6 dígitos: **3 2 0 0 7 6** → A=3, B=2, C=0, D=0, E=7, F=6

| A | B | C | D | E | F | PMAX | L1 | L2 | RR | RN | V | S | CAMBIO |
|---|---|---|---|---|---|------|----|----|----|----|---|---|--------|
| 3 | 2 | 0 | 0 | 7 | 6 | 45 kg | 4 kg | 10 kg | 25 % | 40 % | 10 % | $2.000 | 0 |

**Reglas personalizadas:**
- D = 0 (par) → Tramo 1 **incluye** el límite: `peso ≤ 4`
- E = 7 (impar) → Recargo de fin de semana **después** de los descuentos
- B = 2 (par) → Solo se aplica **el mayor** descuento
- F = 6 (par) → Cupón inexistente **se ignora**
- CAMBIO = 0 → Parte 8: Nueva zona insular (San Andrés), +70 %, sin cupón

---

## Parte 1 · Requisitos y criterios de aceptación (0,4 pts)

### Especificación R1–R8 (con mis números)

- **R1:** 0 < peso ≤ **45** kg; si no, error "peso inválido".
- **R2:** zona ∈ {urbana, rural, nacional}; día ∈ 1..7; si no, error.
- **R3:** Tramo 1 (peso ≤ **4**, incluido): $6.000. Tramo 2 (4 < peso ≤ **10**, incluido): $9.000. Peso > 10: $9.000 + $800 × (peso − 10), proporcional.
- **R4:** Rural: +**25 %**. Nacional: +**40 %**. Urbana: sin recargo.
- **R5:** Sábado (6) y domingo (7): +**$2.000**, sumado **después** de los descuentos (E impar).
- **R6:** Frecuente: 5 %. VIP: **10 %**. Cupón ENVIO10: 10 %. Con dos: solo **el mayor** (B par).
- **R7:** Cupón inexistente: **se ignora** (F par).
- **R8:** Costo mínimo $5.000. Redondeo al múltiplo de $100 más cercano; $50 hacia arriba.

### Historias de usuario (Dado / Cuando / Entonces)

**HU1 · Costo por peso del paquete (cubre R1, R3, R8)**
Como cliente de EnvíaYa, quiero que el costo de mi envío dependa del peso del
paquete en tramos, para pagar exactamente lo que corresponde a su tamaño.

Criterios de aceptación:
- **Dado** un peso de 4 kg (igual a mi L1), **cuando** calculo el costo con zona
  urbana y cliente normal, **entonces** se cobra el tramo 1: $6.000 (mi regla D,
  par, incluye el límite: peso ≤ 4).
- **Dado** un peso de 4,1 kg, **cuando** calculo el costo, **entonces** se cobra el
  tramo 2: $9.000 (ya superó L1 = 4).
- **Dado** un peso de 15 kg, **cuando** calculo el costo, **entonces** se cobra
  $9.000 + $800 × (15 − 10) = $13.000 (proporcional sobre L2 = 10).
- **Dado** un peso de 45,5 kg (mayor que mi PMAX = 45), **cuando** calculo el
  costo, **entonces** se lanza el error "peso inválido".
- **Dado** un peso de 0 kg o negativo, **cuando** calculo el costo, **entonces**
  se lanza el error "peso inválido".

**HU2 · Recargo por zona de destino (cubre R2, R4, R8)**
Como cliente de EnvíaYa, quiero que el costo incluya el recargo según la zona
de destino, para que el precio refleje el costo real de llevar el paquete allí.

Criterios de aceptación:
- **Dado** un envío a zona rural (mi RR = 25 %), **cuando** calculo el costo de
  un paquete de 10 kg, **entonces** el costo es 9.000 × 1,25 = $11.250, que
  redondeado al múltiplo de $100 más cercano (50 hacia arriba, R8) es **$11.300**.
- **Dado** un envío a zona nacional (mi RN = 40 %), **cuando** calculo el costo
  de un paquete de 10 kg, **entonces** el costo es 9.000 × 1,40 = **$12.600**.
- **Dado** un envío a zona urbana, **cuando** calculo el costo, **entonces** no
  se aplica ningún recargo por zona.
- **Dado** una zona que no es urbana, rural ni nacional, **cuando** calculo el
  costo, **entonces** se lanza un error (R2).
- **Dado** un día fuera del rango 1 a 7, **cuando** calculo el costo, **entonces**
  se lanza un error (R2).

**HU3 · Cliente, cupón y fin de semana (cubre R5, R6, R7, R8)**
Como cliente de EnvíaYa, quiero que se apliquen correctamente mi descuento de
cliente, mi cupón y el recargo de fin de semana, para pagar lo justo en cada
promoción.

Criterios de aceptación (reglas B, E y F mías):
- **Dado** un cliente vip (V = 10 %) con cupón ENVIO10 (10 %), **cuando** calculo
  el costo de un paquete de 4 kg en zona urbana un miércoles, **entonces** solo
  se aplica **el mayor** descuento (mi regla B, par) → 6.000 × 0,90 = **$5.400**.
- **Dado** un envío el sábado (día 6) con cliente vip, **cuando** calculo el
  costo, **entonces** el recargo de fin de semana (+$2.000, R5) se suma **después**
  de los descuentos (mi regla E, impar) → 6.000 × 0,90 + 2.000 = **$7.400**.
- **Dado** un cupón que no existe (por ejemplo "BIENVENIDA"), **cuando** calculo
  el costo, **entonces** el cupón se ignora y el costo no cambia (mi regla F,
  par, R7).
- **Dado** un cálculo cuyo valor antes del redondeo fuera menor a $5.000,
  **cuando** obtengo el resultado, **entonces** el costo final nunca es menor
  que $5.000 y se entrega redondeado al múltiplo de $100 (R8).

### Matriz de trazabilidad

| Requisito | Historia | Casos de prueba (se completan en la Parte 3) |
|---|---|---|
| R1 (peso válido, PMAX=45) | HU1 | CN-… |
| R2 (zona y día válidos) | HU2 | CN-… |
| R3 (tarifa base, L1=4, L2=10) | HU1 | CN-… |
| R4 (recargo zona RR=25 %, RN=40 %) | HU2 | CN-… |
| R5 (finde +$2.000 después de descuentos) | HU3 | CN-… |
| R6 (descuentos, solo el mayor) | HU3 | CN-… |
| R7 (cupón inexistente se ignora) | HU3 | CN-… |
| R8 (mínimo $5.000 y redondeo a $100) | HU1, HU2, HU3 | CN-… |

Cada requisito está cubierto por al menos una historia, y cada historia se
verificará con casos de prueba de la matriz de la Parte 3.

---

## Parte 2 · Plan de pruebas (0,5 pts)

*(Escribe aquí: alcance, 4 niveles aplicados al caso, estrategia/ambiente/roles, riesgos con mitigación, criterios de entrada y salida)*

---

## Parte 3 · Caja negra (0,9 pts)

*(Particiones de equivalencia, valores límite en 0/L1/L2/PMAX, tabla de decisión cliente×cupón×finde, matriz ≥20 casos, cálculo paso a paso de 5 casos)*

---

## Parte 4 · Caja blanca (0,6 pts)

*(Grafo de flujo de calc, complejidad ciclomática por 3 métodos, caminos independientes, cobertura)*

---

## Parte 5 · Automatización, ejecución y defectos (0,8 pts)

*(Capturas pytest, cobertura pytest-cov, reportes de defectos, métricas)*

### Defectos encontrados contra el código heredado

*(llenar después de ejecutar las pruebas; pistas a verificar: límite 50 vs PMAX 45, redondeo por truncamiento, sábado sin recargo, finde antes de descuentos, descuentos encadenados vs "solo el mayor", zona/día inválidos sin error)*

---

## Parte 6 · Mantenimiento y refactorización (0,9 pts)

*(≥6 code smells con nombre técnico y línea, clasificación del mantenimiento, refactor con Estrategia y UML, regresión en verde, antes/después)*

---

## Parte 7 · Gestión de configuración (0,5 pts)

*(etiquetas, ramas fix/DEF-xx, refactor/estrategia, test/suite, versionado semántico justificado, CHANGELOG, git log --oneline --graph --all)*

---

## Parte 8 · Solicitud de cambio (0,4 pts)

**Mi solicitud: CAMBIO = 0 → Nueva zona insular (San Andrés), recargo 70 %, sin cupón.**

*(Análisis de impacto con la matriz de trazabilidad, tipo de mantenimiento, rama propia con pruebas primero, nueva versión y CHANGELOG)*
