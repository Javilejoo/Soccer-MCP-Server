# Soccer MCP Server ⚽

Un servidor MCP (Model Context Protocol) que proporciona acceso a datos de fútbol en tiempo real a través de la API de Football-Data.org. Este servidor actúa como "puente" entre Claude y una fuente de datos externa para responder preguntas sobre fútbol.

## 🌟 Características

- **Obtener equipos por competición**: Consulta todos los equipos de una liga específica
- **Listar competiciones disponibles**: Ve todas las ligas y torneos disponibles
- **Integración con Claude**: Funciona perfectamente con Claude Desktop
- **API confiable**: Utiliza Football-Data.org como fuente de datos

## 📋 Requisitos previos

- **Python 3.8+** instalado en tu sistema
- **Cuenta en Football-Data.org** para obtener una API key gratuita
- **Claude Desktop** (para usar el servidor MCP)

## 🔑 Obtener tu API Key de Football-Data.org

1. **Visita**: [https://www.football-data.org/](https://www.football-data.org/)
2. **Regístrate**: Haz clic en "Register" y crea una cuenta gratuita
3. **Verifica tu email**: Confirma tu cuenta a través del correo de verificación
4. **Obtén tu API key**: 
   - Inicia sesión en tu cuenta
   - Ve a tu dashboard/perfil
   - Copia tu **API Token**

### Plan gratuito incluye:
- ✅ 10 llamadas por minuto
- ✅ Acceso a competiciones principales
- ✅ Datos de equipos y jugadores básicos

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/Javilejoo/Soccer-MCP-Server.git
cd Soccer-MCP-Server
```

### 2. Crear entorno virtual
```bash
# En Windows
python -m venv soccervenv
soccervenv\Scripts\activate

# En macOS/Linux
python3 -m venv soccervenv
source soccervenv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto:
```env
API_KEY=tu_api_key_aquí
FOOTBALL_BASE=https://api.football-data.org/v4
HTTP_TIMEOUT=10
```

**Importante**: Reemplaza `tu_api_key_aquí` con tu API key real de Football-Data.org

## ⚙️ Configuración en Claude Desktop

### 1. Localizar el archivo de configuración
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### 2. Agregar configuración MCP
Abre el archivo `claude_desktop_config.json` y agrega:

```json
{
  "mcpServers": {
    "soccer-mcp-server": {
      "command": "python",
      "args": [
        "C:/ruta/completa/a/tu/Soccer-MCP-Server/src/server.py"
      ],
      "env": {
        "PYTHONPATH": "C:/ruta/completa/a/tu/Soccer-MCP-Server/soccervenv/Scripts"
      }
    }
  }
}
```

**Importante**: 
- Reemplaza `C:/ruta/completa/a/tu/Soccer-MCP-Server` con la ruta real donde clonaste el proyecto
- Usa barras diagonales (`/`) incluso en Windows para la configuración JSON

### 3. Reiniciar Claude Desktop
Cierra completamente Claude Desktop y vuelve a abrirlo para que cargue la nueva configuración.

## 🎮 Uso

Una vez configurado, puedes hacer preguntas a Claude como:

### Ejemplos de preguntas:

**Obtener equipos de una liga:**
- "¿Cuáles son los equipos de la Premier League?"
- "Muéstrame todos los equipos de La Liga"
- "¿Qué equipos juegan en la Serie A?"

**Ver competiciones disponibles:**
- "¿Qué competiciones de fútbol están disponibles?"
- "Muéstrame todas las ligas"
- "¿Qué torneos puedo consultar?"

### Códigos de competiciones comunes:
- `PL` - Premier League (Inglaterra)
- `PD` - Primera División / La Liga (España)
- `BL1` - Bundesliga (Alemania)
- `SA` - Serie A (Italia)
- `FL1` - Ligue 1 (Francia)
- `CL` - Champions League
- `WC` - Copa del Mundo

## 🛠️ Herramientas disponibles

### `get_teams_competitions(competition_id: str)`
Obtiene todos los equipos de una competición específica.

**Parámetros:**
- `competition_id`: Código de la competición (ej: "PL", "CL", "BL1")

**Ejemplo de respuesta:**
```json
{
  "count": 20,
  "teams": [
    {
      "id": 57,
      "name": "Arsenal FC",
      "shortName": "Arsenal",
      "founded": 1886,
      "venue": "Emirates Stadium"
    }
  ]
}
```

### `get_competitions()`
Obtiene todas las competiciones disponibles.

**Ejemplo de respuesta:**
```json
{
  "count": 35,
  "competitions": [
    {
      "id": 2021,
      "name": "Premier League",
      "code": "PL",
      "area": {
        "name": "England"
      }
    }
  ]
}
```

## 🔧 Estructura del proyecto

```
Soccer-MCP-Server/
├── src/
│   └── server.py          # Servidor MCP principal
├── soccervenv/            # Entorno virtual Python
├── .env                   # Variables de entorno
├── requirements.txt       # Dependencias Python
└── README.md             # Este archivo
```

## 🐛 Solución de problemas

### Error: "API_KEY no está configurado"
- Verifica que el archivo `.env` existe en la raíz del proyecto
- Asegúrate de que la API key está correctamente configurada sin espacios extra

### Error: "Servidor MCP no encontrado"
- Verifica que la ruta en `claude_desktop_config.json` es correcta
- Asegúrate de usar barras diagonales (`/`) en las rutas
- Reinicia Claude Desktop completamente

### Error: "HTTP 401 Unauthorized"
- Tu API key puede ser inválida o haber expirado
- Verifica tu cuenta en Football-Data.org
- Genera una nueva API key si es necesario

### Error: "HTTP 429 Too Many Requests"
- Has excedido el límite de 10 llamadas por minuto del plan gratuito
- Espera un minuto antes de hacer más consultas

## 📝 Limitaciones

- **Plan gratuito**: 10 llamadas por minuto
- **Datos históricos**: Limitados en el plan gratuito
- **Competiciones**: No todas las ligas están disponibles en el plan gratuito


## 🔗 Enlaces útiles

- [Football-Data.org](https://www.football-data.org/) - API de datos de fútbol
- [Claude Desktop](https://claude.ai/download) - Cliente de Claude
- [Model Context Protocol](https://modelcontextprotocol.io/) - Documentación oficial de MCP
- [FastMCP](https://github.com/jlowin/fastmcp) - Framework para servidores MCP

---

⚽ **¡Disfruta consultando datos de fútbol con Claude!** ⚽Soccer-MCP-Server
MCP server de futbol cuyo propósito es consultar datos de fútbol El servidor actuará como “puente” entre un cliente/LLM y una fuente de datos externa, para responder preguntas sobre futbol  
