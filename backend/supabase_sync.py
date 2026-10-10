"""
Hệ thống đồng bộ dữ liệu đám mây Supabase cho Olympic AI HCMUS 2026.
Tự động kích hoạt khi có kết nối mạng hoặc biến môi trường SUPABASE_URL / SUPABASE_KEY.
Sử dụng chuẩn REST API của Supabase (không cần cài thêm thư viện nặng).
"""

import os
import json
import urllib.request
import urllib.error
from typing import Dict, Any, Optional, List

# Cấu hình dự án Supabase olpai26
DEFAULT_SUPABASE_URL = "https://ahlpdhpxghnctgqbmqrf.supabase.co"
DEFAULT_SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFobHBkaHB4Z2huY3RncWJtcXJmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE2NDQ5MzYsImV4cCI6MjEwNzIyMDkzNn0.Z1uxUCxExjX2Imwy148q4mjrWtjzgBiVvPVv3b93030"

SUPABASE_URL = os.environ.get("SUPABASE_URL", DEFAULT_SUPABASE_URL)
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY", os.environ.get("SUPABASE_KEY", DEFAULT_SUPABASE_KEY))


def _make_request(endpoint: str, method: str = "GET", data: Optional[Dict[str, Any]] = None) -> Optional[Any]:
    """Gửi request tới Supabase REST PostgREST API."""
    url = f"{SUPABASE_URL.rstrip('/')}/rest/v1/{endpoint.lstrip('/')}"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

    body = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            res_body = response.read().decode("utf-8")
            if res_body:
                return json.loads(res_body)
            return []
    except Exception as e:
        # Ghi log nhẹ nhàng và bỏ qua để không ảnh hưởng luồng chính nếu offline
        print(f"[Supabase Sync] Warning/Offline: {e}")
        return None


def sync_submission_to_supabase(sub: Dict[str, Any]) -> bool:
    """Đồng bộ bài nộp của thí sinh lên Supabase Cloud."""
    payload = {
        "username": sub.get("username", "anonymous"),
        "display_name": sub.get("display_name", "Thí sinh"),
        "team_name": sub.get("team_name", ""),
        "exam_id": sub.get("exam_id", ""),
        "score": float(sub.get("score", 0.0)),
        "max_score": float(sub.get("max_score", 100.0)),
        "accuracy_percentage": float(sub.get("accuracy_percentage", 0.0)),
        "correct_count": int(sub.get("correct_count", 0)),
        "total_questions": int(sub.get("total_questions", 0)),
        "time_spent_seconds": int(sub.get("time_spent_seconds", 0)),
        "answers": sub.get("answers", {})
    }
    res = _make_request("submissions", method="POST", data=payload)
    return res is not None


def fetch_cloud_leaderboard(limit: int = 20) -> List[Dict[str, Any]]:
    """Lấy bảng xếp hạng toàn cầu từ Supabase Cloud."""
    res = _make_request(f"submissions?select=id,username,display_name,team_name,exam_id,score,max_score,accuracy_percentage,submitted_at&order=score.desc&limit={limit}")
    return res if isinstance(res, list) else []
