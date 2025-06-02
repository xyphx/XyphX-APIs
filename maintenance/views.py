from django.http import JsonResponse

def test_server(request):
    return JsonResponse({'message': 'Server is running!'})
