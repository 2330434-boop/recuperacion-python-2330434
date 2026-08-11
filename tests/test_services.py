import pytest
from recuperacion_python_2330434.models import Empleado
from recuperacion_python_2330434.services import GestorEmpleados

# --- 1, 2, 3: PRUEBAS FUNCIONAMIENTO NORMAL ---
def test_agregar_empleado_exitoso():
    gestor = GestorEmpleados()
    emp = Empleado("E001", "Carlos", "Sistemas", 15000.0, 3)
    assert gestor.agregar_empleado(emp) is True
    assert len(gestor.empleados) == 1

def test_buscar_por_id_exitoso():
    gestor = GestorEmpleados()
    emp = Empleado("E001", "Carlos", "Sistemas", 15000.0, 3)
    gestor.agregar_empleado(emp)
    encontrado = gestor.buscar_por_id("E001")
    assert encontrado is not None
    assert encontrado.nombre == "Carlos"

def test_calcular_nomina_total():
    gestor = GestorEmpleados()
    gestor.agregar_empleado(Empleado("E001", "Carlos", "Sistemas", 1000.0, 2))
    gestor.agregar_empleado(Empleado("E002", "Ana", "Ventas", 2000.0, 4))
    assert gestor.calcular_nomina_total() == 3000.0

# --- 4, 5: PRUEBAS CASOS LÍMITE ---
def test_empleado_antiguedad_cero():
    gestor = GestorEmpleados()
    emp = Empleado("E003", "Nuevo", "RH", 8000.0, 0)
    assert gestor.agregar_empleado(emp) is True
    assert gestor.buscar_por_id("E003").antiguedad == 0

def test_obtener_mayor_antiguedad_lista_unica():
    gestor = GestorEmpleados()
    gestor.agregar_empleado(Empleado("E001", "Unico", "Sistemas", 5000.0, 1))
    mayor = gestor.obtener_mayor_antiguedad()
    assert mayor is not None
    assert mayor.id_empleado == "E001"

# --- 6, 7: PRUEBAS DATOS INCORRECTOS / INVÁLIDOS ---
def test_agregar_empleado_duplicado():
    gestor = GestorEmpleados()
    emp1 = Empleado("E001", "Carlos", "Sistemas", 15000.0, 3)
    emp2 = Empleado("E001", "Ana", "Ventas", 18000.0, 5)
    gestor.agregar_empleado(emp1)
    assert gestor.agregar_empleado(emp2) is False

def test_actualizar_empleado_inexistente():
    gestor = GestorEmpleados()
    emp_nuevo = Empleado("E999", "Fantasmas", "Nadie", 0.0, 0)
    assert gestor.actualizar_empleado("E999", emp_nuevo) is False

# --- 8: PRUEBA BÚSQUEDA SIN RESULTADOS ---
def test_buscar_por_id_no_existente():
    gestor = GestorEmpleados()
    gestor.agregar_empleado(Empleado("E001", "Carlos", "Sistemas", 10000.0, 2))
    resultado = gestor.buscar_por_id("E999")
    assert resultado is None
