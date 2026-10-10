@echo off
chcp 65001 > nul
title Olympic AI Study Hub & Arena - Full Stack System
color 0A

echo ======================================================================
echo   OLYMPIC AI STUDY HUB & ARENA — HỆ THỐNG LUYỆN THI TOÀN DIỆN 2026
echo   FastAPI Backend + SQLite + Automated Grading + YouTube Lecture Hub
echo ======================================================================
echo.

cd /d "%~dp0"

echo [1/3] Kiểm tra & Cấu hình máy chủ Backend (Cổng 8080)...
REM Tắt tiến trình cũ nếu không phải là FastAPI
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8080" ^| findstr "LISTENING"') do (
    taskkill /PID %%a /F > nul 2>&1
)

echo [2/3] Khởi động Olympic AI Backend Server (FastAPI + SQLite)...
start "Olympic AI Backend [Port 8080]" /min python -m uvicorn backend.main:app --host 127.0.0.1 --port 8080
timeout /t 3 /nobreak > nul

echo [3/3] Đang mở giao diện Study Hub trên trình duyệt Chrome/Default...
start "" "http://localhost:8080/olympic_ai_study_hub.html"

echo.
echo ======================================================================
echo   HỆ THỐNG ĐÃ SẴN SÀNG HOẠT ĐỘNG!
echo   - Web App Study Hub: http://localhost:8080/olympic_ai_study_hub.html
echo   - REST API & Swagger: http://localhost:8080/docs
echo   - Tài khoản mẫu thí sinh:  student / hcmus2026
echo   - Tài khoản quản trị viên: admin   / hcmus2026
echo ======================================================================
echo.
timeout /t 5 > nul
exit
