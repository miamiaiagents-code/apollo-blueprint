import re

with open('/private/tmp/apollo-blueprint/index.html', 'r') as f:
    content = f.read()

agents = {
    'Apollo': ('https://i.pravatar.cc/150?img=68', '#D4A853'),
    'Fin': ('https://i.pravatar.cc/150?img=60', '#4A9EFF'),
    'Chain': ('https://i.pravatar.cc/150?img=47', '#FF6B6B'),
    'Globe': ('https://i.pravatar.cc/150?img=12', '#4ECDC4'),
    'Vault': ('https://i.pravatar.cc/150?img=44', '#FF8C42'),
    'Scout': ('https://i.pravatar.cc/150?img=24', '#A78BFA'),
    'Sage': ('https://i.pravatar.cc/150?img=25', '#34D399'),
    'Maya': ('https://i.pravatar.cc/150?img=45', '#F472B6'),
    'Kira': ('https://i.pravatar.cc/150?img=23', '#FB923C'),
    'Pixel': ('https://i.pravatar.cc/150?img=38', '#818CF8'),
    'Pulse': ('https://i.pravatar.cc/150?img=53', '#F87171'),
    'Cleo': ('https://i.pravatar.cc/150?img=9', '#38BDF8'),
    'Forge': ('https://i.pravatar.cc/150?img=59', '#FBBF24'),
    'Nexus': ('https://i.pravatar.cc/150?img=51', '#A3E635'),
}

# 1. HERO AVATARS
for name, (url, color) in agents.items():
    pattern = (r'(<div class="hero-avatar[^"]*" style=")background:'
               + re.escape(color)
               + r'(" title="' + re.escape(name) + r'">)\s*<svg[^>]*>.*?</svg>')
    replacement = (r'\1border:2px solid ' + color
                   + r'\2<img src="' + url + '" alt="' + name
                   + '" style="width:100%;height:100%;object-fit:cover;border-radius:50%">')
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# 2. ARCHITECTURE ORG CHART (skip Apollo - already has img)
for name, (url, color) in agents.items():
    if name == 'Apollo':
        continue
    pattern = (r'<div style="width:36px;height:36px;border-radius:50%;background:'
               + re.escape(color)
               + r';display:flex;align-items:center;justify-content:center;flex-shrink:0">\s*<svg[^>]*>.*?</svg>\s*</div>')
    replacement = ('<img src="' + url + '" alt="' + name
                   + '" style="width:36px;height:36px;border-radius:50%;border:2px solid ' + color
                   + ';object-fit:cover;flex-shrink:0">')
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# 3. TEAM SECTION AGENT CARDS
for name, (url, color) in agents.items():
    pattern = (r'<div class="agent-avatar" style="background:'
               + re.escape(color)
               + r'">\s*<svg[^>]*>.*?</svg>\s*</div>')
    replacement = ('<div class="agent-avatar" style="border:2px solid ' + color
                   + ';overflow:hidden"><img src="' + url + '" alt="' + name
                   + '" style="width:100%;height:100%;object-fit:cover;border-radius:50%"></div>')
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('/private/tmp/apollo-blueprint/index.html', 'w') as f:
    f.write(content)

print("Done! All SVG icons replaced with avatar images.")
