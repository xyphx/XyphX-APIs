from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .models import Apply
from .serializers import ApplySerializer

class ApplyView(APIView):
    def post(self, request):
        serializer = ApplySerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            context = serializer.data

            # 1. Send notification email to internal team
            application_template = get_template("apply_email.jinja")
            application_html_content = application_template.render(context)

            subject = "XyphX - New Application Received"
            from_email = "xyphx.company@gmail.com"
            to_emails = ["sidharthpunalur@gmail.com", "gayathry.rs22@gmail.com", "surajpmnr@gmail.com"]

            email = EmailMultiAlternatives(subject, "", from_email, to_emails)
            email.attach_alternative(application_html_content, "text/html")
            try:
                email.send()
            except Exception as e:
                print("Internal notification email sending failed:", e)

            # 2. Send feedback email to the applicant
            feedback_template = get_template("feedback_email.jinja")
            feedback_html_content = feedback_template.render(context)

            feedback_subject = "XyphX - Thank you for your application"
            applicant_email = instance.email

            feedback_email = EmailMultiAlternatives(feedback_subject, "", from_email, [applicant_email])
            feedback_email.attach_alternative(feedback_html_content, "text/html")
            try:
                feedback_email.send()
            except Exception as e:
                print("Feedback email sending failed:", e)

            return Response({"message": "Application submitted successfully."}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
