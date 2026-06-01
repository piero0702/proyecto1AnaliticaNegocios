=====================================================================
  PROYECTO: Analítica de Negocios — Oechsle Perú
  MÓDULO:   Modelo Predictivo Simple (Regresión Lineal Múltiple)
  ALUMNO:   Cesar Andrés
  CURSO:    Analítica de Negocios — Ingeniería de Sistemas
=====================================================================

DESCRIPCIÓN
-----------
Este script implementa un modelo de regresión lineal múltiple para
predecir el ticket promedio de compra (en soles) de clientes de
Oechsle Perú, a partir de variables de perfil de cliente,
categoría de producto, canal de venta y comportamiento de compra.


ARCHIVOS DEL PROYECTO
---------------------
  modelo_predictivo.py     → Script principal (ejecutar este)
  requirements.txt         → Librerías necesarias
  README.txt               → Este archivo
  dataset_oechsle.csv      → Se genera al ejecutar el script
  evaluacion_modelo.png    → Se genera al ejecutar el script


CÓMO EJECUTAR
-------------
Paso 1: Abrir terminal (cmd / PowerShell en Windows, Terminal en Mac)

Paso 2: Instalar librerías (solo la primera vez)
  pip install -r requirements.txt

Paso 3: Ejecutar el modelo
  python modelo_predictivo.py

El script hará automáticamente:
  1. Generar el dataset simulado (1,200 registros)
  2. Entrenar el modelo de regresión lineal múltiple
  3. Mostrar métricas en consola (R², MAE, RMSE)
  4. Mostrar gráficos de evaluación
  5. Abrir la interfaz gráfica de predicción


QUÉ VERÁS EN CONSOLA
---------------------
  - Tamaño del dataset de entrenamiento y prueba
  - R² = 0.8834 (el modelo explica el 88.3% de la varianza)
  - MAE = S/ 93.46 (error promedio de predicción)
  - RMSE = S/ 117.61 (penaliza errores grandes)
  - Top 5 variables más influyentes en el ticket


QUÉ VERÁS EN LA INTERFAZ
-------------------------
  - Formulario con 8 variables de entrada
  - Botón "Predecir ticket promedio"
  - Resultado en soles con rango de confianza (±MAE)


VARIABLE OBJETIVO
-----------------
  ticket_promedio_soles → valor continuo (S/ 30 a S/ 3,000)

VARIABLES PREDICTORAS
---------------------
  categoria           → tipo de producto comprado
  canal               → Online / Tienda física
  region              → Lima, Arequipa, Trujillo, Piura, Cusco
  segmento_cliente    → Básico, Silver, Gold, Platinum
  compras_previas     → número de transacciones históricas (1-50)
  meses_cliente       → antigüedad en programa Oechsle (1-84)
  descuento_aplicado  → porcentaje de descuento (0-40%)
  productos_distintos → variedad de ítems en la compra (1-14)


MÉTRICAS DEL MODELO (para el informe)
--------------------------------------
  Métrica    Valor         Interpretación
  ─────────  ──────────    ──────────────────────────────────────────
  R²         0.8834        El modelo explica el 88.3% de la varianza
  MAE        S/ 93.46      Error promedio absoluto de predicción
  RMSE       S/ 117.61     Raíz del error cuadrático medio

  El R² de 0.8834 indica un ajuste muy bueno para regresión lineal.
  El MAE de S/ 93.46 es aceptable considerando tickets que van de
  S/ 30 a S/ 3,000.


VARIABLES MÁS INFLUYENTES (coeficientes del modelo)
-----------------------------------------------------
  Variable                     Coef.      Interpretación
  ───────────────────────────  ─────────  ────────────────────────────────
  segmento_cliente_Platinum    +456.68    Clientes Platinum suben S/ 457
  categoria_Electrónica        +289.26    Electrónica sube el ticket S/ 289
  segmento_cliente_Básico      -318.75    Clientes Básico bajan S/ 319
  segmento_cliente_Silver      -176.94    Clientes Silver bajan S/ 177
  categoria_Belleza            -171.82    Belleza baja el ticket S/ 172
  productos_distintos          +16.39     Cada producto extra sube S/ 16
  compras_previas              +5.09      Cada compra previa sube S/ 5
  descuento_aplicado           -2.99      Cada 1% descuento baja S/ 3


JUSTIFICACIÓN DEL MODELO (para el informe)
-------------------------------------------
Se eligió regresión lineal múltiple porque:
  1. La variable objetivo (ticket) es continua y numérica
  2. Permite interpretar directamente el impacto de cada variable
  3. Es un modelo simple, explicable y validable ante la gerencia
  4. Tiene un excelente R² (88.3%) que justifica su uso práctico
  5. Scikit-learn permite reentrenarlo fácilmente con datos reales

=====================================================================
