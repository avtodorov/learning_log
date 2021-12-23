from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    #  Уставные аутентификации
    path('', include('django.contrib.auth.urls')),
    #  Страничка регистрации
    path('register/', views.register, name='register')
]