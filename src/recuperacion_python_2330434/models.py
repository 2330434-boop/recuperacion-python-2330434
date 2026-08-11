from dataclasses import dataclass


@dataclass
class Empleado:
    id_empleado: str
    nombre: str
    departamento: str
    salario: float
    antiguedad: int
  
