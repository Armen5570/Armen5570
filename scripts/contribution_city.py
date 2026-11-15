
import os
import json
import urllib.request
import urllib.error
from datetime import date, timedelta
from pathlib import Path
from html import escape

USERNAME = os.environ["GITHUB_USERNAME"]
TOKEN = os.environ["GITHUB_TOKEN"]

OUTPUT = Path("assets/contribution-city.svg")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

query = """
query($username: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $username) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""

today = date.today()
start = today - timedelta(days=364)

payload = {
    "query": query,
    "variables": {
        "username": USERNAME,
        "from": start.isoformat() + "T00:00:00Z",
        "to": today.isoformat() + "T23:59:59Z"
    }
}

request = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "Contribution-City"
    }
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode())

if "errors" in result:
    raise RuntimeError(result["errors"])

user = result["data"]["user"]
if user is None:
    raise RuntimeError(f"GitHub user not found: {USERNAME}")

weeks = user["contributionsCollection"]["contributionCalendar"]["weeks"]

days = []
for week in weeks:
    for item in week["contributionDays"]:
        days.append({
            "date": item["date"],
            "count": item["contributionCount"]
        })

max_count = max((d["count"] for d in days), default=1)

# Isometric city layout
width = 1200
height = 520
origin_x = 600
origin_y = 120

cell_w = 24
cell_h = 13
max_building_height = 115

parts = []

parts.append(f"""
<svg xmlns="http://www.w3.org/2000/svg"
     width="{width}" height="{height}"
     viewBox="0 0 {width} {height}">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#07152d"/>
    <stop offset="100%" stop-color="#142b4c"/>
  </linearGradient>
  <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#63e6ff"/>
    <stop offset="100%" stop-color="#2563eb"/>
  </linearGradient>
  <filter id="glow">
    <feGaussianBlur stdDeviation="3" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
</defs>

<rect width="100%" height="100%" rx="18" fill="url(#sky)"/>

<text x="600" y="48" text-anchor="middle"
      font-family="Arial" font-size="26"
      font-weight="bold" fill="#ffffff">
  CONTRIBUTION CITY
</text>

<text x="600" y="75" text-anchor="middle"
      font-family="Arial" font-size="13" fill="#9fb8d8">
  {escape(USERNAME)} · LAST 365 DAYS
</text>
""")

# Stars
for i in range(55):
    x = (i * 197 + 31) % width
    y = (i * 83 + 100) % 270
    parts.append(
        f'<circle cx="{x}" cy="{y}" r="1.4" fill="#b8d9ff" opacity=".65"/>'
    )

# Ground plane
parts.append("""
<path d="M600 105 L1120 365 L600 500 L80 365 Z"
      fill="#163b57" stroke="#2c6680" stroke-width="2"/>
""")

# Draw buildings in isometric rows
for index, item in enumerate(days):
    count = item["count"]
    row = index // 52
    col = index % 52

    x = origin_x + (col - row) * cell_w
    y = origin_y + (col + row) * cell_h + 30

    building_h = (
        5 + (count / max_count) * max_building_height
        if count > 0 else 3
    )

    color = (
        "#36d399" if count >= max_count * 0.65 else
        "#38bdf8" if count > 0 else
        "#24465e"
    )

    top = y - building_h

    # Building front and side
    parts.append(f"""
    <g>
      <path d="M{x} {top} l12 -6 l12 6 l-12 6 Z"
            fill="#a5f3fc" opacity=".95"/>
      <path d="M{x} {top} l12 6 v{building_h} l-12 -6 Z"
            fill="{color}"/>
      <path d="M{x+12} {top+6} l12 -6 v{building_h} l-12 6 Z"
            fill="#155e75"/>
      <path d="M{x+5} {top+12} v{max(0, building_h-15)}"
            stroke="#d1fae5" stroke-width="2" opacity=".5"/>
      <title>{item["date"]}: {count} contributions</title>
    </g>
    """)

parts.append(f"""
<text x="600" y="490" text-anchor="middle"
      font-family="Arial" font-size="13" fill="#c8d9ed">
  Total contributions: {sum(d["count"] for d in days)}
</text>
</svg>
""")

OUTPUT.write_text("\n".join(parts), encoding="utf-8")
print(f"Generated {OUTPUT}")
