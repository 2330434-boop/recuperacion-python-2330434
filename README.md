# Recuperación Python - Proyecto de Empleados

## Datos del estudiante
- **Nombre completo:** Angel Morales Sánchez
- **Matrícula:** 2330434
- **Grupo:** IM 8-1
- **Número de variante:** 17

## Descripción
Sistema en consola desarrollado en Python para la administración de empleados, registro de salarios, cálculo de nómina y consulta de estadísticas.

## Funcionalidades
- Registrar empleados validando identificadores únicos.
- Consultar lista general de empleados.
- Búsqueda por ID.
- Actualizar y eliminar registros.
- Cálculo de nómina total y estadísticas de antigüedad.

## Estructura del proyecto
- `src/recuperacion_python_2330434/`:
  - `models.py`: Definición de la entidad `Empleado`.
  - `services.py`: Lógica de negocios y validaciones.
  - `main.py`: Menú interactivo en consola.
- `tests/`:
  - `test_services.py`: Pruebas unitarias automatizadas.

## Requisitos
- Python >= 3.12
- Gestor de paquetes `uv`

## Sincronización e Instalación
```bash
uv sync

Ejecución del Programa
Bash
uv run python -m recuperacion_python_2330434.main

Pruebas Automatizadas
Bash
uv run pytest

Revisión y Formato con Ruff
Bash
uv run ruff check .
uv run ruff format --check .

Decisiones de Diseño
Se implementó una arquitectura modular dividiendo la representación de datos (models.py), la lógica operativa (services.py) y la interfaz en consola (main.py) para mantener una clara separación de responsabilidades.

Problemas Encontrados
Problema: Mover el archivo pyproject.toml y la carpeta de pruebas a la raíz para que uv y pytest reconozcan la estructura correctamente.

Solución: Se reorganizaron los módulos asegurando que los paquetes queden alojados en src/ y tests/.
