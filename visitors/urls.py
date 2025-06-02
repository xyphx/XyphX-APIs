from django.urls import path
from .views import TotalVisitorsView, UpdatePortfolioView, UpdateGetWarrantyView

urlpatterns = [
    path('', TotalVisitorsView.as_view(), name='visitors-total'),
    path('portfolio/', UpdatePortfolioView.as_view(), name='visitors-portfolio-update'),
    path('get-warranty/', UpdateGetWarrantyView.as_view(), name='visitors-get-warranty-update'),
]
