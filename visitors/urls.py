from django.urls import path
from .views import VisitorsView, PortfolioView

urlpatterns = [
    path('', VisitorsView.as_view(), name='visitors-home'),
    path('portfolio/', PortfolioView.as_view(), name='visitors-portfolio'),
]
