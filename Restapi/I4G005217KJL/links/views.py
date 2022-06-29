from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView
from .models import Link
from .serializer import LinkSerializer

# Create your views here.
class LinkListApi(ListAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.filter(active=True)


class LinkUpdateAPI(UpdateAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.filter(active=True)
    
class LinkDetailApi(RetrieveAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.filter(active=True)
    
class LinkCreateApi(CreateAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.filter(active=True)
    
class LinkDeleteView(DestroyAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.filter(active=True)

    