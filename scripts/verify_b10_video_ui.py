# -*- coding: utf-8 -*-
import sys
import json
import time
import subprocess
import urllib.request
import base64
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
URL = "http://localhost:8080/olympic_ai_study_hub.html"
PORT = 9224

def main():
    print("=== KIỂM TRA VIDEO TAB & PROBLEM OLP01-B10 ===")
    cmd = [
        CHROME_PATH,
        "--headless=new",
        f"--remote-debugging-port={PORT}",
        "--disable-gpu",
        "--no-sandbox",
        "--window-size=1600,1000",
        "--remote-allow-origins=*",
        URL
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2.5)

    try:
        import websocket
        version_url = f"http://127.0.0.1:{PORT}/json"
        req = urllib.request.urlopen(version_url, timeout=5)
        tabs = json.loads(req.read().decode('utf-8'))
        target_tab = None
        for t in tabs:
            if "olympic_ai_study_hub" in t.get("url", ""):
                target_tab = t
                break
        if not target_tab and len(tabs) > 0:
            target_tab = tabs[0]
            
        print(f"Connected tab: {target_tab.get('title')} ({target_tab.get('url')})")
        ws_url = target_tab.get("webSocketDebuggerUrl")
        ws = websocket.create_connection(ws_url, timeout=15, suppress_origin=True)

        msg_id = 1
        def evaluate(expr):
            nonlocal msg_id
            payload = {
                "id": msg_id,
                "method": "Runtime.evaluate",
                "params": {"expression": expr, "returnByValue": True}
            }
            msg_id += 1
            ws.send(json.dumps(payload))
            while True:
                res = json.loads(ws.recv())
                if res.get("id") == payload["id"]:
                    result = res.get("result", {}).get("result", {})
                    return result.get("value")

        def send_cmd(method, params=None):
            nonlocal msg_id
            payload = {"id": msg_id, "method": method, "params": params or {}}
            msg_id += 1
            ws.send(json.dumps(payload))
            while True:
                res = json.loads(ws.recv())
                if res.get("id") == payload["id"]:
                    return res.get("result", {})

        send_cmd("Page.enable")

        def capture_screenshot(filename):
            res = send_cmd("Page.captureScreenshot", {"format": "png"})
            img_data = base64.b64decode(res.get("data", ""))
            with open(filename, "wb") as f:
                f.write(img_data)
            print(f"Đã lưu ảnh chụp: {filename}")

        # Wait for page ready
        for _ in range(20):
            if evaluate("typeof ALL_EXAMS !== 'undefined'"):
                break
            time.sleep(0.5)

        # 1. Chuyển sang câu OLP01-B10
        # Tìm index của câu có id 'OLP01-B10'
        b10_idx = evaluate("""
            (function() {
                const ex = ALL_EXAMS[currentExamId];
                if (!ex) return -1;
                return ex.questions.findIndex(q => q.id === 'OLP01-B10');
            })()
        """)
        print(f"Index câu OLP01-B10: {b10_idx}")
        if b10_idx is not None and b10_idx >= 0:
            evaluate(f"jumpToQuestion({b10_idx})")
            time.sleep(0.5)

        # Mở Inspector nếu chưa mở
        evaluate("if (!isInspectorOpen) toggleInspector()")
        time.sleep(0.3)

        # Chuyển Inspector sang tab video (BÀI GIẢNG)
        evaluate("switchInspectorTab('video')")
        time.sleep(0.5)

        # Đọc thông tin video card hiện tại
        vid_title = evaluate("document.querySelector('.video-card-cp div[style*=\"font-size:12.5px\"]') ? document.querySelector('.video-card-cp div[style*=\"font-size:12.5px\"]').innerText : ''")
        vid_channel = evaluate("document.querySelector('.video-card-cp span strong') ? document.querySelector('.video-card-cp span strong').innerText : ''")
        yt_link = evaluate("document.querySelector('.video-card-cp a[title*=\"YouTube\"]') ? document.querySelector('.video-card-cp a[title*=\"YouTube\"]').href : ''")
        print(f"\nThông tin video hiện tại:")
        print(f"  Tiêu đề: {vid_title}")
        print(f"  Kênh: {vid_channel}")
        print(f"  Link YouTube: {yt_link}")

        # Click phát video inline
        evaluate("document.getElementById('btnPlayInline').click()")
        time.sleep(1.0)

        # Kiểm tra iframe embed src
        iframe_src = evaluate("document.querySelector('iframe.video-iframe-embed') ? document.querySelector('iframe.video-iframe-embed').src : ''")
        print(f"  Iframe embed src: {iframe_src}")

        # Chụp ảnh màn hình
        artifact_dir = r"C:\Users\HP\.gemini\antigravity-ide\brain\aa690221-10c6-463c-b522-a5a5cf66e453"
        out_img = os.path.join(artifact_dir, "b10_video_verified.png")
        capture_screenshot(out_img)

        # Kiểm tra điều kiện pass
        assert "YFwyHcJ8je8" in iframe_src or "YFwyHcJ8je8" in yt_link, "Lỗi: Video ID không phải là YFwyHcJ8je8!"
        print("\n✓ XÁC NHẬN THÀNH CÔNG: Video YFwyHcJ8je8 đã được nhúng và nạp chuẩn xác!")

    finally:
        proc.terminate()
        proc.wait()

if __name__ == "__main__":
    main()
