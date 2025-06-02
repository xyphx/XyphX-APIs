from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from visitors.models import Visitor

def update_total_visitors(visitor):
    visitor.total = visitor.portfolio + visitor.get_warranty  # Add more fields if needed
    visitor.save()

class TotalVisitorsView(APIView):
    def get(self, request):
        visitor = Visitor.objects.first()
        data = {
            'total': visitor.total,
            'portfolio': visitor.portfolio,
            'get_warranty': visitor.get_warranty,
        }
        return JsonResponse(data, status=200)

class UpdatePortfolioView(APIView):
    def put(self, request):
        visitor = Visitor.objects.first()
        visitor.portfolio += 1
        visitor.save()
        update_total_visitors(visitor)
        return JsonResponse({'message': 'portfolio visitors updated successfully'}, status=200)

    
class UpdateGetWarrantyView(APIView):
    def put(self, request):
        visitor = Visitor.objects.first()
        visitor.get_warranty += 1
        visitor.save()
        update_total_visitors(visitor)
        return JsonResponse({'message': 'getWarranty visitors updated successfully'}, status=200)

