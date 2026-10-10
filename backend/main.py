# -*- coding: utf-8 -*-
"""
Main FastAPI Application for Olympic AI Study Hub & Arena Platform.
Data-Agnostic, Production-Ready, Self-Hosted E2E Engine.
"""

from contextlib import asynccontextmanager
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse

from backend.config import PUBLIC_DIR, PORT, HOST
from backend.seed import seed_database
from backend.routers import auth_routes, exam_routes, submission_routes, leaderboard_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Seed and sync database
    seed_database()
    yield
    # Shutdown logic if any

app = FastAPI(
    title="Olympic AI HCMUS — Academic Arena API",
    description="Data-Agnostic Competitive AI & Knowledge Evaluation Platform with Automated Grading and Leaderboards.",
    version="2.0.0",
    lifespan=lifespan
)

# Enable CORS for local development and web hosting
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth_routes.router)
app.include_router(exam_routes.router)
app.include_router(submission_routes.router)
app.include_router(leaderboard_routes.router)

# Healthcheck
@app.get("/api/health", tags=["System"])
def healthcheck():
    return {
        "status": "healthy",
        "service": "Olympic AI Study Hub API",
        "version": "2.0.0"
    }

# Serve Frontend Root & Direct HTML
@app.get("/", include_in_schema=False)
def root_index():
    study_hub_file = PUBLIC_DIR / "olympic_ai_study_hub.html"
    if study_hub_file.exists():
        return FileResponse(str(study_hub_file), media_type="text/html")
    return RedirectResponse(url="/docs")

@app.get("/olympic_ai_study_hub.html", include_in_schema=False)
def study_hub_html():
    study_hub_file = PUBLIC_DIR / "olympic_ai_study_hub.html"
    if study_hub_file.exists():
        return FileResponse(str(study_hub_file), media_type="text/html")
    return RedirectResponse(url="/")

# Mount Public Assets if directory exists
if PUBLIC_DIR.exists():
    app.mount("/public", StaticFiles(directory=str(PUBLIC_DIR)), name="public")
    app.mount("/assets", StaticFiles(directory=str(PUBLIC_DIR)), name="assets")
    # Mount directly at root fallback for relative assets (katex, fonts, pdf)
    app.mount("/", StaticFiles(directory=str(PUBLIC_DIR), html=True), name="static_root")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host=HOST, port=PORT, reload=True)
