import os
import httpx
from dotenv import load_dotenv
from fastmcp import FastMCP

# Cargar variables de entorno
load_dotenv()

mcp = FastMCP("Soccer-MCP-Server")

@mcp.tool()
async def get_teams_competitions(competition_id: str):
    """
    Obtiene los equipos de una competición específica.
    
    Args:
        competition_id: ID de la competición (ej: "PL" para Premier League, "CL" para Champions League)
    
    Returns:
        Lista de equipos de la competición especificada
    """
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("FOOTBALL_BASE")
    timeout = int(os.getenv("HTTP_TIMEOUT", "10"))
    
    if not api_key or not base_url:
        return {"error": "API_KEY o FOOTBALL_BASE no están configurados en .env"}
    
    url = f"{base_url}/competitions/{competition_id}/teams"
    headers = {"X-Auth-Token": api_key}
    
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": f"Error: {str(e)}"}

@mcp.tool()
async def get_competitions():
    """
    Obtiene todas las competiciones disponibles.
    
    Returns:
        Lista de competiciones disponibles con sus IDs y nombres
    """
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("FOOTBALL_BASE")
    timeout = int(os.getenv("HTTP_TIMEOUT", "10"))
    
    if not api_key or not base_url:
        return {"error": "API_KEY o FOOTBALL_BASE no están configurados en .env"}
    
    url = f"{base_url}/competitions"
    headers = {"X-Auth-Token": api_key}
    
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": f"Error: {str(e)}"}

if __name__ == "__main__":
    mcp.run(transport="stdio")