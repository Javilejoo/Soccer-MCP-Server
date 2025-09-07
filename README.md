# Soccer MCP Server ⚽

A Model Context Protocol (MCP) server that provides real-time access to football/soccer data through the Football-Data.org API. This server acts as a "bridge" between Claude a## 📝 Limitations

- **Free plan**: 10 calls per minute
- **Historical data**: Limited in the free plan
- **Competitions**: Not all leagues are available in the free plan

## 🔗 Useful Links

- [Football-Data.org](https://www.football-data.org/) - Football data API
- [Claude Desktop](https://claude.ai/download) - Claude client
- [Model Context Protocol](https://modelcontextprotocol.io/) - Official MCP documentation
- [FastMCP](https://github.com/jlowin/fastmcp) - Framework for MCP servers

---

⚽ **Enjoy querying football data with Claude!** ⚽ources to answer football-related questions.

## 🌟 Features

- **Get teams by competition**: Query all teams from a specific league
- **List available competitions**: View all available leagues and tournaments
- **Claude integration**: Works seamlessly with Claude Desktop
- **Reliable API**: Uses Football-Data.org as the data source

## 📋 Prerequisites

- **Python 3.8+** installed on your system
- **Football-Data.org account** to get a free API key
- **Claude Desktop** (to use the MCP server)

## 🔑 Getting your Football-Data.org API Key

1. **Visit**: [https://www.football-data.org/](https://www.football-data.org/)
2. **Register**: Click "Register" and create a free account
3. **Verify your email**: Confirm your account through the verification email
4. **Get your API key**: 
   - Log into your account
   - Go to your dashboard/profile
   - Copy your **API Token**

### Free plan includes:
- ✅ 10 calls per minute
- ✅ Access to major competitions
- ✅ Basic team and player data

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Javilejoo/Soccer-MCP-Server.git
cd Soccer-MCP-Server
```

### 2. Create virtual environment
```bash
# On Windows
python -m venv soccervenv
soccervenv\Scripts\activate

# On macOS/Linux
python3 -m venv soccervenv
source soccervenv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root:
```env
API_KEY=your_api_key_here
FOOTBALL_BASE=https://api.football-data.org/v4
HTTP_TIMEOUT=10
```

**Important**: Replace `your_api_key_here` with your actual Football-Data.org API key

## ⚙️ Claude Desktop Configuration

### 1. Locate the configuration file
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### 2. Add MCP configuration
Open the `claude_desktop_config.json` file and add:

```json
{
  "mcpServers": {
    "soccer-mcp-server": {
      "command": "python",
      "args": [
        "C:/full/path/to/your/Soccer-MCP-Server/src/server.py"
      ],
      "env": {
        "PYTHONPATH": "C:/full/path/to/your/Soccer-MCP-Server/soccervenv/Scripts"
      }
    }
  }
}
```

**Important**: 
- Replace `C:/full/path/to/your/Soccer-MCP-Server` with the actual path where you cloned the project
- Use forward slashes (`/`) even on Windows for JSON configuration

### 3. Restart Claude Desktop
Completely close Claude Desktop and reopen it to load the new configuration.

## 🎮 Usage

Once configured, you can ask Claude questions like:

### Example questions:

**Get teams from a league:**
- "What are the teams in the Premier League?"
- "Show me all teams in La Liga"
- "Which teams play in Serie A?"

**View available competitions:**
- "What football competitions are available?"
- "Show me all leagues"
- "What tournaments can I query?"

### Common competition codes:
- `PL` - Premier League (England)
- `PD` - Primera División / La Liga (Spain)
- `BL1` - Bundesliga (Germany)
- `SA` - Serie A (Italy)
- `FL1` - Ligue 1 (France)
- `CL` - Champions League
- `WC` - World Cup

## 🛠️ Available Tools

### `get_teams_competitions(competition_id: str)`
Gets all teams from a specific competition.

**Parameters:**
- `competition_id`: Competition code (e.g., "PL", "CL", "BL1")

**Example response:**
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
Gets all available competitions.

**Example response:**
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

## 🔧 Project Structure

```
Soccer-MCP-Server/
├── src/
│   └── server.py          # Main MCP server
├── soccervenv/            # Python virtual environment
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🐛 Troubleshooting

### Error: "API_KEY not configured"
- Verify that the `.env` file exists in the project root
- Make sure the API key is correctly configured without extra spaces

### Error: "MCP server not found"
- Verify that the path in `claude_desktop_config.json` is correct
- Make sure to use forward slashes (`/`) in paths
- Restart Claude Desktop completely

### Error: "HTTP 401 Unauthorized"
- Your API key might be invalid or expired
- Check your Football-Data.org account
- Generate a new API key if necessary

### Error: "HTTP 429 Too Many Requests"
- You've exceeded the 10 calls per minute limit of the free plan
- Wait one minute before making more queries

## 📝 Limitations

- **Free plan**: 10 calls per minute
- **Historical data**: Limited in the free plan
- **Competitions**: Not all leagues are available in the free plan


## 🔗 Enlaces útiles

- [Football-Data.org](https://www.football-data.org/) - API de datos de fútbol
- [Claude Desktop](https://claude.ai/download) - Cliente de Claude
- [Model Context Protocol](https://modelcontextprotocol.io/) - Documentación oficial de MCP
- [FastMCP](https://github.com/jlowin/fastmcp) - Framework para servidores MCP

---

⚽ **¡Disfruta consultando datos de fútbol con Claude!** ⚽Soccer-MCP-Server
MCP server de futbol cuyo propósito es consultar datos de fútbol El servidor actuará como “puente” entre un cliente/LLM y una fuente de datos externa, para responder preguntas sobre futbol  
