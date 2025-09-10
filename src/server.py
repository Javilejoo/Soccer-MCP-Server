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
    List all teams for a particular competition.
    
    Args:
        competition_id: competition id (e.g., "PL" for Premier League, "CL" for Champions League)

    Returns:
        List of teams in the specified competition
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
    List all available competitions.

    Args:
        None
    
    Returns:
        List of available competitions with their IDs and names
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

@mcp.tool()
async def get_teams_by_competition(competition_id: str):
    """
    List all teams for a particular competition.
    
    Args:
        competition_id: ID of the competition (e.g., "PL" for Premier League, "CL" for Champions League)
    
    Returns:
        List of teams in the specified competition
    """
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("FOOTBALL_BASE")
    timeout = int(os.getenv("HTTP_TIMEOUT", "10"))
    
    if not api_key or not base_url:
        return {"error": "API_KEY or FOOTBALL_BASE not set in .env"}
    
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
async def get_matches_by_competition(competition_id: str):
    """
    List all matches for a particular competition.
    
    Args:
        competition_id: competition id (e.g., "PL" for Premier League, "CL" for Champions League)
    
    Returns:
        List of matches in the specified competition
    """
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("FOOTBALL_BASE")
    timeout = int(os.getenv("HTTP_TIMEOUT", "10"))
    
    if not api_key or not base_url:
        return {"error": "API_KEY o FOOTBALL_BASE no están configurados en .env"}
    
    url = f"{base_url}/competitions/{competition_id}/matches"
    headers = {"X-Auth-Token": api_key}
    
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": f"Error: {str(e)}"}
    
@mcp.tool()
async def get_team_by_id(team_id: str):
    """
    Show one particular team.
    
    Args:
        team_id: Team id
    
    Returns:
        Details of the specified team
    """
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("FOOTBALL_BASE")
    timeout = int(os.getenv("HTTP_TIMEOUT", "10"))
    
    if not api_key or not base_url:
        return {"error": "API_KEY o FOOTBALL_BASE no están configurados en .env"}
    
    url = f"{base_url}/teams/{team_id}"
    headers = {"X-Auth-Token": api_key}
    
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": f"Error: {str(e)}"}
    
@mcp.tool()
async def get_top_scorers_by_competitions(competition_id: str):
    """
    List top scorers for a particular competition.
    
    Args:
        competition_id: competition id (e.g., "PL" for Premier League, "CL" for Champions League)

    Returns:
        List of top scorers in the specified competition
    """
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("FOOTBALL_BASE")
    timeout = int(os.getenv("HTTP_TIMEOUT", "10"))
    
    if not api_key or not base_url:
        return {"error": "API_KEY o FOOTBALL_BASE no están configurados en .env"}
    
    url = f"{base_url}/competitions/{competition_id}/scorers"
    headers = {"X-Auth-Token": api_key}
    
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": f"Error: {str(e)}"}
    
@mcp.tool()
async def get_player_by_id(player_id: str):
    """
    List one particular person.
    
    Args:
        player_id: Player id

    Returns:
        Details of the specified player
    """
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("FOOTBALL_BASE")
    timeout = int(os.getenv("HTTP_TIMEOUT", "10"))
    
    if not api_key or not base_url:
        return {"error": "API_KEY o FOOTBALL_BASE no están configurados en .env"}
    
    url = f"{base_url}/persons/{player_id}"
    headers = {"X-Auth-Token": api_key}
    
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": f"Error: {str(e)}"}
    
@mcp.tool()
async def get_info_matches_of_a_player(player_id: str):
    """
    Show all matches for a particular person.
    Args:
        player_id: player id

    Returns:
        List of matches for the specified player
    """
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("FOOTBALL_BASE")
    timeout = int(os.getenv("HTTP_TIMEOUT", "10"))

    if not api_key or not base_url:
        return {"error": "API_KEY o FOOTBALL_BASE no están configurados en .env"}

    url = f"{base_url}/persons/{player_id}/matches"
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