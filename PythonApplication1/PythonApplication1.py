import pandas as pd
from pathlib import Path

players = pd.read_csv("players.csv")
teams = pd.read_csv("teams.csv")

site = Path("site")
site.mkdir(exist_ok=True)

goal_lookup = dict(zip(teams["team"], teams["goals"]))

leaderboard = []

for _, row in players.iterrows():
    player_teams = [row["team1"], row["team2"], row["team3"], row["team4"]]
    total = sum(goal_lookup[team] for team in player_teams)

    leaderboard.append({
        "player": row["player"],
        "teams": player_teams,
        "score": total
    })

leaderboard.sort(key=lambda x: x["score"], reverse=True)

html = """
<html>
<head>
    <title>World Cup 2026 Sweeps</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<h1>⚽ WORLD CUP 2026 SWEEPSTAKES HQ ⚽</h1>

<marquee> WOW! </marquee>

<table>
<tr>
    <th>Rank</th>
    <th>Player</th>
    <th>Teams</th>
    <th>Total Points</th>
</tr>
"""

for i, entry in enumerate(leaderboard, start=1):
    html += f"""
<tr>
    <td>{i}</td>
    <td>{entry["player"]}</td>
    <td>{", ".join(entry["teams"])}</td>
    <td>{entry["score"]}</td>
</tr>
"""

html += """
</table>
</body>
</html>
"""

(site / "index.html").write_text(html, encoding="utf-8")

css = """
body {
    background: navy;
    color: yellow;
    font-family: "Comic Sans MS", Arial;
}

h1 {
    text-align: center;
    color: lime;
    text-shadow: 2px 2px red;
}

marquee {
    color: white;
    background: red;
    font-size: 24px;
    margin-bottom: 20px;
}

table {
    width: 90%;
    margin: auto;
    border: 5px ridge hotpink;
    background: black;
}

th {
    background: red;
    color: white;
    padding: 10px;
}

td {
    border: 1px solid lime;
    padding: 8px;
    text-align: center;
}
"""

(site / "style.css").write_text(css, encoding="utf-8")

print("Website generated! Open site/index.html")
