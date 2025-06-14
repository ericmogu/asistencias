import os
import pandas as pd  # Asegúrate de que esta línea esté presente

def contiene_grado_y_estudiante(text):
    if not isinstance(text, str):
        return False
    texto_lower = text.lower()
    return 'grado' in texto_lower and 'estudiante' in texto_lower

def fila_a_eliminar(row):
    textos = row.astype(str)
    contiene_grado = textos.str.contains('grado', case=False, na=False).any()
    contiene_estudiante = textos.str.contains('estudiante', case=False, na=False).any()
    return contiene_grado and contiene_estudiante

def cargar_y_filtrar_excel(carpeta):
    dataframes = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.xlsx'):
            ruta_archivo = os.path.join(carpeta, archivo)
            df = pd.read_excel(ruta_archivo)
            print(f"Nombres de columnas en archivo {archivo}: {df.columns.tolist()}")
            df_filtrado = df[~df.apply(fila_a_eliminar, axis=1)]
            df_filtrado = df_filtrado.dropna(how='all')
            df_filtrado = df_filtrado.dropna(axis=1, how='all')
            dataframes.append(df_filtrado)
    if dataframes:
        df_combinado = pd.concat(dataframes, ignore_index=True)
    else:
        df_combinado = pd.DataFrame()
    return df_combinado
