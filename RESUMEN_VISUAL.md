# 🎯 RESUMEN VISUAL - Interfaz Oechsle Perú (Quick Reference)

## ⚡ CHECKLIST EN 5 PASOS

```
PASO 1: ELIGE LA CATEGORÍA              PASO 2: ELIGE EL CANAL
┌─────────────────────────┐             ┌──────────────────┐
│ • Electrónica    +289   │             │ • Online    -24  │
│ • Hogar y Deco    +85   │             │ • Tienda   +24   │
│ • Ropa y Moda   -145    │             └──────────────────┘
│ • Deportes       -58    │
│ • Belleza       -172    │
└─────────────────────────┘

PASO 3: SELECCIONA SEGMENTO (⭐ MÁS IMPORTANTE)
┌────────────────────────────┐
│ • Platinum    +457 🏆      │  ← MAYOR TICKET
│ • Gold        +39         │
│ • Silver     -177         │
│ • Básico     -319 ▼       │  ← MENOR TICKET
└────────────────────────────┘

PASO 4: AJUSTA LOS SLIDERS (VARIABLES NUMÉRICAS)
┌────────────────────────────────────────────┐
│ Compras previas (1-50)      | +S/ 5.09 c/u │
│ Meses cliente (1-84)        | +S/ 2.21 c/u │
│ Descuento (0-40%)           | -S/ 2.99 c/u │
│ Productos (1-14)            | +S/ 16.39 c/u│
└────────────────────────────────────────────┘

PASO 5: PRESIONA "PREDECIR TICKET PROMEDIO" → ✅ VER RESULTADO
```

---

## 📊 TABLA DE IMPACTOS (Cuánto sube/baja cada variable)

### VARIABLES CATEGÓRICAS (Valor Fijo)

| **SEGMENTO** | Impacto | **CATEGORÍA** | Impacto |
|---|---|---|---|
| Platinum ⭐⭐⭐ | **+S/ 457** | Electrónica ⭐⭐⭐ | **+S/ 289** |
| Gold | +S/ 39 | Hogar y Deco | +S/ 85 |
| Silver | -S/ 177 | Ropa y Moda | -S/ 145 |
| Básico | -S/ 319 | Deportes | -S/ 58 |
| | | Belleza | -S/ 172 |

| **CANAL** | Impacto | **REGIÓN** | Impacto |
|---|---|---|---|
| Tienda física | +S/ 24 | Cusco | +S/ 10 |
| Online | -S/ 24 | Piura | +S/ 7 |
| | | Arequipa | -S/ 7 |
| | | Trujillo | -S/ 8 |
| | | Lima | -S/ 3 |

### VARIABLES NUMÉRICAS (Por unidad)
| **Variable** | **Coef** | **Rango** | **Ejemplo** | **Impacto** |
|---|---|---|---|---|
| Compras previas | +5.09 | 1-50 | 10 → +S/ 51 |
| Meses cliente | +2.21 | 1-84 | 24 → +S/ 53 |
| **Productos** | **+16.39** | **1-14** | **5 → +S/ 82** |
| Descuento (%) | -2.99 | 0-40% | 10% → -S/ 30 |

---

## 🎨 LAYOUT DE LA INTERFAZ

```
┌─────────────────────────────────────────────────────────┐
│  OECHSLE PERÚ — Predictor de Ticket Promedio            │
│  R² = 88.3% | MAE = S/ 93.46                            │
└─────────────────────────────────────────────────────────┘

┌──────────────────────────┬──────────────────────────────┐
│   PANEL IZQUIERDO        │   PANEL DERECHO              │
│   (INPUTS)               │   (RESULTADOS)               │
│                          │                              │
│ 📦 PRODUCTO              │ ┌────────────────────────┐   │
│ ├─ Categoría [dropdown]  │ │ S/ 1,234.56            │   │
│ └─ Canal [dropdown]      │ │ Rango: S/ 1,141-1,328  │   │
│                          │ │ ±MAE S/ 93.46          │   │
│ 👥 CLIENTE               │ └────────────────────────┘   │
│ ├─ Segmento [dropdown]   │                              │
│ ├─ Región [dropdown]     │ 📊 GRÁFICO                   │
│ ├─ Compras [slider]      │ (Contribución de c/variable)│
│ └─ Meses [slider]        │                              │
│                          │ Seg: Platinum    ▰▰▰ +457   │
│ 🛒 COMPRA                │ Cat: Electrónica ▰▰▰ +289   │
│ ├─ Descuento [slider]    │ Productos        ▰▰  +82    │
│ └─ Productos [slider]    │ Meses           ▰  +53      │
│                          │ ...                          │
│ [🔵 PREDECIR TICKET]    │                              │
│                          │                              │
└──────────────────────────┴──────────────────────────────┘
```

---

## 🧮 CÁLCULO SIMPLIFICADO

```
BASE DE CÁLCULO:
┌──────────────────────────────────────────┐
│ Ticket = 425.24 (intercepto)             │
│        + Segmento (Platinum: +457)       │
│        + Categoría (Electrónica: +289)   │
│        + Compras × 5.09                  │
│        + Meses × 2.21                    │
│        + Productos × 16.39               │
│        + Canal (Tienda: +24)             │
│        + Región (Cusco: +10)             │
│        - Descuento × 2.99                │
│        = RESULTADO FINAL ✅              │
└──────────────────────────────────────────┘

LÍMITES:
  Mínimo: S/ 30 (aun con todos negativos)
  Máximo: S/ 3,000 (incluso combinaciones altas)
```

---

## 📈 3 ESCENARIOS TÍPICOS

### 🏆 ESCENARIO 1: VIP (Ticket Alto)
```
Categoría:     Electrónica (+289)
Canal:         Tienda (+24)
Segmento:      Platinum (+457)        ← CLAVE
Región:        Cusco (+10)
Compras:       40 unidades (+204)
Meses:         60 meses (+132)
Descuento:     5% (-15)
Productos:     10 items (+164)
───────────────────────────────
TOTAL:         ~S/ 1,665 ± 93
```

### 💼 ESCENARIO 2: ESTÁNDAR (Ticket Medio)
```
Categoría:     Hogar y Deco (+85)
Canal:         Online (-24)
Segmento:      Gold (+39)             ← CLIENTE NORMAL
Región:        Lima (-3)
Compras:       15 unidades (+76)
Meses:         24 meses (+53)
Descuento:     10% (-30)
Productos:     5 items (+82)
───────────────────────────────
TOTAL:         ~S/ 703 ± 93
```

### 🔵 ESCENARIO 3: ENTRADA (Ticket Bajo)
```
Categoría:     Belleza (-172)
Canal:         Online (-24)
Segmento:      Básico (-319)          ← CLIENTE NUEVO
Región:        Trujillo (-8)
Compras:       3 unidades (+15)
Meses:         1 mes (+2)
Descuento:     25% (-75)
Productos:     1 item (+16)
───────────────────────────────
TOTAL:         ~S/ 260 ± 93
```

---

## 🎯 VARIABLE MÁS INFLUYENTES (TOP 5)

| Ranking | Variable | Coef | Tipo | Acción |
|---------|----------|------|------|--------|
| 🥇 1 | Segmento Platinum | +457 | Categórica | Enfocarse en clientes premium |
| 🥈 2 | Categoría Electrónica | +289 | Categórica | Promover electrónica |
| 🥉 3 | Productos distintos | +16.39 | Numérica | Cross-sell (vender más items) |
| 4 | Compras previas | +5.09 | Numérica | Retención de clientes |
| 5 | Meses cliente | +2.21 | Numérica | Lealtad en el tiempo |

---

## 💡 CASOS DE USO

```
❓ PREGUNTA                          ✅ SOLUCIÓN
─────────────────────────────────────────────────────────
¿Cuánto ganan clientes Platinum?     Predice con Platinum
  vs Básico?                         y Básico, compara

¿Vender a Online vs Tienda?          Predice dos veces,
  ¿Cuál es mejor?                    observa diferencia

¿Vale la pena dar 20% descuento?     Predice con 0% y 20%,
  vs sin descuento?                  calcula el impacto

¿Electrónica vs Belleza rentabilidad? Predice cada una,
                                      ve diferencia (+S/461)

¿Cuánto sube si le vendo              Predice con prod=5
  3 productos más?                    y prod=8, diferencia=+S/49

¿Qué región produce más tickets?      Predice todas las
                                      regiones, compara
```

---

## 🎓 RESUMEN TÉCNICO

| Concepto | Detalle |
|----------|---------|
| **Modelo** | Regresión Lineal Múltiple (scikit-learn) |
| **Variables Input** | 8 (5 categóricas + 3 numéricas) |
| **Variable Output** | 1 (ticket_promedio_soles) |
| **R²** | 0.8834 (88.3% varianza explicada) ✅ |
| **MAE** | S/ 93.46 (error medio absoluto) |
| **RMSE** | S/ 117.61 (error cuadrático) |
| **Registros Training** | 960 (80%) |
| **Registros Test** | 240 (20%) |
| **Interfaz** | Web (HTML + CSS + JavaScript) |
| **Servidor** | HTTP Python (localhost:8080) |
| **Latencia** | ~5 ms por predicción |

---

## ⌨️ ATAJOS ÚTILES

```
NAVEGADOR:
  F12         → Ver consola (para debugging)
  Ctrl+R      → Refrescar página
  Ctrl+L      → Limpiar URL y empezar de nuevo

TERMINAL (mientras se ejecuta interfaz.py):
  Ctrl+C      → Cerrar servidor
  ↑ flecha    → Repetir último comando
```

---

**🎯 USO ÓPTIMO:**
1. Mantén el navegador abierto
2. Ajusta variables lentamente para ver cambios
3. Compara 2-3 escenarios antes de decidir
4. El gráfico muestra exactamente qué influye más
5. Confía en el rango de ±MAE para tus decisiones

**📚 Para más detalles, consulta:** GUIA_INTERFAZ.md (versión completa)
