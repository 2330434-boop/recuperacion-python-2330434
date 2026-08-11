import pytest
from recuperacion_python_2330434.services import GestorEmpleados


def test_registrar_empleado_exito():
    gestor = GestorEmpleados()
    emp = gestor.registrar_empleado("E01", "Juan Pérez", "Sistemas", 15000.0, 2)
    assert emp.id_empleado == "E01"
    assert emp.nombre == "Juan Pérez"
    assert len(gestor.obtener_todos()) == 1


def test_registrar_empleado_id_duplicado():
    gestor = GestorEmpleados()
    gestor.registrar_empleado("E01", "Juan Pérez", "Sistemas", 15000.0, 2)
    with pytest.raises(ValueError, match="Ya existe un empleado"):
        gestor.registrar_empleado("E01", "Maria Lopez", "Ventas", 18000.0, 1)


def test_registrar_empleado_salario_invalido():
    gestor = GestorEmpleados()
    with pytest.raises(ValueError, match="salario debe ser un valor positivo"):
        gestor.registrar_empleado("E01", "Juan Pérez", "Sistemas", -500.0, 2)


def test_actualizar_empleado():
    gestor = GestorEmpleados()
    gestor.registrar_empleado("E01", "Juan Pérez", "Sistemas", 15000.0, 2)
    exito = gestor.actualizar_empleado("E01", salario=20000.0, antiguedad=3)
    assert exito is True
    emp = gestor.buscar_por_id("E01")
    assert emp.salario == 20000.0
    assert emp.antiguedad == 3


def test_eliminar_empleado():
    gestor = GestorEmpleados()
    gestor.registrar_empleado("E01", "Juan Pérez", "Sistemas", 15000.0, 2)
    assert gestor.eliminar_empleado("E01") is True
    assert len(gestor.obtener_todos()) == 0


def test_obtener_resumen_y_nomina():
    gestor = GestorEmpleados()
    gestor.registrar_empleado("E01", "Ana Gómez", "Sistemas", 20000.0, 5)
    gestor.registrar_empleado("E02", "Carlos López", "Ventas", 30000.0, 2)

    resumen = gestor.obtener_resumen()
    assert resumen["total_empleados"] == 2
    assert resumen["nomina_total"] == 50000.0
    assert resumen["promedio_salario"] == 25000.0
    assert resumen["mayor_antiguedad"].id_empleado == "E01"
