
import os
import json
import urllib.request
from datetime import date, timedelta, datetime, time, timezone
from pathlib import Path
from html import escape

USERNAME = "Armen5570"
TOKEN = os.environ["GITHUB_TOKEN"]

OUTPUT = Path("assets/contribution-mountains.svg")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

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

today = date.today()
start = today - timedelta(days=364)

payload = {
    "query": query,
    "variables": {
        "login": USERNAME,
        "from": datetime.combine(
            start, time.min, tzinfo=timezone.utc
        ).isoformat(),
        "to": datetime.combine(
            today, time.max, tzinfo=timezone.utc
        ).isoformat()
    }
}

request = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "Contribution-Mountains"
    }
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode())

if result.get("errors"):
    raise RuntimeError(result["errors"])

user = result["data"]["user"]

if user is None:
    raise RuntimeError("GitHub user not found")

calendar = user["contributionsCollection"]["contributionCalendar"]

days = [
    day
    for week in calendar["weeks"]
    for day in week["contributionDays"]
]

total = calendar["totalContributions"]
maximum = max(
    (day["contributionCount"] for day in days),
    default=1
) or 1

parts = []

parts.append("""
<svg xmlns="http://www.w3.org/2000/svg"
     width="1200" height="560"
     viewBox="0 0 1200 560">

<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#071426"/>
    <stop offset="100%" stop-color="#102d43"/>
  </linearGradient>
</defs>

<rect width="1200" height="560" rx="20" fill="url(#sky)"/>

<text x="600" y="43"
      text-anchor="middle"
      fill="#ffffff"
      font-family="Arial"
      font-size="27"
      font-weight="bold">
  CONTRIBUTION MOUNTAINS
</text>
""")

# Stars
for i in range(60):
    x = (i * 173 + 47) % 1200
    y = 85 + ((i * 61 + 23) % 130)

    parts.append(
        f'<circle cx="{x}" cy="{y}" r="1.5" fill="#b9d9ef" opacity=".5"/>'
    )

# Background mountains
parts.append("""
<path d="M0 300 L150 180 L280 290 L430 150
L580 300 L730 170 L880 300 L1040 160
L1200 300 L1200 560 L0 560Z"
fill="#183e55" opacity=".5"/>
""")

# Contribution mountains
for index, item in enumerate(days):

    col = index // 7
    row = index % 7

    x = 600 + (col - row) * 11
    y = 190 + (col + row) * 4.5

    count = item["contributionCount"]

    height = (
        4 + (count / maximum) ** 0.65 * 90
        if count > 0 else 2
    )

    peak_y = y - height

    if count == 0:
        left = "#24465a"
        right = "#1b394e"
        snow = "#355a6b"
    elif count >= maximum * 0.65:
        left = "#34d399"
        right = "#08745f"
        snow = "#d1fae5"
    elif count >= maximum * 0.25:
        left = "#38bdf8"
        right = "#145b7e"
        snow = "#dbeafe"
    else:
        left = "#60a5fa"
        right = "#23477f"
        snow = "#bfdbfe"

    parts.append(f"""
    <g>
      <title>{escape(item["date"])}: {count} contributions</title>

      <path d="M{x-9} {y}
               L{x} {y-5}
               L{x} {peak_y}
               Z"
            fill="{left}"/>

      <path d="M{x} {y-5}
               L{x+9} {y}
               L{x} {peak_y}
               Z"
            fill="{right}"/>

      <path d="M{x} {peak_y}
               l-3 8
               l6 0 Z"
            fill="{snow}"/>
    </g>
    """)

parts.append(f"""
<text x="600" y="510"
      text-anchor="middle"
      fill="#ffffff"
      font-family="Arial"
      font-size="20"
      font-weight="bold">
  {total:,} CONTRIBUTIONS
</text>

<text x="600" y="535"
      text-anchor="middle"
      fill="#9fb8cc"
      font-family="Arial"
      font-size="12">
  @{USERNAME} · LAST 365 DAYS
</text>

</svg>
""")

OUTPUT.write_text("\n".join(parts), encoding="utf-8")

print("Contribution Mountains generated successfully!")
