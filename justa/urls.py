from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='inicio'),
    path('login-modal/', views.login_modal, name='login_modal'),
    path('register-modal/', views.register_modal, name='register_modal'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('blogs/', views.blogs, name='blogs'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('politicas/', views.politicas, name='politicas'),
]

# Sirve los archivos multimedia en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)