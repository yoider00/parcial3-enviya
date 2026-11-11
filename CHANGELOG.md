# Changelog

Todos los cambios notables de este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),
y este proyecto adhiere a [Versionado Semántico](https://semver.org/lang/es/).

## [2.1.0] - 2026-11-11

### Added

- **CHG-001:** nueva zona **insular (San Andrés)** con recargo del **70 %**
  (`ZonaInsular`, `RECARGO_INSULAR = 0.70`).
- Los envíos insulares **no aceptan cupón**: el cupón se ignora en esa zona
  (atributo `acepta_cupon = False` en la estrategia).
- Casos de prueba CN-27, CN-28 y CN-29, escritos **antes** de la implementación (TDD).

Implementado en la rama `cambio/zona-insular` e integrado a master con merge.
Versión **minor**: funcionalidad nueva sin cambio de interfaz.

## [2.0.0] - 2026-11-11

### Changed

- **CAMBIO ROMPENTE (breaking):** se eliminó el parámetro `flag` de `calc(...)`.
  La función ya no imprime por consola; la responsabilidad de presentación sale
  del contrato de cálculo. Al cambiar la interfaz pública corresponde el salto
  de versión **major** según versionado semántico.

### Refactor

- Extracción de funciones: `_validar_entradas`, `_tarifa_base`,
  `_descuento_maximo`, `_aplicar_finde`, `_con_minimo_y_redondeo`.
- Números mágicos reemplazados por constantes de negocio con nombre.
- **Patrón Estrategia** para el recargo por zona (`RecargoZona` → Urbana/Rural/Nacional).
- Eliminación de código muerto (`t = t`) y de anidamientos innecesarios.
- Complejidad ciclomática: 14 en una función → máximo 4 por función.
- Suite adaptada al nuevo contrato (CW-01 ahora verifica que `flag` ya no existe).

## [1.0.1] - 2026-11-11

### Fixed

- **DEF-01:** el peso máximo aceptado era 50 kg; ahora respeta PMAX = 45 (R1).
- **DEF-02:** las zonas inválidas se procesaban en silencio; ahora se valida (R2).
- **DEF-03:** los días fuera de 1–7 no se validaban; ahora se valida (R2).
- **DEF-04:** el sábado no recibía el recargo de fin de semana (R5).
- **DEF-05:** el recargo de fin de semana se sumaba antes de los descuentos (R5/E).
- **DEF-06:** los descuentos se encadenaban; ahora se aplica solo el mayor (R6/B).
- **DEF-07:** el redondeo truncaba; ahora redondea al múltiplo de $100 con $50 hacia arriba (R8).

Correcciones sin cambio de interfaz → versión **patch** según versionado semántico.
Ejecución de 11 ramas `fix/DEF-01 … fix/DEF-07`, `refactor/estrategia` y `test/suite`,
integradas a master con merges.

## [1.0.0] - 2026-11-11

### Added

- Función `calc` heredada del desarrollador anterior (código legado).
- `CONFIG` lleno con los parámetros del código estudiantil 0182320076
  (PMAX=45, L1=4, L2=10, RR=25 %, RN=40 %, V=10 %, S=$2.000).
- Suite inicial de pruebas (en progreso).
