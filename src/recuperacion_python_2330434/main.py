from recuperacion_python_2330434.services import GestorEmpleados


def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE EMPLEADOS ---")
    print("1. Registrar empleado")
    print("2. Listar todos los empleados")
    print("3. Buscar empleado por ID")
    print("4. Filtrar empleados por departamento")
    print("5. Actualizar empleado")
    print("6. Eliminar empleado")
    print("7. Ver estadísticas / resumen (Nómina y Antigüedad)")
    print("8. Salir")


def ejecutar():
    gestor = GestorEmpleados()

    # Datos de prueba iniciales
    gestor.registrar_empleado("E001", "Ana Gómez", "Sistemas", 25000.0, 3)
    gestor.registrar_empleado("E002", "Carlos López", "Ventas", 18000.0, 5)
    gestor.registrar_empleado("E003", "María Ruiz", "Sistemas", 30000.0, 2)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-8): ").strip()

        if opcion == "1":
            try:
                id_emp = input("ID: ")
                nombre = input("Nombre: ")
                dept = input("Departamento: ")
                salario = float(input("Salario: "))
                antiguedad = int(input("Antigüedad (años): "))
                gestor.registrar_empleado(id_emp, nombre, dept, salario, antiguedad)
                print("✅ Empleado registrado con éxito.")
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif opcion == "2":
            empleados = gestor.obtener_todos()
            if not empleados:
                print("ℹ️ No hay empleados registrados.")
            else:
                for emp in empleados:
                    print(
                        f"[{emp.id_empleado}] {emp.nombre} | Dept: {emp.departamento} | Salario: ${emp.salario} | Antigüedad: {emp.antiguedad} años"
                    )

        elif opcion == "3":
            id_emp = input("ID a buscar: ")
            emp = gestor.buscar_por_id(id_emp)
            if emp:
                print(
                    f"Encontrado: {emp.nombre} - Dept: {emp.departamento} - Salario: ${emp.salario}"
                )
            else:
                print("❌ Empleado no encontrado.")

        elif opcion == "4":
            dept = input("Ingresa el departamento a filtrar (ej. Sistemas, Ventas): ")
            filtrados = gestor.filtrar_por_departamento(dept)
            if not filtrados:
                print(f"ℹ️ No se encontraron empleados en el departamento '{dept}'.")
            else:
                print(f"\n--- EMPLEADOS EN {dept.upper()} ---")
                for emp in filtrados:
                    print(
                        f"[{emp.id_empleado}] {emp.nombre} | Salario: ${emp.salario} | Antigüedad: {emp.antiguedad} años"
                    )

        elif opcion == "5":
            id_emp = input("ID del empleado a actualizar: ")
            print("Deja en blanco lo que no quieras cambiar:")
            nombre = input("Nuevo nombre: ")
            dept = input("Nuevo departamento: ")
            sal_str = input("Nuevo salario: ")
            ant_str = input("Nueva antigüedad: ")

            try:
                sal = float(sal_str) if sal_str.strip() else None
                ant = int(ant_str) if ant_str.strip() else None
                exito = gestor.actualizar_empleado(
                    id_emp, nombre or None, dept or None, sal, ant
                )
                if exito:
                    print("✅ Empleado actualizado.")
                else:
                    print("❌ No se encontró el empleado.")
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif opcion == "6":
            id_emp = input("ID a eliminar: ")
            if gestor.eliminar_empleado(id_emp):
                print("✅ Empleado eliminado.")
            else:
                print("❌ No se encontró el empleado.")

        elif opcion == "7":
            resumen = gestor.obtener_resumen()
            print("\n--- RESUMEN Y ESTADÍSTICAS ---")
            print(f"Total empleados: {resumen['total_empleados']}")
            print(f"Nómina total: ${resumen['nomina_total']}")
            print(f"Promedio salario: ${resumen['promedio_salario']:.2f}")

            emp_mayor = resumen["mayor_antiguedad"]
            if emp_mayor:
                print(
                    f"⭐ Empleado con MAYOR ANTIGÜEDAD: {emp_mayor.nombre} ({emp_mayor.antiguedad} años)"
                )
            else:
                print("Mayor antigüedad: N/A")

        elif opcion == "8":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    ejecutar()
