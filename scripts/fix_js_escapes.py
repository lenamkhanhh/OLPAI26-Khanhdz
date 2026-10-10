# -*- coding: utf-8 -*-
import os
import sys

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"

def fix():
    script_path = os.path.join(ROOT_DIR, "docs", "generate_full_hub.py")
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Sửa s.split('\n') thành s.split(String.fromCharCode(10))
    content = content.replace("const lines = s.split('\\n');", "const lines = s.split(String.fromCharCode(10));")
    content = content.replace("const lines = s.split('\n');", "const lines = s.split(String.fromCharCode(10));")

    # 2. Sửa regex split sections
    content = content.replace("const sections = expText.split(/(?=###\\s+\\d+\\.)/);", "const sections = expText.split(/(?=###\\\\s+\\\\d+\\\\.)/);")

    # 3. Sửa ta.value + '\\n\\n'
    content = content.replace("ta.value + '\\n\\n'", "ta.value + '\\\\n\\\\n'")

    with open(script_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed generate_full_hub.py")

if __name__ == "__main__":
    fix()
