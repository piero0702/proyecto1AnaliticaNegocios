# 🚀 CHEAT SHEET - Predictor Oechsle (1 página)

## EJECUTAR
```bash
python interfaz.py  → Se abre en http://localhost:8080
```

---

## 5 PASOS PARA PREDECIR

| # | QUÉ HACER | OPCIONES | IMPACTO |
|---|-----------|----------|---------|
| 1️⃣ | **Categoría** | Electrónica, Hogar, Ropa, Deportes, Belleza | -172 a +289 |
| 2️⃣ | **Canal** | Online / Tienda | -24 a +24 |
| 3️⃣ | **Segmento** ⭐ | Platinum, Gold, Silver, Básico | -319 a +457 |
| 4️⃣ | **Región** | Lima, Arequipa, Cusco, Trujillo, Piura | -8 a +10 |
| 5️⃣ | **Sliders** | Compras, Meses, Descuento, Productos | Ver tabla |

---

## FÓRMULA RÁPIDA

```
Ticket = 425 + Seg + Cat + (Compras×5) + (Meses×2) 
         + (Prod×16) + Canal + Región - (Desc×3)
```

---

## IMPACTOS PRINCIPALES

### CATEGORÍA → Sube/Baja
- 📱 Electrónica: **+289** ⬆️⬆️⬆️
- 🛋️ Hogar: **+85** ⬆️
- 👕 Ropa: **-145** ⬇️
- ⚽ Deportes: **-58** ⬇️
- 💄 Belleza: **-172** ⬇️

### SEGMENTO → Sube/Baja ⭐ MÁS IMPORTANTE
- 👑 Platinum: **+457** 🏆
- 💎 Gold: **+39**
- 🥈 Silver: **-177**
- 🔵 Básico: **-319** 📉

### SLIDERS → Por unidad
| Variable | Coef | Rango | +/-  |
|----------|------|-------|------|
| Compras | +5 | 1-50 | ⬆️ |
| Meses | +2 | 1-84 | ⬆️ |
| Productos | +16 | 1-14 | ⬆️ |
| Descuento (%) | -3 | 0-40 | ⬇️ |

---

## 3 EJEMPLOS RÁPIDOS

### 🏆 VIP: Electrónica + Tienda + Platinum
- Base: 425
- Seg: +457
- Cat: +289
- Canal: +24
- 20 compras: +102
- 48 meses: +106
- 5 prod: +82
- 10% desc: -30
- **→ S/ 1,455**

### 💼 NORMAL: Hogar + Online + Gold
- Base: 425
- Seg: +39
- Cat: +85
- Canal: -24
- 15 compras: +76
- 24 meses: +53
- 3 prod: +49
- 15% desc: -45
- **→ S/ 658**

### 🔵 BÁSICO: Belleza + Online + Básico
- Base: 425
- Seg: -319
- Cat: -172
- Canal: -24
- 5 compras: +25
- 6 meses: +13
- 1 prod: +16
- 20% desc: -60
- **→ S/ 304**

---

## RESULTADO VISUAL

```
┌─ TICKET ESTIMADO ─────────────────┐
│  S/ 1,234.56 ± 93.46              │
│  Rango: S/ 1,141 – S/ 1,328       │
└───────────────────────────────────┘

📊 GRÁFICO (Qué sube/baja más):
   
   Seg: Platinum      ▰▰▰▰▰▰▰ +457
   Cat: Electrónica   ▰▰▰▰▰ +289
   Productos          ▰▰ +82
   Meses             ▰ +53
   Compras           ▰ +51
   ──────────────────────────────
   Descuento         ▮ -30
   Canal             ▮ -24
```

---

## COMPARAR ESCENARIOS

✅ **PARA TOMAR DECISIONES:**
1. Predice escenario A
2. Predice escenario B
3. Resta los tickets
4. Elige el que más gana

**Ejemplo:**
- Platinum: S/ 1,400
- Gold: S/ 1,100
- **Diferencia: +S/ 300** → Enfocarse en Platinum

---

## MODELO QUALITY

| Métrica | Valor | Interpretación |
|---------|-------|---|
| **R²** | 0.8834 | Explica 88.3% ✅ |
| **MAE** | S/ 93 | Error promedio |
| **RMSE** | S/ 118 | Penaliza errores |
| **Rango tickets** | S/ 30-3,000 | Datos válidos |

---

## TOP 5 FACTORES

1. 🥇 Segmento cliente (±457 soles)
2. 🥈 Categoría (±289 soles)
3. 🥉 Productos en carrito (±16 c/u)
4. 4️⃣ Compras previas (±5 c/u)
5. 5️⃣ Meses cliente (±2 c/u)

---

## CASOS TÍPICOS

| Caso | Solución |
|------|----------|
| ¿Qué categoría gana más? | Compara Electrónica vs Belleza |
| ¿Tienda o Online? | Predice igual pero canal diferente |
| ¿Vale el descuento? | Compara con 0% y 30% descuento |
| ¿Cliente premium da más? | Compara Platinum vs Básico |
| ¿Cross-sell? | Sube de 3 a 8 productos, observa +80 |

---

## INTERFAZ BUTTONS/INPUTS

```
LEFT PANEL (Inputs):        RIGHT PANEL (Outputs):
─────────────────           ───────────────────
[dropdown] Categoría        [ TICKET: S/ 1,234 ]
[dropdown] Canal            
[dropdown] Segmento         [GRÁFICO]
[dropdown] Región           (Contribuciones)
[slider]   Compras          
[slider]   Meses            
[slider]   Descuento        
[slider]   Productos        
[PREDECIR] ← CLICK AQUÍ    
```

---

## PREGUNTAS → RESPUESTAS (30 segundos)

```
Q: ¿Cuánto vale un cliente Platinum?
A: Predice Platinum - baja por -319 en Básico = diferencia

Q: ¿Debo dar 20% o 5% descuento?
A: Predice ambos → diferencia de -45 soles

Q: ¿Electrónica o Belleza?
A: Electrónica +289, Belleza -172 → diferencia +461 soles

Q: ¿Vender 5 o 10 productos?
A: +5 productos × 16 = +80 soles más

Q: ¿Tienda física es mejor?
A: +24 soles vs Online → diferencia mínima
```

---

## ⚡ TIPS

✅ DO:
- Predice 2-3 escenarios antes de decidir
- Lee el gráfico de contribuciones (qué influye más)
- Confía en el rango ±93 soles
- Usa para pricing y estrategia

❌ DON'T:
- No creas predicciones fuera de S/ 30-3,000
- No extrapolés sin sentido (1000 compras)
- No ignores el MAE (±93 es importante)
- No olvides: es predicción, no realidad exacta

---

📱 **Interfaz web** | 🧮 **R² = 88.3%** | 💰 **MAE = ±S/ 93** | ⚡ **5ms/predicción**

*Para guía completa: ver GUIA_INTERFAZ.md | Para casos: ver RESUMEN_VISUAL.md*
