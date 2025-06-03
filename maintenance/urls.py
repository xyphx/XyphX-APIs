from django.urls import path
from .views import TestServerView

urlpatterns = [
    path('', TestServerView.as_view(), name='test-server')
]
