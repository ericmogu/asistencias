import matplotlib.pyplot as plt  # Asegúrate de que esta línea esté presente

def etiqueta_con_cantidad(pct, allvals):
    absolute = int(round(pct / 100. * sum(allvals)))
    return f"{absolute} ({pct:.1f}%)"

def crear_grafico_circular(cantidades, categorias):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(cantidades, labels=categorias, autopct=lambda pct: etiqueta_con_cantidad(pct, cantidades),
           startangle=90, colors=['#4CAF50', '#F44336'])
    ax.set_title('Proporción y Cantidad de Asistencias y Ausencias del Último Día', fontsize=14, fontweight='bold')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    return fig

def crear_grafico_barras(df_resultado_final):
    total_ausencias_por_grado = df_resultado_final.groupby('GRADO')['Total_Ausencias'].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    total_ausencias_por_grado.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_xlabel('Grado', fontsize=12)
    ax.set_ylabel('Total de Ausencias', fontsize=12)
    ax.set_title('Total de Ausencias por Grado en el Mes', fontsize=14, fontweight='bold')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y')
    plt.tight_layout()
    return fig
