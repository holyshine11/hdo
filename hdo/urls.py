from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oil.urls')),  # 앱의 URL 패턴 포함
]