import pytest
from recuperacion_python_2330434.models import Empleado
from recuperacion_python_2330434.services import GestorEmpleados


def test_agregar_empleado():
    gestor = GestorEmpleados()
    emp = Empleado("E001", "Carlos", "Sistemas", 15000.0, 3)
    assert gestor.agregar_empleado(emp) is True
    assert len(gestor.empleados) == 1


def test_agregar_empleado_duplicado():
    gestor = GestorEmpleados()
    emp1 = Empleado("E001", "Carlos", "Sistemas", 15000.0, 3)
    emp2 = Empleado("E001", "Ana", "Ventas", 18000.0, 5)
    gestor.agregar_empleado(emp1)
    assert gestor.agregar_empleado(emp2) is False


def test_buscar_por_id():
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


def test_obtener_mayor_antiguedad():
    gestor = GestorEmpleados()
    gestor.agregar_empleado(Empleado("E001", "Carlos", "Sistemas", 1000.0, 2))
    gestor.agregar_empleado(Empleado("E002", "Ana", "Ventas", 2000.0, 5))
    mayor = gestor.obtener_mayor_antiguedad()
    assert mayor is not None
    assert mayor.id_empleado == "E002"
