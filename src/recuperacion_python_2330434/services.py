from typing import Optional
from .models import Empleado


class GestorEmpleados:
    def __init__(self) -> None:
        self.empleados: list[Empleado] = []

    def buscar_por_id(self, id_empleado: str) -> Optional[Empleado]:
        id_clean = id_empleado.strip().upper()
        for emp in self.empleados:
            if emp.id_empleado.upper() == id_clean:
                return emp
        return None

    def registrar_empleado(
        self,
        id_empleado: str,
        nombre: str,
        departamento: str,
        salario: float,
        antiguedad: int,
    ) -> Empleado:
        id_clean = id_empleado.strip()
        nombre_clean = nombre.strip()
        dept_clean = departamento.strip()

        if not id_clean or not nombre_clean or not dept_clean:
            raise ValueError(
                "El ID, nombre y departamento no pueden estar vacíos."
            )

        if self.buscar_por_id(id_clean) is not None:
            raise ValueError(f"Ya existe un empleado con el ID '{id_clean}'.")

        if salario <= 0:
            raise ValueError("El salario debe ser un valor positivo mayor a 0.")

        if antiguedad < 0:
            raise ValueError("La antigüedad no puede ser negativa.")

        empleado = Empleado(
            id_empleado=id_clean,
            nombre=nombre_clean,
            departamento=dept_clean,
            salario=salario,
            antiguedad=antiguedad,
        )
        self.empleados.append(empleado)
        return empleado

    def obtener_todos(self) -> list[Empleado]:
        return self.empleados.copy()

    def actualizar_empleado(
        self,
        id_empleado: str,
        nombre: Optional[str] = None,
        departamento: Optional[str] = None,
        salario: Optional[float] = None,
        antiguedad: Optional[int] = None,
    ) -> bool:
        emp = self.buscar_por_id(id_empleado)
        if emp is None:
            return False

        if nombre is not None and nombre.strip():
            emp.nombre = nombre.strip()
        if departamento is not None and departamento.strip():
            emp.departamento = departamento.strip()
        if salario is not None:
            if salario <= 0:
                raise ValueError(
                    "El salario debe ser un valor positivo mayor a 0."
                )
            emp.salario = salario
        if antiguedad is not None:
            if antiguedad < 0:
                raise ValueError("La antigüedad no puede ser negativa.")
            emp.antiguedad = antiguedad

        return True

    def eliminar_empleado(self, id_empleado: str) -> bool:
        emp = self.buscar_por_id(id_empleado)
        if emp:
            self.empleados.remove(emp)
            return True
        return False

    def calcular_nomina_total(self) -> float:
        return sum(emp.salario for emp in self.empleados)

    def filtrar_por_departamento(self, departamento: str) -> list[Empleado]:
        dept_clean = departamento.strip().lower()
        return [
            emp
            for emp in self.empleados
            if emp.departamento.lower() == dept_clean
        ]

    def obtener_mayor_antiguedad(self) -> Optional[Empleado]:
        if not self.empleados:
            return None
        return max(self.empleados, key=lambda emp: emp.antiguedad)

    def obtener_resumen(self) -> dict:
        total = len(self.empleados)
        if total == 0:
            return {
                "total_empleados": 0,
                "nomina_total": 0.0,
                "promedio_salario": 0.0,
                "mayor_antiguedad": None,
            }

        nomina = self.calcular_nomina_total()
        mayor_ant = self.obtener_mayor_antiguedad()

        return {
            "total_empleados": total,
            "nomina_total": nomina,
            "promedio_salario": nomina / total,
            "mayor_antiguedad": mayor_ant,
        }
