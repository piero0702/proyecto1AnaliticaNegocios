"""
Interfaz web — Predictor de Ticket Oechsle Perú
Ejecutar: python3 interfaz.py
Abre automáticamente en el navegador en http://localhost:8080
"""
import http.server, webbrowser, threading, json, urllib.parse, os

os.environ['TK_SILENCE_DEPRECATION'] = '1'

COEFS = {
    'intercepto': 425.24,
    'compras_previas': 5.087,
    'meses_cliente': 2.211,
    'descuento_aplicado': -2.987,
    'productos_distintos': 16.388,
    'categoria_Belleza': -171.819,
    'categoria_Deportes': -57.856,
    'categoria_Electronica': 289.256,
    'categoria_Hogar_y_Deco': 85.010,
    'categoria_Ropa_y_Moda': -144.591,
    'canal_Online': -23.662,
    'canal_Tienda_fisica': 23.662,
    'region_Arequipa': -6.635,
    'region_Cusco': 9.766,
    'region_Lima': -2.929,
    'region_Piura': 7.498,
    'region_Trujillo': -7.700,
    'segmento_Basico': -318.752,
    'segmento_Gold': 39.014,
    'segmento_Platinum': 456.675,
    'segmento_Silver': -176.937,
}

HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Predictor de Ticket — Oechsle Perú</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Helvetica, sans-serif; background: #F5F5F5; color: #25252E; }

  header { background: #FF0705; color: white; text-align: center; padding: 20px 16px 16px; }
  header h1 { font-size: 22px; margin-bottom: 4px; }
  header p  { font-size: 13px; color: #FFD5D5; }
  header small { font-size: 11px; color: #FFB3B3; display: block; margin-top: 4px; }

  .layout { display: flex; gap: 20px; padding: 20px; max-width: 1100px; margin: 0 auto; }

  .card { background: white; border-radius: 10px; border: 1px solid #E5E5E5; padding: 16px 18px; margin-bottom: 12px; }
  .card h3 { font-size: 12px; color: #777777; font-weight: 600; margin-bottom: 10px; text-transform: uppercase; letter-spacing: .5px; }

  label { display: block; font-size: 12px; font-weight: 600; color: #444444; margin-bottom: 4px; margin-top: 10px; }
  select, input[type=range] { width: 100%; }
  select { padding: 8px 10px; border: 1px solid #E5E5E5; border-radius: 6px; font-size: 14px; background: white; }
  select:focus { outline: none; border-color: #FF0705; }

  .slider-row { display: flex; align-items: center; gap: 10px; }
  input[type=range] { flex: 1; accent-color: #FF0705; }
  .slider-val { min-width: 38px; text-align: right; font-weight: 700; color: #FF0705; font-size: 15px; }

  .col-left  { flex: 0 0 380px; }
  .col-right { flex: 1; }

  #btn { width: 100%; padding: 13px; background: #FF0705; color: white; border: none;
         border-radius: 8px; font-size: 15px; font-weight: 700; cursor: pointer; margin-top: 4px; }
  #btn:hover { background: #BC0000; }

  #resultado { background: #25252E; border-radius: 10px; color: white; text-align: center;
               padding: 18px; margin-bottom: 14px; }
  #resultado h2 { font-size: 26px; }
  #resultado p  { font-size: 13px; color: #B5B5B5; margin-top: 6px; }

  .chart-card { background: white; border-radius: 10px; border: 1px solid #E5E5E5; padding: 16px 18px; }
  .chart-card h3 { font-size: 13px; font-weight: 700; color: #FF0705; margin-bottom: 14px; }

  .bar-row { display: flex; align-items: center; margin-bottom: 9px; font-size: 12px; }
  .bar-label { flex: 0 0 130px; text-align: right; padding-right: 10px; color: #444444; font-size: 11px; }
  .bar-track { flex: 1; position: relative; height: 22px; background: #F5F5F5; border-radius: 4px; overflow: hidden; }
  .bar-fill   { position: absolute; top: 3px; height: 16px; border-radius: 3px; transition: width .4s; }
  .bar-fill.pos { background: #3AB1C7; }
  .bar-fill.neg { background: #BC0000; }
  .bar-num { flex: 0 0 70px; padding-left: 8px; font-weight: 700; font-size: 11px; color: #444444; }

  .placeholder { text-align: center; color: #B5B5B5; font-size: 14px; padding: 40px 0; }

  @media (max-width: 700px) { .layout { flex-direction: column; } .col-left { flex: none; } }
</style>
</head>
<body>

<header>
  <h1>Oechsle Perú</h1>
  <p>Modelo Predictivo · Ticket Promedio de Compra</p>
  <small>Regresión Lineal Múltiple &nbsp;·&nbsp; R² = 88.3% &nbsp;·&nbsp; MAE = S/ 93.46</small>
</header>

<div class="layout">

  <!-- COLUMNA IZQUIERDA -->
  <div class="col-left">

    <div class="card">
      <h3>Características del producto</h3>
      <label>Categoría de producto</label>
      <select id="cat">
        <option>Electrónica</option><option>Ropa y Moda</option>
        <option>Hogar y Deco</option><option>Deportes</option><option>Belleza</option>
      </select>
      <label>Canal de venta</label>
      <select id="canal"><option>Online</option><option>Tienda física</option></select>
    </div>

    <div class="card">
      <h3>Perfil del cliente</h3>
      <label>Segmento de cliente</label>
      <select id="seg"><option>Gold</option><option>Platinum</option><option>Silver</option><option>Básico</option></select>
      <label>Región</label>
      <select id="region"><option>Lima</option><option>Arequipa</option><option>Trujillo</option><option>Piura</option><option>Cusco</option></select>
      <label>Compras previas: <span id="v_compras">15</span></label>
      <div class="slider-row">
        <input type="range" id="compras" min="1" max="50" value="15" oninput="document.getElementById('v_compras').textContent=this.value">
        <span class="slider-val" id="sv_compras">15</span>
      </div>
      <label>Meses como cliente: <span id="v_meses">24</span></label>
      <div class="slider-row">
        <input type="range" id="meses" min="1" max="84" value="24" oninput="document.getElementById('v_meses').textContent=this.value;document.getElementById('sv_meses').textContent=this.value">
        <span class="slider-val" id="sv_meses">24</span>
      </div>
    </div>

    <div class="card">
      <h3>Detalles de la compra</h3>
      <label>Descuento aplicado (%)</label>
      <div class="slider-row">
        <input type="range" id="desc" min="0" max="40" value="10" oninput="document.getElementById('sv_desc').textContent=this.value+'%'">
        <span class="slider-val" id="sv_desc">10%</span>
      </div>
      <label>Productos distintos en el carrito</label>
      <div class="slider-row">
        <input type="range" id="prod" min="1" max="14" value="3" oninput="document.getElementById('sv_prod').textContent=this.value">
        <span class="slider-val" id="sv_prod">3</span>
      </div>
    </div>

    <button id="btn" onclick="predecir()">Predecir ticket promedio</button>
  </div>

  <!-- COLUMNA DERECHA -->
  <div class="col-right">

    <div id="resultado">
      <h2 id="ticket_txt">Ingresa los datos y presiona Predecir</h2>
      <p id="rango_txt"></p>
    </div>

    <div class="chart-card">
      <h3>Contribución de cada variable a la predicción</h3>
      <div id="chart"><p class="placeholder">Presiona "Predecir" para ver el análisis</p></div>
    </div>

  </div>
</div>

<script>
const COEFS = {
  intercepto: 425.24,
  compras_previas: 5.087, meses_cliente: 2.211,
  descuento_aplicado: -2.987, productos_distintos: 16.388,
  'categoria_Electrónica': 289.256, 'categoria_Ropa y Moda': -144.591,
  'categoria_Hogar y Deco': 85.010, 'categoria_Deportes': -57.856,
  'categoria_Belleza': -171.819,
  'canal_Online': -23.662, 'canal_Tienda física': 23.662,
  'region_Lima': -2.929, 'region_Arequipa': -6.635,
  'region_Trujillo': -7.700, 'region_Piura': 7.498, 'region_Cusco': 9.766,
  'segmento_Básico': -318.752, 'segmento_Silver': -176.937,
  'segmento_Gold': 39.014, 'segmento_Platinum': 456.675,
};

function g(id){ return document.getElementById(id); }

function predecir(){
  const cat     = g('cat').value;
  const canal   = g('canal').value;
  const seg     = g('seg').value;
  const region  = g('region').value;
  const compras = +g('compras').value;
  const meses   = +g('meses').value;
  const desc    = +g('desc').value;
  const prod    = +g('prod').value;

  const contribs = {
    ['Seg: '+seg]:       COEFS['segmento_'+seg] || 0,
    ['Cat: '+cat]:       COEFS['categoria_'+cat] || 0,
    ['Canal: '+canal]:   COEFS['canal_'+canal] || 0,
    ['Región: '+region]: COEFS['region_'+region] || 0,
    'Compras previas':   COEFS.compras_previas * compras,
    'Meses cliente':     COEFS.meses_cliente * meses,
    'Descuento':         COEFS.descuento_aplicado * desc,
    'Prod. distintos':   COEFS.productos_distintos * prod,
  };

  let ticket = COEFS.intercepto;
  Object.values(contribs).forEach(v => ticket += v);
  ticket = Math.max(30, Math.min(3000, ticket));

  g('ticket_txt').textContent = 'Ticket estimado: S/ ' + ticket.toLocaleString('es-PE', {minimumFractionDigits:2, maximumFractionDigits:2});
  const ri = Math.max(0, ticket - 93.46), rs = ticket + 93.46;
  g('rango_txt').textContent = `Rango probable: S/ ${ri.toFixed(2)} – S/ ${rs.toFixed(2)}   (±MAE S/ 93.46)`;

  // Barras
  const items = Object.entries(contribs).sort((a,b)=>a[1]-b[1]);
  const maxAbs = Math.max(...items.map(([,v])=>Math.abs(v)), 1);
  let html = '';
  items.forEach(([name, val])=>{
    const pct = (Math.abs(val)/maxAbs*100).toFixed(1);
    const cls = val>=0 ? 'pos' : 'neg';
    const sign = val>=0 ? '+' : '';
    const left = val>=0 ? '50%' : (50 - parseFloat(pct)/2)+'%';
    const w    = (parseFloat(pct)/2)+'%';
    html += `<div class="bar-row">
      <div class="bar-label">${name}</div>
      <div class="bar-track">
        <div class="bar-fill ${cls}" style="left:${val>=0?'50%':((50-parseFloat(pct)/2)+'%')};width:${parseFloat(pct)/2}%"></div>
      </div>
      <div class="bar-num">${sign}S/${Math.round(val)}</div>
    </div>`;
  });
  g('chart').innerHTML = html;
}
</script>
</body>
</html>"""

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML.encode('utf-8'))

PORT = 8080
server = http.server.HTTPServer(('localhost', PORT), Handler)
print(f"\n  Abriendo interfaz en http://localhost:{PORT}")
print("  Presiona Ctrl+C para cerrar.\n")
threading.Timer(0.8, lambda: webbrowser.open(f'http://localhost:{PORT}')).start()
server.serve_forever()
