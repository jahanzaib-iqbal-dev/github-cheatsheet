import json
import re
from datetime import date

with open('progress.txt') as f:
    day = int(f.read().strip()) + 1

if day > 365:
    print("All 365 tips published!")
    exit(0)

with open('tips.json') as f:
    tips = json.load(f)

tip = next(t for t in tips if t['day'] == day)

tip_block = (
    f"### Day {tip['day']} — {tip['title']}\n"
    f"`{tip['category']}` · {date.today().isoformat()}\n\n"
    f"```bash\n{tip['command']}\n```\n\n"
    f"> {tip['desc']}\n\n"
    f"---\n"
)

with open('README.md') as f:
    content = f.read()

content = content.replace('<!-- TIPS_START -->\n', f'<!-- TIPS_START -->\n{tip_block}')
content = re.sub(r'tips-\d+%20%2F%20365', f'tips-{day}%20%2F%20365', content)

with open('README.md', 'w') as f:
    f.write(content)

with open('progress.txt', 'w') as f:
    f.write(str(day))

print(f"Added Day {day}: {tip['title']}")
