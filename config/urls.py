

from django.contrib import admin
from django.urls import path, include
from queueapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('book/<int:service_id>/', views.book_token, name='book_token'),
    path('accounts/', include('django.contrib.auth.urls')),
]
