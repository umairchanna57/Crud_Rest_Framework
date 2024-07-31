from rest_framework import serializers
from .models import BlogPost 


# creating model Here


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id' , 'title' , 'content', 'published']

        def __str__(self):
            return self.title
            
