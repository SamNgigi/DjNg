# from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Txt

from .serializers import TxtSerializer


# Create your views here.
class TxtList(ListCreateAPIView):

    queryset = Txt.objects.all()
    serializer_class = TxtSerializer


class TxtDetail(RetrieveUpdateDestroyAPIView):

    queryset = Txt.objects.all()
    serializer_class = TxtSerializer
