from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import views
from rest_framework.status import *
from .models import *
from .serializers import *

# Create your views here.

    
class NoticeDetailView:
    def put(self, request, pk, format=None):
        post = get_object_or_404(Notice, pk=pk)
        serializer = NoticeSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'TF 공지 수정 성공', 'data': serializer.data}, status = HTTP_200_OK)
        return Response({'message': 'TF 공지 수정 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)