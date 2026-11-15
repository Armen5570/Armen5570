
import os
import json
import urllib.request
from datetime import date, timedelta
from pathlib import Path
from html import escape

username = "Armen5570"
token = os.environ["GITHUB_TOKEN"]

today = date.today()
start = today - timedelta(days=364)

query = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        totalContributions
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

payload = {
    "query": query,
    "variables": {
        "login": username,
        "from": start.isoformat() + "T00:00:00Z",
        "to": today.isoformat() + "T23:59:59Z"
    }
}

request = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read())

if result.get("errors"):
    raise Exception(result["errors"])

calendar = result["data"]["user"]["contributionsCollection"]["contributionCalendar"]

days = [
    day
    for week in calendar["weeks"]
    for day in week["contributionDays"]
]

maximum = max(
    (day["contributionCount"] for day in days),
    default=1
) or 1

total = calendar["totalContributions"]

svg = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="560" viewBox="0 0 1200 560">',
    '<defs><linearGradient id="bg" x2="0" y2="1"><stop stop-color="#071426"/><stop offset="1" stop-color="#163b55"/></linearGradient></defs>',
    '<rect width="1200" height="560" rx="20" fill="url(#bg)"/>',
    '<text x="600" y="48" text-anchor="middle" fill="white" font-size="28" font-family="Arial" font-weight="bold">CONTRIBUTION MOUNTAINS</text>',
    f'<text x="600" y="76" text-anchor="middle" fill="#9fb8cc" font-size="14" font-family="Arial">@{escape(username)} · LAST 365 DAYS</text>'
]

# Stars
for i in range(65):
    x = (i * 173 + 31) % 1200
    y = 100 + (i * 47) % 150
    svg.append(f'<circle cx="{x}" cy="{y}" r="1.5" fill="#c5e7ff" opacity=".6"/>')

# Background mountains
svg.append(
    '<path d="M0 330 L150 190 L280 320 L450 160 L620 330 L790 175 L960 320 L1100 190 L1200 300 L1200 560 L0 560Z" fill="#1d5268"/>'
)

# Main 3D mountain range
for i, day in enumerate(days):
    col = i // 7
    row = i % 7

    x = 600 + (col - row) * 11
    y = 190 + (col + row) * 4.5

    count = day["contributionCount"]
    h = 3 + (count / maximum) ** 0.65 * 90 if count else 2

    peak = y - h

    if count == 0:
        c1, c2, snow = "#24465a", "#18384c", "#355a6b"
    elif count >= maximum * 0.65:
        c1, c2, snow = "#34d399", "#08745f", "#d1fae5"
    elif count >= maximum * 0.25:
        c1, c2, snow = "#38bdf8", "#145b7e", "#dbeafe"
    else:
        c1, c2, snow = "#60a5fa", "#23477f", "#bfdbfe"

    svg.append(f"""
    <g>
      <title>{escape(day['date'])}: {count} contributions</title>
      <path d="M{x-9} {y} L{x} {y-5} L{x} {peak} Z" fill="{c1}"/>
      <path d="M{x} {y-5} L{x+9} {y} L{x} {peak} Z" fill="{c2}"/>
      <path d="M{x} {peak} l-3 8 h6 Z" fill="{snow}"/>
    </g>
    """)

svg.append(f"""
<text x="600" y="510" text-anchor="middle"
      fill="white" font-size="21" font-family="Arial" font-weight="bold">
  {total:,} CONTRIBUTIONS
</text>
<text x="600" y="535" text-anchor="middle"
      fill="#9fb8cc" font-size="12" font-family="Arial">
  Updated automatically from GitHub
</text>
</svg>
""")

Path("assets").mkdir(exist_ok=True)
Path("assets/contribution-mountains.svg").write_text(
    "\n".join(svg),
    encoding="utf-8"
)

print("Contribution Mountains created!")
