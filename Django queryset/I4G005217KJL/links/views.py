from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView
from .models import Link
from .serializer import LinkSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework import status
import datetime

from . import models


# # Create your views here.
# class LinkListApi(ListAPIView):
#     serializer_class = LinkSerializer
#     queryset = Link.objects.filter(active=True)


# class LinkUpdateAPI(UpdateAPIView):
#     serializer_class = LinkSerializer
#     queryset = Link.objects.filter(active=True)
    
# class LinkDetailApi(RetrieveAPIView):
#     serializer_class = LinkSerializer
#     queryset = Link.objects.filter(active=True)
    
# class LinkCreateApi(CreateAPIView):
#     serializer_class = LinkSerializer
#     queryset = Link.objects.filter(active=True)
    
# class LinkDeleteView(DestroyAPIView):
#     serializer_class = LinkSerializer
#     queryset = Link.objects.filter(active=True)


class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self,request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = LinkSerializer(qs,many=True).data
        return Response(data,status=status.HTTP_200_OK)
    
    
class RecentLinkView(APIView):
    
    """
    Returns a list of recently created active links
    """
    def get(self,request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        time_preriod = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=time_preriod)
        data = LinkSerializer(qs,many=True).data
        return Response(data,status=status.HTTP_200_OK)
        
    