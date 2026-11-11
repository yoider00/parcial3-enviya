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

- **HU1 (pesos y tramos - R1, R3):** Como cliente de EnvíaYa, quiero que el costo dependa del peso de mi paquete, para pagar solo lo que corresponde.
  - Dado un peso de 4 kg, cuando calculo el costo, entonces el tramo es $6.000 (L1 incluido).
  - Dado un peso de 45,5 kg, cuando calculo el costo, entonces se lanza "peso inválido".
- **HU2 (zonas y recargos - R4):** Como cliente, ...
- **HU3 (cliente, cupón y fin de semana - R5, R6, R7, R8):** Como cliente, ...
- *(Completa HU2 y HU3 con tus criterios Dado/Cuando/Entonces)*

### Matriz de trazabilidad

| Requisito | Historia | Casos de prueba |
|---|---|---|
| R1 | HU1 | (completar con IDs de la Parte 3) |
| R3 | HU1 | |
| R4 | HU2 | |
| R5 | HU3 | |
| R6 | HU3 | |
| R7 | HU3 | |
| R8 | HU1, HU3 | |

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
