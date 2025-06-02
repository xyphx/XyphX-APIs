from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from visitors.models import Visitor

class TotalVisitorsView(APIView):
    def get(self, request):
        visitor = Visitor.objects.first()
        return JsonResponse({'total': visitor.total})

class PortfolioView(APIView):
    def get(self, request):
        visitor = Visitor.objects.first()
        return JsonResponse({'portfolio': visitor.portfolio})

class GetWarrantyView(APIView):
    def get(self, request):
        visitor = Visitor.objects.first()
        return JsonResponse({'getWarranty': visitor.get_warranty})

