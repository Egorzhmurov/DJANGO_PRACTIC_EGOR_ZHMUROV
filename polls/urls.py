from django.urls import path
from . import views

urlpatterns = [
    # Головна сторінка зі списком
    path('', views.index, name='index'),
    # Сторінка конкретного питання (з кружечками)
    path('<int:question_id>/', views.detail, name='detail'),
    # Сторінка для обробки голосу (невидима для користувача)
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # Сторінка результатів
    path('<int:question_id>/results/', views.results, name='results'),
]