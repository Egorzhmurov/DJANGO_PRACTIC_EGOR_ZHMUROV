from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Админку отправляем по адресу 127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),

    # А твои опросы делаем главной страницей: 127.0.0.1:8000/
    path('', include('polls.urls')),
]