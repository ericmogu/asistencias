import configparser
from data_loading import cargar_y_filtrar_excel
from data_processing import contar_asistencias_por_dia_y_grado
from email_utils import enviar_email_con_graficos
from data_visualization import crear_grafico_circular, crear_grafico_barras

def main():
    # Cargar configuración
    config = configparser.ConfigParser()
    config.read('config.ini')

    SMTP_SERVER = config['EMAIL']['SMTP_SERVER']
    SMTP_PORT = config['EMAIL']['SMTP_PORT']
    EMAIL_SENDER = config['EMAIL']['EMAIL_SENDER']
    EMAIL_PASSWORD = config['EMAIL']['EMAIL_PASSWORD']
    EMAIL_RECEIVER = config['EMAIL']['EMAIL_RECEIVER']

    # Cargar y filtrar datos
    carpeta = 'files'
    df_resultado = cargar_y_filtrar_excel(carpeta)
    print(f'Todos los archivos Excel en "{carpeta}" han sido combinados, filtrados y ordenados.')

    if df_resultado.empty:
        print("No hay datos para procesar.")
        return
    
    df_resultado['GRADO'] = df_resultado['GRADO'].astype(str).str.replace(' ', '')
    df_resultado_final = contar_asistencias_por_dia_y_grado(df_resultado)
    print("Conteo de ausencias y asistencias por día y grado:")
    print(df_resultado_final.head(30))

    ultima_columna_ausencias = df_resultado_final.filter(like='Ausencias_').columns[-1]
    ultima_columna_asistencias = df_resultado_final.filter(like='Asistencias_').columns[-1]

    total_ausencias_ultimo_dia = df_resultado_final[ultima_columna_ausencias].sum()
    total_asistencias_ultimo_dia = df_resultado_final[ultima_columna_asistencias].sum()

    print(f'Total de Ausencias del Último Día: {total_ausencias_ultimo_dia}')
    print(f'Total de Asistencias del Último Día: {total_asistencias_ultimo_dia}')

    # Gráfico circular
    cantidades = [total_asistencias_ultimo_dia, total_ausencias_ultimo_dia]
    categorias = ['Asistencias', 'Ausencias']
    fig_circular = crear_grafico_circular(cantidades, categorias)

    # Totalizar asistencias y ausencias por grado
    total_ausencias = df_resultado_final.filter(like='Ausencias_').sum(axis=1)
    total_asistencias = df_resultado_final.filter(like='Asistencias_').sum(axis=1)
    df_resultado_final['Total_Ausencias'] = total_ausencias
    df_resultado_final['Total_Asistencias'] = total_asistencias
    df_ausencias = df_resultado_final[['GRADO', 'Total_Ausencias', 'Total_Asistencias']]
    print("Total de ausencias y asistencias por grado:")
    print(df_ausencias.head(30))

    # Gráfico barras
    fig_barras = crear_grafico_barras(df_resultado_final)

    # Enviar email con gráficos
    asunto_email = 'Informe Gráficos de Asistencias y Ausencias'
    cuerpo_email = 'A continuación se incluyen los gráficos de asistencias y ausencias generados automáticamente.'
    figuras = [
        (fig_circular, 'grafico_circular'),
        (fig_barras, 'grafico_barras')
    ]
    enviar_email_con_graficos(asunto_email, cuerpo_email, figuras, 
                               SMTP_SERVER, SMTP_PORT, EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER)

if __name__ == '__main__':
    main()
