# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Txt

from .serializers import TxtSerializer


# Create your views here.
class TxtViewSet(viewsets.ModelViewSet):
    """
    We have to have all these three for the ModelViewSet to work.
    And remember to migrate for the api to work.
    """
    queryset = Txt.objects.all()
    permission_classes = [permissions.AllowAny,]
    serializer_class = TxtSerializer