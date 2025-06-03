from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from jinja2 import Template
from .models import Apply
from .serializers import ApplySerializer

class ApplyView(APIView):
    def post(self, request):
        serializer = ApplySerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            context = serializer.data

            # Load and render Jinja2 template
            template = get_template("apply_email.jinja")
            html_content = template.render(context)

            subject = "New Application Received"
            from_email = "xyphx.company@gmail.com"
            to_emails = ["sidhartpunalur@gmail.com", "gayathry.rs22@gmail.com"]

            email = EmailMultiAlternatives(subject, "", from_email, to_emails)
            email.attach_alternative(html_content, "text/html")
            email.send()

            return Response({"message": "Application submitted successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
