from django.shortcuts import render
from .models import BlogPost
from rest_framework import generics , status 
from .serializer import BlogPostSerializer
from rest_framework.response import Response



class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def delete(self ,  requests , *args , **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset= BlogPost.objects.all()
    serializer_class =BlogPostSerializer
    lookup_field="pk"