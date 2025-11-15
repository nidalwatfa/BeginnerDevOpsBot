#!/data/data/com.termux/files/usr/bin/bash

echo "🔧 بدء إعداد بيئة Termux..."

# تحديث الحزم
pkg update -y && pkg upgrade -y

# تثبيت الأدوات الأساسية
pkg install -y git python docker

# التحقق من الإصدارات
echo "✅ التحقق من الإصدارات:"
python --version
git --version
docker --version

# رسالة نجاح
echo "🎉 تم إعداد البيئة بنجاح! يمكنك الآن تشغيل المشروع."
