# -*- coding: utf-8 -*-
import urllib.request
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

all_24 = [
    ("§1.1", "HVXime0nQeI"),
    ("§1.2", "_PwhiWxHK8o"),
    ("§1.3", "7VeUPuFGJHk"),
    ("§1.4", "J4Wdy0Wc_xQ"),
    ("§1.5", "fSytzGwwBVw"),
    ("§1.6", "NGf0voTMlcs"),
    ("§1.7", "4jRBRDbJemM"),
    ("§1.8", "4b5d3muPQmA"),
    ("§1.9", "U3X98xZ4_no"),
    ("§2.2", "aircAruvnKk"),
    ("§2.3", "Ilg3gGewQ5U"),
    ("§2.4", "6ArSys5qHAU"),
    ("§2.5", "nhqo0u1a6fw"),
    ("§2.7", "s2coXdufOzE"),
    ("§2.8", "YFwyHcJ8je8"),
    ("§3.1", "bNb2fEVKeEo"),
    ("§3.3", "GWt6Fu05voI"),
    ("§3.4", "oLvmLJkmXuc"),
    ("§3.5", "TrdevFK_am4"),
    ("§3.6", "9s_FpMpdYW8"),
    ("§4.3", "gQddtTdmG_8"),
    ("§4.5", "eMlx5fFNoYc"),
    ("§5.1", "HZGCoVF3YvM"),
    ("§5.2", "zeJD6dqJ5lo"),
]

print(f"Testing all {len(all_24)} videos...")
failed = []
for sec, ytid in all_24:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={ytid}&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=4) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"✓ {sec}: {ytid:11s} | {data.get('title')[:60]}")
    except Exception as e:
        print(f"❌ {sec}: {ytid:11s} | {e}")
        failed.append((sec, ytid, str(e)))

print(f"\nResult: {len(all_24) - len(failed)}/{len(all_24)} ALIVE. Failed: {len(failed)}")
if failed:
    sys.exit(1)
