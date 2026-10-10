# -*- coding: utf-8 -*-
"""
Vercel Serverless Function entrypoint for Olympic AI Study Hub Backend.
Exposes FastAPI ASGI app to Vercel Python runtime.
"""

import sys
from pathlib import Path

# Add project root to sys.path for backend imports
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from backend.main import app

# Export for Vercel ASGI
handler = app
