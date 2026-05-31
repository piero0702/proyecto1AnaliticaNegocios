# 📊 Guía de Uso - Predictor de Ticket Oechsle Perú

## 🚀 INICIO RÁPIDO

### ¿Cómo ejecutar la interfaz?
```bash
python interfaz.py
```
- Se abre automáticamente en tu navegador en `http://localhost:8080`
- Para cerrar: presiona **Ctrl+C** en la terminal

---

## 📋 CHECKLIST: PASO A PASO PARA HACER UNA PREDICCIÓN

### **FASE 1️⃣: INICIA EL PROGRAMA**
- [ ] Abre terminal/PowerShell en la carpeta del proyecto
- [ ] Ejecuta: `python interfaz.py`
- [ ] Espera el mensaje: *"Abriendo interfaz en http://localhost:8080"*
- [ ] Se abre automáticamente en tu navegador

---

### **FASE 2️⃣: CARACTERÍSTICAS DEL PRODUCTO (Panel Izquierdo Arriba)**

**Sección:** *"Características del producto"*

#### Paso 1: Selecciona la Categoría
- [ ] Haz clic en el dropdown de **"Categoría de producto"**
- [ ] Elige UNA de estas opciones:
  - `Electrónica` → Sube el ticket ~S/ 289
  - `Ropa y Moda` → Baja el ticket ~S/ 145
  - `Hogar y Deco` → Sube el ticket ~S/ 85
  - `Deportes` → Baja el ticket ~S/ 58
  - `Belleza` → Baja el ticket ~S/ 172
- [ ] Observa que el cambio se verá reflejado cuando presiones "Predecir"

#### Paso 2: Selecciona el Canal de Venta
- [ ] Haz clic en el dropdown de **"Canal de venta"**
- [ ] Elige UNA de estas opciones:
  - `Online` → Baja el ticket ~S/ 24
  - `Tienda física` → Sube el ticket ~S/ 24
- [ ] Esto afecta si la compra es por internet o en tienda

---

### **FASE 3️⃣: PERFIL DEL CLIENTE (Panel Izquierdo Centro)**

**Sección:** *"Perfil del cliente"*

#### Paso 3: Selecciona el Segmento
- [ ] Haz clic en el dropdown de **"Segmento de cliente"**
- [ ] Elige UNA de estas opciones (⭐ **MÁS INFLUYENTE**):
  - `Platinum` → Sube el ticket ~S/ 457 ⬆️ (mayor impacto)
  - `Gold` → Sube el ticket ~S/ 39
  - `Silver` → Baja el ticket ~S/ 177
  - `Básico` → Baja el ticket ~S/ 319 ⬇️ (menor ticket)

#### Paso 4: Selecciona la Región
- [ ] Haz clic en el dropdown de **"Región"**
- [ ] Elige UNA de estas opciones:
  - `Lima` → Baja levemente S/ 3
  - `Arequipa` → Baja S/ 7
  - `Cusco` → Sube S/ 10
  - `Trujillo` → Baja S/ 8
  - `Piura` → Sube S/ 7
- [ ] La región tiene bajo impacto (~S/ 3-10)

#### Paso 5: Ajusta "Compras Previas"
- [ ] Observa el label: **"Compras previas: [número]"**
- [ ] Arrastra el slider horizontal:
  - Rango: **1 a 50** compras
  - Cada compra suma ~S/ 5 al ticket
  - Ejemplo: 10 compras = +S/ 51 aprox.
- [ ] El número se actualiza en tiempo real

#### Paso 6: Ajusta "Meses como Cliente"
- [ ] Observa el label: **"Meses como cliente: [número]"**
- [ ] Arrastra el slider horizontal:
  - Rango: **1 a 84 meses** (~7 años)
  - Cada mes suma ~S/ 2.2 al ticket
  - Ejemplo: 24 meses = +S/ 53 aprox.
- [ ] Los clientes antiguos tienden a comprar más

---

### **FASE 4️⃣: DETALLES DE LA COMPRA (Panel Izquierdo Abajo)**

**Sección:** *"Detalles de la compra"*

#### Paso 7: Ajusta "Descuento Aplicado"
- [ ] Observa el slider de **"Descuento aplicado (%)"**
- [ ] Arrastra el slider horizontal:
  - Rango: **0% a 40%** de descuento
  - **IMPACTO NEGATIVO**: Cada 1% resta ~S/ 3 del ticket
  - Ejemplo: 10% descuento = -S/ 30 aprox.
- [ ] Los descuentos REDUCEN el ticket (lógica: venden más barato)

#### Paso 8: Ajusta "Productos Distintos"
- [ ] Observa el slider de **"Productos distintos en el carrito"**
- [ ] Arrastra el slider horizontal:
  - Rango: **1 a 14 productos** diferentes
  - **IMPACTO POSITIVO**: Cada producto suma ~S/ 16 al ticket
  - Ejemplo: 5 productos = +S/ 82 aprox.
- [ ] Más variedad = carrito más grande

---

### **FASE 5️⃣: GENERAR PREDICCIÓN (Panel Izquierdo Bottom)**

#### Paso 9: Presiona el Botón
- [ ] Haz clic en el botón verde: **"Predecir ticket promedio"**
- [ ] El sistema calcula la predicción en millisegundos

---

### **FASE 6️⃣: VER RESULTADOS (Panel Derecho)**

#### Resultado Principal (Recuadro Verde Grande)
- [ ] Aparece el **"Ticket estimado"** en grandes números
  - Ejemplo: `S/ 1,234.56`
- [ ] Muestra el **"Rango probable"** debajo
  - Ejemplo: `Rango probable: S/ 1,141.10 – S/ 1,327.98   (±MAE S/ 93.46)`
  - ✅ Esto significa: el valor real probablemente esté en ese rango
  - MAE = Error Medio Absoluto del modelo

#### Gráfico de Contribuciones (Debajo)
- [ ] Se actualiza automáticamente con cada predicción
- [ ] Muestra **"Contribución de cada variable a la predicción"**
- [ ] Cada barra horizontal representa:
  - **Barras VERDES (↑)** = variables que SUBEN el ticket
  - **Barras ROJAS (↓)** = variables que BAJAN el ticket
  - **Longitud de la barra** = magnitud del impacto (en soles)
  - **Número al lado** = impacto exacto (±S/ XXX)

---

## 📊 INTERPRETACIÓN DEL GRÁFICO DE CONTRIBUCIONES

### Ejemplo de lectura:
```
Seg: Platinum                        →  verde, +S/ 457    (más influyente)
Cat: Electrónica                     →  verde, +S/ 289
Prod. distintos                      →  verde, +S/ 48     (5 productos × 16)
Meses cliente                        →  verde, +S/ 53     (24 meses × 2.2)
Compras previas                      →  verde, +S/ 76     (15 compras × 5)
Intercepto (base)                    →  verde, +S/ 425
────────────────────────────────────────────────────────
Descuento                            →  rojo,  -S/ 30     (10% × 3)
Canal: Online                        →  rojo,  -S/ 24
Region: Trujillo                     →  rojo,  -S/ 8
────────────────────────────────────────────────────────
TOTAL ESTIMADO                                 = S/ 1,226
```

---

## 🧮 CÓMO FUNCIONA MATEMÁTICAMENTE

### Fórmula del Modelo:
```
Ticket = Intercepto + (Coef₁ × Var₁) + (Coef₂ × Var₂) + ... + (Coef₈ × Var₈)

Ticket = 425.24 + (5.09 × compras) + (2.21 × meses) 
         + (16.39 × productos) + (-2.99 × descuento)
         + (Coef_seg) + (Coef_cat) + (Coef_canal) + (Coef_region)
```

### Variables Numéricas (Impacto Linear):
| Variable | Coef | Rango | Ejemplo | Impacto |
|----------|------|-------|---------|---------|
| Compras previas | +5.09 | 1-50 | 20 compras | +S/ 102 |
| Meses cliente | +2.21 | 1-84 | 36 meses | +S/ 80 |
| Productos distintos | +16.39 | 1-14 | 8 productos | +S/ 131 |
| Descuento (%) | -2.99 | 0-40 | 15% descuento | -S/ 45 |

### Variables Categóricas (Valores Fijos):
| Categoría | Categoría | Coef | Impacto |
|-----------|-----------|------|---------|
| **Segmento** | Platinum | +456.68 | Sube mucho |
| | Gold | +39.01 | Sube poco |
| | Silver | -176.94 | Baja |
| | Básico | -318.75 | Baja mucho |
| **Producto** | Electrónica | +289.26 | Sube mucho |
| | Hogar y Deco | +85.01 | Sube |
| | Ropa y Moda | -144.59 | Baja |
| | Deportes | -57.86 | Baja poco |
| | Belleza | -171.82 | Baja |
| **Canal** | Tienda física | +23.66 | Sube poco |
| | Online | -23.66 | Baja poco |
| **Región** | Cusco | +9.77 | Sube poco |
| | Piura | +7.50 | Sube poco |
| | Lima | -2.93 | Baja poco |
| | Arequipa | -6.64 | Baja poco |
| | Trujillo | -7.70 | Baja poco |

---

## 🎯 EJEMPLOS DE PREDICCIONES

### Escenario 1: Cliente VIP
```
Categoría:        Electrónica
Canal:            Tienda física
Segmento:         Platinum          ← 💎 Cliente premium
Región:           Lima
Compras previas:  40
Meses cliente:    72
Descuento:        5%
Productos:        10

Predicción:
  + Intercepto                       425.24
  + Segmento Platinum           +456.68
  + Categoría Electrónica       +289.26
  + Compras (40×5.09)           +203.60
  + Meses (72×2.21)             +159.12
  + Productos (10×16.39)        +163.90
  + Canal Tienda física         +23.66
  + Región Lima                  -2.93
  - Descuento (5×2.99)          -14.95
  ──────────────────────────────────
  TOTAL ESTIMADO: S/ 1,704.58 ± S/ 93.46
```

### Escenario 2: Cliente Básico
```
Categoría:        Belleza
Canal:            Online
Segmento:         Básico            ← 🔵 Cliente entrada
Región:           Piura
Compras previas:  5
Meses cliente:    3
Descuento:        25%
Productos:        2

Predicción:
  + Intercepto                       425.24
  - Segmento Básico             -318.75
  - Categoría Belleza           -171.82
  + Compras (5×5.09)            +25.45
  + Meses (3×2.21)              +6.63
  + Productos (2×16.39)         +32.78
  - Canal Online                -23.66
  + Región Piura                +7.50
  - Descuento (25×2.99)         -74.75
  ──────────────────────────────────
  TOTAL ESTIMADO: S/ 262.62 ± S/ 93.46
```

---

## 💡 CASOS DE USO - ¿QUÉ PUEDO HACER?

### 1. 📈 Analizar el Impacto de Cambios
- **Pregunta**: ¿Cuánto sube el ticket si cambio de Silver a Gold?
- **Solución**: Haz dos predicciones, una con cada segmento, ¡mira la diferencia!
- **Resultado**: Verás exactamente qué diferencia genera (+S/ ~77)

### 2. 🎁 Simular Estrategias de Descuento
- **Pregunta**: ¿Cuánto pierdo si doy 20% descuento vs 5%?
- **Solución**: Predice dos veces con descuentos diferentes
- **Resultado**: Compara los tickets resultantes

### 3. 📊 Identificar Perfiles Rentables
- **Pregunta**: ¿Qué combinación de factores genera más ventas?
- **Solución**: Prueba múltiples combinaciones (Electrónica + Platinum + Tienda física)
- **Resultado**: Descubre el perfil de cliente más valioso

### 4. 🔍 Validar Hipótesis de Negocio
- **Pregunta**: ¿Los clientes antiguos realmente compran más?
- **Solución**: Compara predicción con 10 meses vs 70 meses
- **Resultado**: Verifica si meses_cliente tiene impacto (~S/ 2.2 × diferencia)

### 5. 🎯 Estrategia de Cross-Selling
- **Pregunta**: ¿Cuánto sube el ticket si le vendo 3 productos más?
- **Solución**: Predice con 5 productos, luego con 8 productos
- **Resultado**: Ves que cada producto suma ~S/ 16.39

### 6. 💰 Planificación de Promociones
- **Pregunta**: ¿Cuál es el ticket promedio por categoría?
- **Solución**: Predice para cada categoría manteniendo otros datos igual
- **Resultado**: Decide dónde enfocarte

---

## 🔧 ELEMENTOS TÉCNICOS

### Variables de la Interfaz HTML
```javascript
id="cat"      → Categoría seleccionada
id="canal"    → Canal de venta
id="seg"      → Segmento de cliente
id="region"   → Región
id="compras"  → Slider compras previas (1-50)
id="meses"    → Slider meses cliente (1-84)
id="desc"     → Slider descuento (0-40%)
id="prod"     → Slider productos (1-14)
```

### Función Principal: `predecir()`
1. Lee los valores de los 8 inputs
2. Calcula la contribución de cada variable
3. Suma todas las contribuciones + intercepto
4. Limita resultado entre S/ 30 y S/ 3,000
5. Muestra ticket + rango de confianza (±MAE)
6. Dibuja gráfico de barras horizontales

### Servidor
- **Puerto**: 8080 (localhost)
- **Tipo**: HTTP simple en Python
- **Formato**: HTML + CSS + JavaScript en vivo (sin recarga)
- **Coeficientes**: Embebidos en JavaScript (no necesita conexión a BD)

---

## ⚠️ LIMITACIONES Y CONSIDERACIONES

### Validez del Modelo
- ✅ R² = **0.8834** → Explica el 88.3% de la varianza (EXCELENTE)
- ✅ MAE = **S/ 93.46** → Error promedio aceptable para el rango de tickets
- ✅ RMSE = **S/ 117.61** → Penaliza errores grandes

### Rango de Datos
- Tickets: S/ 30 a S/ 3,000
- Compras: 1 a 50 transacciones
- Meses: 1 a 84 meses
- Descuento: 0% a 40%
- Productos: 1 a 14 items

### ⚠️ Advertencias
- Las predicciones fuera del rango de entrenamiento pueden ser menos precisas
- El modelo asume relaciones lineales entre variables
- No incluye factores como estacionalidad o promociones especiales
- Los coeficientes son estáticos (entrenados UNA VEZ)

---

## 🎓 CONCLUSIÓN

### La interfaz permite:
1. ✅ **Predecir** tickets de forma instantánea
2. ✅ **Entender** qué variables impactan más
3. ✅ **Comparar** escenarios diferentes
4. ✅ **Simular** estrategias de negocio
5. ✅ **Visualizar** contribuciones de cada factor

### Mejor para:
- Analistas de negocio
- Gerentes de ventas
- Equipos de pricing
- Simulaciones "what-if"
- Capacitación en analytics

---

**Desarrollado por:** Cesar Andrés | Analítica de Negocios - Ingeniería de Sistemas
**Modelo:** Regresión Lineal Múltiple (scikit-learn)
**Precisión:** R² = 88.3% | MAE = S/ 93.46
