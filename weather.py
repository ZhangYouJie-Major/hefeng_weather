import os
from typing import Any

import argparse
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("heFeng_weather")


def get_api_config() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument("--WEATHER_API_BASE", type=str, help="和风 API 基础 URL")
    parser.add_argument("--WEATHER_API_KEY", type=str, help="和风 API Key")
    args, _ = parser.parse_known_args()

    # 返回多个配置项
    return {
        'WEATHER_API_BASE': args.WEATHER_API_BASE,
        'WEATHER_API_KEY': args.WEATHER_API_KEY
    }


async def make_weather_request(endpoint: str, params: dict = None) -> dict[str, Any] | None:
    """Make a request to the QWeather API with proper error handling."""
    if params is None:
        params = {}

    config = get_api_config()

    # Add the API key to the params
    WEATHER_API_BASE = config['WEATHER_API_BASE']
    params['key'] = config['WEATHER_API_KEY']

    url = f"{WEATHER_API_BASE}/{endpoint}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params, timeout=30.0)
            response.raise_for_status()
            data = response.json()

            # Check if the API response is successful
            if data.get('code') == '200':
                return data
            return None
        except Exception:
            return None


def format_forecast(day: dict) -> str:
    """Format a daily forecast into a readable string."""
    return f"""
日期: {day['fxDate']}
温度: {day['tempMin']}°C - {day['tempMax']}°C
天气: {day['textDay']} (白天) / {day['textNight']} (夜间)
风况: {day['windDirDay']} {day['windScaleDay']}级
湿度: {day['humidity']}%
紫外线指数: {day['uvIndex']}
降水量: {day['precip']}毫米
气压: {day['pressure']}百帕
能见度: {day['vis']}公里
云量: {day['cloud']}%
月相: {day['moonPhase']}
日出: {day['sunrise']}
日落: {day['sunset']}
"""


@mcp.tool()
async def get_forecast(location: str) -> str:
    """Get weather forecast for a location.

    Args:
        location: Location ID (e.g. 101010100 for Beijing)
    """
    data = await make_weather_request('v7/weather/3d', {'location': location})

    if not data or 'daily' not in data:
        return "Unable to fetch forecast data for this location."

    forecasts = [format_forecast(day) for day in data['daily']]
    return "\n---\n".join(forecasts)


@mcp.tool()
async def get_location_id(city_name: str) -> str | Any:
    """Query the location id by city name. Returns the location id of the first matching city, or None if no match is found.
    
    Args:
        city_name: The name of the city to query
    """
    data = await make_weather_request('geo/v2/city/lookup', {'location': city_name})
    if not data or 'location' not in data:
        return "No matching cities found."
    return data['location'][0]['id']


if __name__ == "__main__":
    mcp.run(transport='stdio')
