#!/bin/bash
# BeginnerDevOpsBot - Termux Setup Script

echo "🔧 تثبيت المتطلبات على Termux..."
pkg update -y && pkg upgrade -y
pkg install python git -y

echo "📥 استنساخ المشروع..."
git clone https://github.com/nidalwatfa/BeginnerDevOpsBot.git
cd BeginnerDevOpsBot || exit

echo "🚀 تشغيل النشر..."
python deploy_website.py

echo "✅ تم النشر في: /tmp/deploy_output"
echo "افتح الملف: /tmp/deploy_output/index.html"
echo "استخدم 'termux-open' لفتح المتصفح"
