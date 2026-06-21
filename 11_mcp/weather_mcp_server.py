#!/usr/bin/env python3
"""
基于 FastMCP 的天气查询服务
AI 助手可通过 MCP 协议调用 get_weather 工具获取实时天气
"""

from fastmcp import FastMCP
import requests

# 创建 MCP 服务实例
mcp = FastMCP(name="Weather Tools")  # [reference:0][reference:1]

# ---------- 地理编码：城市名 → 经纬度 ----------
def geocode_city(city: str):
    """使用 Nominatim 将城市名转为经纬度"""
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json", "limit": 1}
    headers = {"User-Agent": "WeatherMCP/1.0"}
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            return None
        return float(data[0]["lat"]), float(data[0]["lon"])
    except Exception:
        return None

# ---------- 获取天气 ----------
def fetch_weather(lat: float, lon: float):
    """从 Open-Meteo 获取当前天气（免费，无需 API Key）"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "timezone": "auto",
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        current = data.get("current", {})
        return {
            "temperature": current.get("temperature_2m"),
            "humidity": current.get("relative_humidity_2m"),
            "wind_speed": current.get("wind_speed_10m"),
            "unit": "°C",
        }
    except Exception as e:
        return {"error": str(e)}

# ---------- MCP 工具：暴露给 AI 调用 ----------
@mcp.tool
def get_weather(city: str) -> dict:
    """
    获取指定城市的实时天气信息

    Args:
        city: 城市名称，如 "北京"、"London"、"Tokyo"

    Returns:
        包含温度、湿度、风速的字典
        示例: {"temperature": 22.5, "humidity": 65, "wind_speed": 12.3, "unit": "°C"}
    """
    # 1. 城市转经纬度
    coords = geocode_city(city)
    if coords is None:
        return {"city": city, "error": "未找到该城市"}

    lat, lon = coords

    # 2. 获取天气
    weather = fetch_weather(lat, lon)

    # 3. 组装返回结果
    return {
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "weather": weather,
    }


# ---------- 启动服务 ----------
if __name__ == "__main__":
    # stdio 模式：通过标准输入输出通信，适合 Claude Desktop 等客户端[reference:2]
    mcp.run(transport="stdio")