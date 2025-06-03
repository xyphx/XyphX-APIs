from django.http import JsonResponse
from rest_framework.views import APIView

class TestServerView(APIView):
    def get(request):
        return JsonResponse({'message': 'Server is running!'})
