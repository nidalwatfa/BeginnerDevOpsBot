# استخدم صورة Python الرسمية
FROM python:3.9-slim

# ضبط مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ الملفات إلى الحاوية
COPY . /app

# تثبيت أي متطلبات إذا كانت موجودة
RUN pip install --no-cache-dir -r requirements.txt || true

# الأمر الافتراضي لتشغيل السكربت
CMD ["python", "deploy_website.py"]
