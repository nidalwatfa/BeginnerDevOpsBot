#!/usr/bin/env python3
"""
Beginner Automation Bot - Step 1: Deploy a Static Website
"""

import os
import shutil
from datetime import datetime

# Configuration
SOURCE_DIR = "website"          # Folder containing your HTML/CSS/JS
DEPLOY_DIR = "/tmp/deploy_output"  # Temporary deployment folder
INDEX_FILE = "index.html"

def create_sample_website():
    os.makedirs(SOURCE_DIR, exist_ok=True)
    
    html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>موقعي الأول - أتمتة DevOps</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background: #f0f8ff; }
        h1 { color: #2c3e50; }
        .btn { padding: 10px 20px; background: #27ae60; color: white; text-decoration: none; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>مرحباً! تم النشر بنجاح عبر الأتمتة</h1>
    <p>الوقت: {}</p>
    <a href="#" class="btn">ابدأ الآن</a>
</body>
</html>""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    with open(os.path.join(SOURCE_DIR, INDEX_FILE), "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"تم إنشاء موقع ويب عينة في مجلد: {SOURCE_DIR}")

def deploy():
    if not os.path.exists(SOURCE_DIR):
        print("خطأ: مجلد الموقع غير موجود!")
        return
    
    os.makedirs(DEPLOY_DIR, exist_ok=True)
    shutil.rmtree(DEPLOY_DIR)  # Clean previous deploy
    shutil.copytree(SOURCE_DIR, DEPLOY_DIR, dirs_exist_ok=True)
    
    print(f"تم النشر بنجاح إلى: {DEPLOY_DIR}")
    print(f"افتح الملف: {os.path.join(DEPLOY_DIR, INDEX_FILE)}")

if __name__ == "__main__":
    create_sample_website()
    deploy()
