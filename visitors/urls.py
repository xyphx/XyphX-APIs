from django.urls import path
from .views import TotalVisitorsView, PortfolioView, GetWarrantyView

urlpatterns = [
    path('', TotalVisitorsView.as_view(), name='visitors-total'),
    path('portfolio/', PortfolioView.as_view(), name='visitors-portfolio'),
    path('get-warranty/', GetWarrantyView.as_view(), name='visitors-get-warranty'),
]
