from api.ApiDeAcceso import consultar_casos
from tabulate import tabulate

def seguro(valor):
    """Convierte NaN/None a 'VACÍO' para que la impresión no falle y se note que falta el dato."""
    return "ESTE CAMPO ESTA VACIO EN LA BASE DE DATOS" if valor is None or (isinstance(valor, float) and valor != valor) or str(valor).strip() == "" else str(valor)

def _imprimir_tabla(df):
   
    headers = [
        "Ciudad de ubicación",
        "Departamento",
        "Edad",
        "Tipo de contagio",
        "Estado",
        "País de procedencia"
    ]
    if df.empty:
        print("No hay datos para esa consulta.")
        return

    tabla = []
    for _, fila in df.iterrows():
        tabla.append([
            seguro(fila.get("ciudad_municipio_nom")),
            seguro(fila.get("departamento_nom")),
            seguro(fila.get("edad")),
            seguro(fila.get("fuente_tipo_contagio")),
            seguro(fila.get("estado")),
            seguro(fila.get("pais_viajo_1_nom")),
        ])
    print(tabulate(tabla, headers=headers, tablefmt="fancy_grid", showindex=False))

def ejecutar_ui():
    print("=== Consulta de Casos COVID-19 en Colombia ===")
    

    departamento = input("Ingrese el nombre del departamento: ").strip()
    limite_str = input("Ingrese el número de registros a consultar: ").strip()

    # Validación de número: solo acepta positivos, pide de nuevo si es inválido
    while True:
        try:
            limite = int(limite_str)
            if limite <= 0:
                print("El límite debe ser un número positivo. Intente de nuevo.")
                limite_str = input("Ingrese el número de registros a consultar: ").strip()
            else:
                break
        except ValueError:
            print("Valor no numérico. Intente de nuevo.")
            limite_str = input("Ingrese el número de registros a consultar: ").strip()

    try:
        df = consultar_casos(departamento, limite)
        print(f"\n=== Resultados obtenidos: {len(df)} fila(s) ===\n")
        _imprimir_tabla(df)
    except Exception as e:
        print("Error en la consulta:", e)
