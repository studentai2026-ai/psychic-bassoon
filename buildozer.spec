[app]

# اسم التطبيق (يظهر تحت الأيقونة)
title = المساعد الدراسي

# اسم الحزمة (يجب أن يكون حروف إنجليزية صغيرة بدون مسافات)
package.name = studentai
package.domain = org.studentai

# الملف الأساسي
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# الإصدار
version = 1.0.0

# المكتبات المطلوبة
requirements = python3,kivy,requests,urllib3,charset-normalizer,idna,certifi

# الصلاحيات
android.permissions = INTERNET

# الاتجاه
orientation = portrait

# ملء الشاشة
fullscreen = 1

# إخفاء شريط الحالة
android.hide_titlebar = 0

# الحد الأدنى لإصدار Android
android.minapi = 21

# إصدار Android المستهدف
android.api = 33

# منع الضغط
android.accept_sdk_license = True

# المعماريات (arm64 للأجهزة الحديثة، armeabi للأجهزة القديمة)
android.archs = arm64-v8a, armeabi-v7a

# عنوان الإصدار
android.versionCode = 1

# ألوان
android.presplash_color = #0F172A