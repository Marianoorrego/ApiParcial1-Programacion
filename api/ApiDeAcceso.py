from sodapy import Socrata
import pandas as pd

def consultar_casos(nombre_departamento, limite_registros):
    """
    Esta función trae los casos de COVID-19 de Colombia, pero solo los del departamento y numero de registros que se le indiquen.

    Parámetros:
        nombre_departamento (str): El nombre del departamento que se quiere buscar
        limite_registros (int): Cuantos casos como máximo se quieren traer (Entero positivo)

    Devuelve un DataFrame de pandas con las columnas más importantes (ciudad, departamento, edad, tipo, estado y país de procedencia). Si no hay datos, igual devuelve la tabla vacía con esas columnas """
  
    client = Socrata("www.datos.gov.co", None)

    depto = nombre_departamento.strip().upper()

    # Consulta solo las columnas requeridas
    resultados = client.get(
        "gt2j-8ykr",
        select="ciudad_municipio_nom,departamento_nom,edad,fuente_tipo_contagio,estado,pais_viajo_1_nom",
        where=f"departamento_nom='{depto}'",
        limit=limite_registros
    )

    # Convertir resultados a DataFrame
    return pd.DataFrame.from_records(resultados)
  