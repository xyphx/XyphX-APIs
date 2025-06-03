from django.urls import path, include
from maintenance.views import test_server

urlpatterns = [
    path('visitors/', include('visitors.urls')),
    path('test-server/', test_server, name='test-server'),
    path('apply/', include('apply.urls')),
]
