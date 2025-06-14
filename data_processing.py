import pandas as pd  # Asegúrate de que esta línea esté presente

def contar_ausencias_por_dia_y_grado(df):
    columnas_dias = [col for col in df.columns if str(col).strip().isdigit()]
    if 'GRADO' not in df.columns:
        raise KeyError('La columna "GRADO" no se encuentra en el DataFrame.')
    df_ausencias = df.groupby('GRADO')[columnas_dias].apply(lambda x: x.notna().sum())
    df_ausencias = df_ausencias.reset_index()
    return df_ausencias

def contar_asistencias_por_dia_y_grado(df):
    columnas_dias = [col for col in df.columns if str(col).strip().isdigit()]
    if 'GRADO' not in df.columns:
        raise KeyError('La columna "GRADO" no se encuentra en el DataFrame.')
    df_ausencias = df.groupby('GRADO')[columnas_dias].apply(lambda x: x.notna().sum())
    df_asistencias = df.groupby('GRADO')[columnas_dias].apply(lambda x: x.isna().sum())
    df_resultado = pd.concat([
        df_ausencias.rename(columns=lambda x: f'Ausencias_{x}'),
        df_asistencias.rename(columns=lambda x: f'Asistencias_{x}')
    ], axis=1)
    df_resultado = df_resultado.reset_index()
    return df_resultado
