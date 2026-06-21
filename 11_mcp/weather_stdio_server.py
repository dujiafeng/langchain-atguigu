#!/usr/bin/env python3
"""
极简天气服务端（stdio 模式）
从 stdin 读取城市名（每行一个），将天气 JSON 输出到 stdout
"""

import sys
import json
import requests

# ---------- 地理编码：城市名 -> 经纬度 ----------
def geocode(city: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json", "limit": 1}
    headers = {"User-Agent": "WeatherStdio/1.0"}
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
def fetch_weather(lat, lon, units="celsius"):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
        "temperature_unit": "celsius" if units == "celsius" else "fahrenheit",
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
            "unit": "°C" if units == "celsius" else "°F",
        }
    except Exception as e:
        return {"error": str(e)}

# ---------- 主循环：从 stdin 读取，逐行处理 ----------
def main():
    # 可以加个启动提示（输出到 stderr 不会干扰 stdout 的 JSON）
    sys.stderr.write("Weather stdio server started, waiting for city names...\n")
    sys.stderr.flush()

    for line in sys.stdin:
        city = line.strip()
        if not city:
            continue          # 跳过空行

        # 1. 转经纬度
        coords = geocode(city)
        if coords is None:
            result = {"city": city, "error": "City not found"}
        else:
            lat, lon = coords
            weather = fetch_weather(lat, lon)
            result = {
                "city": city,
                "latitude": lat,
                "longitude": lon,
                "weather": weather,
            }

        # 2. 输出 JSON 到 stdout（每行一个 JSON）
        print(json.dumps(result, ensure_ascii=False))
        sys.stdout.flush()   # 确保立即输出

if __name__ == "__main__":
    main()