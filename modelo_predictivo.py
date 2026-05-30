"""
=============================================================
  PROYECTO: Analítica de Negocios - Saga Falabella Perú
  MÓDULO:   Modelo Predictivo Simple
  ALUMNO:   Cesar Andrés (Sección: Modelo Predictivo)
  CURSO:    Analítica de Negocios - Ingeniería de Sistemas
=============================================================

VARIABLE OBJETIVO: Ticket promedio de compra (en soles)
TIPO DE MODELO:    Regresión Lineal Múltiple
HERRAMIENTA:       Python + scikit-learn

VARIABLES PREDICTORAS:
  - Categoría de producto   (Belleza, Deportes, Electrónica, Hogar y Deco, Ropa y Moda)
  - Segmento de cliente     (Básico, Silver, Gold, Platinum)
  - Canal de venta          (Online, Tienda física)
  - Región                  (Lima, Arequipa, Trujillo, Piura, Cusco)
  - Compras previas         (número de transacciones históricas)
  - Meses como cliente      (antigüedad en el programa Falabella)
  - Descuento aplicado (%)  (porcentaje de descuento en la compra)
  - Productos distintos     (variedad de ítems en la compra)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import tkinter as tk
from tkinter import ttk, messagebox

# ──────────────────────────────────────────────
#  1. GENERACIÓN DEL DATASET SIMULADO
# ──────────────────────────────────────────────
def generar_dataset(n=1200, seed=42):
    np.random.seed(seed)

    CATEGORIAS = ['Ropa y Moda', 'Electrónica', 'Hogar y Deco', 'Deportes', 'Belleza']
    CANALES    = ['Online', 'Tienda física']
    REGIONES   = ['Lima', 'Arequipa', 'Trujillo', 'Piura', 'Cusco']
    SEGMENTOS  = ['Básico', 'Silver', 'Gold', 'Platinum']

    cat_arr    = np.random.choice(CATEGORIAS, n)
    canal_arr  = np.random.choice(CANALES, n)
    region_arr = np.random.choice(REGIONES, n)
    seg_arr    = np.random.choice(SEGMENTOS, n)

    compras_previas    = np.random.randint(1, 50, n)
    meses_cliente      = np.random.randint(1, 84, n)
    descuento_pct      = np.random.uniform(0, 40, n)
    productos_distintos = np.random.randint(1, 15, n)

    # Lógica de negocio para el ticket
    SEG_BASE  = {'Básico': 80,  'Silver': 180, 'Gold': 320,  'Platinum': 600}
    CAT_MULT  = {'Ropa y Moda': 1.0, 'Electrónica': 2.5, 'Hogar y Deco': 1.8,
                 'Deportes': 1.3, 'Belleza': 0.9}
    CANAL_MULT = {'Online': 0.95, 'Tienda física': 1.05}

    ticket = np.array([
        SEG_BASE[s] * CAT_MULT[c] * CANAL_MULT[ch]
        + compras_previas[i] * 5.2
        + meses_cliente[i] * 2.1
        + productos_distintos[i] * 15
        - descuento_pct[i] * 3.1
        + np.random.normal(0, 25)
        for i, (s, c, ch) in enumerate(zip(seg_arr, cat_arr, canal_arr))
    ])
    ticket = np.clip(ticket, 30, 3000).round(2)

    df = pd.DataFrame({
        'categoria':           cat_arr,
        'canal':               canal_arr,
        'region':              region_arr,
        'segmento_cliente':    seg_arr,
        'compras_previas':     compras_previas,
        'meses_cliente':       meses_cliente,
        'descuento_aplicado':  descuento_pct.round(1),
        'productos_distintos': productos_distintos,
        'ticket_promedio_soles': ticket
    })
    return df


# ──────────────────────────────────────────────
#  2. ENTRENAMIENTO DEL MODELO
# ──────────────────────────────────────────────
def entrenar_modelo(df):
    X = pd.get_dummies(
        df.drop('ticket_promedio_soles', axis=1),
        columns=['categoria', 'canal', 'region', 'segmento_cliente'],
        drop_first=False
    )
    y = df['ticket_promedio_soles']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    metricas = {
        'R2':   round(r2_score(y_test, y_pred), 4),
        'MAE':  round(mean_absolute_error(y_test, y_pred), 2),
        'RMSE': round(np.sqrt(mean_squared_error(y_test, y_pred)), 2),
        'n_train': len(X_train),
        'n_test':  len(X_test),
    }

    coeficientes = dict(zip(X.columns, modelo.coef_))
    coeficientes['intercepto'] = modelo.intercept_

    return modelo, metricas, coeficientes, X.columns.tolist(), y_test, y_pred


# ──────────────────────────────────────────────
#  3. REPORTE DE MÉTRICAS EN CONSOLA
# ──────────────────────────────────────────────
def imprimir_reporte(metricas, coeficientes):
    print("\n" + "="*55)
    print("  MODELO PREDICTIVO — SAGA FALABELLA PERÚ")
    print("  Regresión Lineal Múltiple | scikit-learn")
    print("="*55)
    print(f"\n  Registros de entrenamiento : {metricas['n_train']}")
    print(f"  Registros de prueba        : {metricas['n_test']}")
    print("\n  MÉTRICAS DE EVALUACIÓN")
    print(f"  {'R² (varianza explicada)':<30} {metricas['R2']:.4f}  →  {metricas['R2']*100:.1f}%")
    print(f"  {'MAE (error medio absoluto)':<30} S/ {metricas['MAE']}")
    print(f"  {'RMSE (raíz error cuadrático)':<30} S/ {metricas['RMSE']}")
    print("\n  INTERPRETACIÓN:")
    print(f"  El modelo explica el {metricas['R2']*100:.1f}% de la variabilidad")
    print(f"  del ticket de compra. En promedio, las predicciones")
    print(f"  se desvían S/ {metricas['MAE']:.2f} del valor real.")
    print("\n  TOP 5 VARIABLES MÁS INFLUYENTES:")

    coefs_sin_intercepto = {k: v for k, v in coeficientes.items() if k != 'intercepto'}
    top5 = sorted(coefs_sin_intercepto.items(), key=lambda x: abs(x[1]), reverse=True)[:5]
    for nombre, valor in top5:
        signo = "↑ sube" if valor > 0 else "↓ baja"
        print(f"  {nombre:<35} {signo} S/ {abs(valor):.2f}")
    print("="*55 + "\n")


# ──────────────────────────────────────────────
#  4. GRÁFICOS DE EVALUACIÓN
# ──────────────────────────────────────────────
def mostrar_graficos(metricas, coeficientes, y_test, y_pred):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle('Saga Falabella Perú — Evaluación del Modelo Predictivo',
                 fontsize=13, fontweight='bold', y=1.02)

    # --- Gráfico 1: Real vs Predicho ---
    ax1 = axes[0]
    ax1.scatter(y_test, y_pred, alpha=0.4, color='#1D9E75', s=20, label='Predicciones')
    lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
    ax1.plot(lims, lims, 'r--', linewidth=1.5, label='Predicción perfecta')
    ax1.set_xlabel('Ticket real (S/)', fontsize=11)
    ax1.set_ylabel('Ticket predicho (S/)', fontsize=11)
    ax1.set_title('Real vs Predicho', fontsize=12)
    ax1.legend(fontsize=9)
    ax1.text(0.05, 0.92, f'R² = {metricas["R2"]:.4f}',
             transform=ax1.transAxes, fontsize=10,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # --- Gráfico 2: Distribución de errores ---
    ax2 = axes[1]
    errores = y_pred - y_test.values
    ax2.hist(errores, bins=40, color='#378ADD', edgecolor='white', alpha=0.85)
    ax2.axvline(0, color='red', linestyle='--', linewidth=1.5)
    ax2.axvline(errores.mean(), color='orange', linestyle='--', linewidth=1.5,
                label=f'Media: {errores.mean():.1f}')
    ax2.set_xlabel('Error (predicho − real) en S/', fontsize=11)
    ax2.set_ylabel('Frecuencia', fontsize=11)
    ax2.set_title('Distribución de errores', fontsize=12)
    ax2.legend(fontsize=9)

    # --- Gráfico 3: Importancia de variables (top 10) ---
    ax3 = axes[2]
    coefs_sin_intercepto = {k: v for k, v in coeficientes.items() if k != 'intercepto'}
    top10 = sorted(coefs_sin_intercepto.items(), key=lambda x: abs(x[1]), reverse=True)[:10]
    nombres = [x[0].replace('segmento_cliente_', 'Seg: ')
                   .replace('categoria_', 'Cat: ')
                   .replace('canal_', 'Canal: ')
                   .replace('region_', 'Reg: ')
               for x, _ in top10]
    valores = [v for _, v in top10]
    colores = ['#1D9E75' if v > 0 else '#D85A30' for v in valores]

    bars = ax3.barh(range(len(nombres)), valores, color=colores, edgecolor='white')
    ax3.set_yticks(range(len(nombres)))
    ax3.set_yticklabels(nombres, fontsize=9)
    ax3.axvline(0, color='gray', linewidth=0.8)
    ax3.set_xlabel('Coeficiente (impacto en S/)', fontsize=11)
    ax3.set_title('Top 10 variables por impacto', fontsize=12)
    ax3.invert_yaxis()

    plt.tight_layout()
    plt.savefig('evaluacion_modelo_falabella.png', dpi=150, bbox_inches='tight')
    print("  Gráficos guardados en: evaluacion_modelo_falabella.png")
    plt.show()


# ──────────────────────────────────────────────
#  5. INTERFAZ GRÁFICA (TKINTER)
# ──────────────────────────────────────────────
COEFS_MODELO = {
    'intercepto': 425.24,
    'compras_previas': 5.087,
    'meses_cliente': 2.211,
    'descuento_aplicado': -2.987,
    'productos_distintos': 16.388,
    'categoria_Belleza': -171.819,
    'categoria_Deportes': -57.856,
    'categoria_Electrónica': 289.256,
    'categoria_Hogar y Deco': 85.010,
    'categoria_Ropa y Moda': -144.591,
    'canal_Online': -23.662,
    'canal_Tienda física': 23.662,
    'region_Arequipa': -6.635,
    'region_Cusco': 9.766,
    'region_Lima': -2.929,
    'region_Piura': 7.498,
    'region_Trujillo': -7.700,
    'segmento_cliente_Básico': -318.752,
    'segmento_cliente_Gold': 39.014,
    'segmento_cliente_Platinum': 456.675,
    'segmento_cliente_Silver': -176.937,
}

def predecir_ticket(cat, seg, canal, region, compras, meses, descuento, productos):
    ticket = COEFS_MODELO['intercepto']
    ticket += COEFS_MODELO['compras_previas'] * compras
    ticket += COEFS_MODELO['meses_cliente'] * meses
    ticket += COEFS_MODELO['descuento_aplicado'] * descuento
    ticket += COEFS_MODELO['productos_distintos'] * productos
    ticket += COEFS_MODELO.get(f'categoria_{cat}', 0)
    ticket += COEFS_MODELO.get(f'canal_{canal}', 0)
    ticket += COEFS_MODELO.get(f'region_{region}', 0)
    ticket += COEFS_MODELO.get(f'segmento_cliente_{seg}', 0)
    return max(30.0, min(3000.0, ticket))


def lanzar_interfaz():
    VERDE   = '#1D9E75'
    AZUL    = '#185FA5'
    BG      = '#F7F8FA'
    CARD    = '#FFFFFF'
    TEXTO   = '#1a1a2e'
    MUTED   = '#6B7280'

    root = tk.Tk()
    root.title("Predictor de Ticket — Saga Falabella Perú")
    root.geometry("1100x760")
    root.configure(bg=BG)
    root.resizable(True, True)

    # ── Header ──
    header = tk.Frame(root, bg=AZUL, pady=14)
    header.pack(fill='x')
    tk.Label(header, text="Saga Falabella Perú",
             font=('Helvetica', 16, 'bold'), fg='white', bg=AZUL).pack()
    tk.Label(header, text="Modelo Predictivo de Ticket Promedio de Compra",
             font=('Helvetica', 10), fg='#B5D4F4', bg=AZUL).pack()
    tk.Label(header, text="Regresión Lineal Múltiple  ·  R² = 88.3%  ·  MAE = S/ 93.46",
             font=('Helvetica', 9), fg='#9FE1CB', bg=AZUL).pack(pady=(2, 0))

    # ── Layout principal: columna izquierda (formulario) + derecha (resultado + gráfico) ──
    main = tk.Frame(root, bg=BG)
    main.pack(fill='both', expand=True, padx=0, pady=0)

    # ─── COLUMNA IZQUIERDA: formulario ───
    left = tk.Frame(main, bg=BG, width=420)
    left.pack(side='left', fill='y', padx=0, pady=0)
    left.pack_propagate(False)

    canvas = tk.Canvas(left, bg=BG, highlightthickness=0)
    scroll = ttk.Scrollbar(left, orient='vertical', command=canvas.yview)
    frame  = tk.Frame(canvas, bg=BG, padx=16, pady=12)

    frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    canvas.create_window((0, 0), window=frame, anchor='nw')
    canvas.configure(yscrollcommand=scroll.set)
    canvas.pack(side='left', fill='both', expand=True)
    scroll.pack(side='right', fill='y')

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TCombobox', fieldbackground=CARD, background=CARD,
                    foreground=TEXTO, selectbackground=AZUL)

    vars_tk = {}

    def campo(padre, etiqueta, opciones=None, tipo='combo', desde=1, hasta=50, default=None):
        blk = tk.Frame(padre, bg=CARD, padx=12, pady=8,
                       relief='flat', bd=0, highlightthickness=1,
                       highlightbackground='#E5E7EB')
        blk.pack(fill='x', pady=3)
        tk.Label(blk, text=etiqueta, font=('Helvetica', 9, 'bold'),
                 fg=MUTED, bg=CARD).pack(anchor='w')

        if tipo == 'combo':
            v = tk.StringVar(value=default or opciones[0])
            cb = ttk.Combobox(blk, textvariable=v, values=opciones,
                               state='readonly', font=('Helvetica', 11))
            cb.pack(fill='x', pady=(4, 0))
            return v

        if tipo == 'slider':
            v = tk.IntVar(value=default or desde)
            row = tk.Frame(blk, bg=CARD)
            row.pack(fill='x', pady=(4, 0))
            lbl = tk.Label(row, text=str(v.get()), font=('Helvetica', 11, 'bold'),
                           fg=AZUL, bg=CARD, width=5)
            lbl.pack(side='right')
            sl = ttk.Scale(row, from_=desde, to=hasta, variable=v, orient='horizontal',
                           command=lambda e: lbl.config(text=str(int(float(e)))))
            sl.pack(fill='x', side='left', expand=True)
            return v

    def seccion(texto):
        tk.Label(frame, text=texto, font=('Helvetica', 10, 'bold'),
                 fg=AZUL, bg=BG).pack(anchor='w', pady=(10, 2))

    seccion("Características del producto")
    vars_tk['cat']   = campo(frame, "Categoría de producto",
                              ['Electrónica','Ropa y Moda','Hogar y Deco','Deportes','Belleza'])
    vars_tk['canal'] = campo(frame, "Canal de venta", ['Online','Tienda física'])

    seccion("Perfil del cliente")
    vars_tk['seg']    = campo(frame, "Segmento de cliente",
                               ['Gold','Platinum','Silver','Básico'])
    vars_tk['region'] = campo(frame, "Región",
                               ['Lima','Arequipa','Trujillo','Piura','Cusco'])
    vars_tk['compras'] = campo(frame, "Número de compras previas",
                                tipo='slider', desde=1, hasta=50, default=15)
    vars_tk['meses']   = campo(frame, "Meses como cliente en Falabella",
                                tipo='slider', desde=1, hasta=84, default=24)

    seccion("Detalles de la compra")
    vars_tk['descuento'] = campo(frame, "Descuento aplicado (%)",
                                  tipo='slider', desde=0, hasta=40, default=10)
    vars_tk['productos'] = campo(frame, "Productos distintos en el carrito",
                                  tipo='slider', desde=1, hasta=14, default=3)

    # ── Botón predecir (parte inferior izquierda) ──
    btn_frame = tk.Frame(left, bg=BG, pady=8, padx=16)
    btn_frame.pack(fill='x', side='bottom')

    btn = tk.Button(btn_frame, text="Predecir ticket promedio",
                    font=('Helvetica', 12, 'bold'),
                    bg=AZUL, fg='white', activebackground='#0C447C',
                    relief='flat', pady=10, cursor='hand2')
    btn.pack(fill='x')

    # ─── COLUMNA DERECHA: resultado + gráfico ───
    right = tk.Frame(main, bg=BG)
    right.pack(side='left', fill='both', expand=True, padx=10, pady=10)

    # Tarjeta de resultado
    resultado_frame = tk.Frame(right, bg=VERDE, pady=12, padx=20)
    resultado_frame.pack(fill='x', pady=(0, 10))

    lbl_resultado = tk.Label(resultado_frame,
                             text="Ingresa los datos y presiona Predecir",
                             font=('Helvetica', 15, 'bold'),
                             fg='white', bg=VERDE)
    lbl_resultado.pack()

    lbl_sub = tk.Label(resultado_frame, text="",
                        font=('Helvetica', 10), fg='#9FE1CB', bg=VERDE)
    lbl_sub.pack(pady=(4, 0))

    # Tarjeta de contribución de variables
    grafico_card = tk.Frame(right, bg=CARD, highlightthickness=1,
                            highlightbackground='#E5E7EB')
    grafico_card.pack(fill='both', expand=True)

    tk.Label(grafico_card, text="Contribución de cada variable a la predicción",
             font=('Helvetica', 10, 'bold'), fg=AZUL, bg=CARD).pack(anchor='w', padx=12, pady=(8, 0))

    fig_contrib, ax_contrib = plt.subplots(figsize=(5.5, 4.5))
    fig_contrib.patch.set_facecolor(CARD)
    ax_contrib.set_facecolor(CARD)
    ax_contrib.text(0.5, 0.5, "Presiona 'Predecir'\npara ver el análisis",
                    ha='center', va='center', fontsize=11, color=MUTED,
                    transform=ax_contrib.transAxes)
    ax_contrib.axis('off')

    canvas_fig = FigureCanvasTkAgg(fig_contrib, master=grafico_card)
    canvas_fig.get_tk_widget().pack(fill='both', expand=True, padx=8, pady=8)

    # ── Lógica de predicción ──
    def on_predecir():
        try:
            cat       = vars_tk['cat'].get()
            seg       = vars_tk['seg'].get()
            canal     = vars_tk['canal'].get()
            region    = vars_tk['region'].get()
            compras   = int(vars_tk['compras'].get())
            meses     = int(vars_tk['meses'].get())
            descuento = float(vars_tk['descuento'].get())
            productos = int(vars_tk['productos'].get())

            ticket = predecir_ticket(cat, seg, canal, region, compras, meses, descuento, productos)

            lbl_resultado.config(text=f"Ticket estimado: S/ {ticket:,.2f}")
            rango_inf = max(0, ticket - 93.46)
            rango_sup = ticket + 93.46
            lbl_sub.config(
                text=f"Rango probable: S/ {rango_inf:,.2f} – S/ {rango_sup:,.2f}   (±MAE S/ 93.46)"
            )

            # ── Gráfico de contribución ──
            contribuciones = {
                f"Seg: {seg}":       COEFS_MODELO.get(f'segmento_cliente_{seg}', 0),
                f"Cat: {cat}":       COEFS_MODELO.get(f'categoria_{cat}', 0),
                f"Canal: {canal}":   COEFS_MODELO.get(f'canal_{canal}', 0),
                f"Región: {region}": COEFS_MODELO.get(f'region_{region}', 0),
                "Compras previas":   COEFS_MODELO['compras_previas'] * compras,
                "Meses cliente":     COEFS_MODELO['meses_cliente'] * meses,
                "Descuento":         COEFS_MODELO['descuento_aplicado'] * descuento,
                "Prod. distintos":   COEFS_MODELO['productos_distintos'] * productos,
            }

            nombres = list(contribuciones.keys())
            valores = list(contribuciones.values())
            colores = ['#1D9E75' if v >= 0 else '#D85A30' for v in valores]

            orden = sorted(range(len(valores)), key=lambda i: valores[i])
            nombres = [nombres[i] for i in orden]
            valores = [valores[i] for i in orden]
            colores = [colores[i] for i in orden]

            ax_contrib.clear()
            ax_contrib.set_facecolor(CARD)
            bars = ax_contrib.barh(nombres, valores, color=colores, edgecolor='white', height=0.6)
            ax_contrib.axvline(0, color='#9CA3AF', linewidth=0.8)

            for bar, val in zip(bars, valores):
                xpos = val + (8 if val >= 0 else -8)
                ha   = 'left' if val >= 0 else 'right'
                ax_contrib.text(xpos, bar.get_y() + bar.get_height() / 2,
                                f"S/{val:+.0f}", va='center', ha=ha, fontsize=8, color=TEXTO)

            ax_contrib.set_xlabel("Impacto en S/ sobre el ticket", fontsize=9, color=TEXTO)
            ax_contrib.tick_params(axis='y', labelsize=8.5, colors=TEXTO)
            ax_contrib.tick_params(axis='x', labelsize=8, colors=TEXTO)
            ax_contrib.spines[['top', 'right']].set_visible(False)
            ax_contrib.spines[['left', 'bottom']].set_color('#E5E7EB')
            fig_contrib.tight_layout(pad=1.2)
            canvas_fig.draw()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    btn.config(command=on_predecir)
    root.mainloop()


# ──────────────────────────────────────────────
#  6. MAIN — ejecuta todo en orden
# ──────────────────────────────────────────────
if __name__ == '__main__':
    print("\n Generando dataset simulado de Falabella Perú...")
    df = generar_dataset(n=1200)
    df.to_csv('dataset_falabella.csv', index=False)
    print(f"  Dataset guardado: dataset_falabella.csv ({len(df)} registros)")

    print("\n Entrenando modelo de regresión lineal múltiple...")
    modelo, metricas, coeficientes, columnas, y_test, y_pred = entrenar_modelo(df)

    imprimir_reporte(metricas, coeficientes)

    print(" Generando gráficos de evaluación...")
    mostrar_graficos(metricas, coeficientes, y_test, y_pred)

    print(" Lanzando interfaz de predicción...\n")
    lanzar_interfaz()
