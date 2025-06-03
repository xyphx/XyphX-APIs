from django.urls import path, include

urlpatterns = [
    path('visitors/', include('visitors.urls')),
    path('test-server/', include('maintenance.urls')),
    path('apply/', include('apply.urls')),
]
