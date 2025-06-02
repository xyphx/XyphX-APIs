from rest_framework.views import APIView
from rest_framework.response import Response

class VisitorsView(APIView):
    def get(self, request):
        return Response({"message": "Visitors Home"})

class PortfolioView(APIView):
    def get(self, request):
        return Response({"message": "Visitors Portfolio"})

