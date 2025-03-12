from django.shortcuts import render
from rest_framework.views import APIView
from .models import main
from backend_api.serializer import mainSerializer
from rest_framework.response import Response

class mainView(APIView):
    def get(self, request):
        output = [
            {
                "title": output.title,
                "description": output.description
            } for output in main.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = mainSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
