# Parcial 3 · Ingeniería de Software I · EnvíaYa

Mantenimiento y pruebas de la función `calc` de EnvíaYa (Riohacha).

- Estudiante: (tu nombre) · Código: 0182320076
- Parámetros: PMAX=45, L1=4, L2=10, RR=25 %, RN=40 %, V=10 %, S=$2.000, CAMBIO=0

## Cómo ejecutar las pruebas

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
```

## Cobertura

```bash
python -m pytest tests/ --cov=envios --cov-branch --cov-report=term-missing
```

## Estructura

```
envios.py          # código heredado v1.0.0 (no modificar hasta Parte 6)
tests/test_envios.py
docs/Informe_Parcial3.md
CHANGELOG.md
```
