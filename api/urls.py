from django.urls import path 
from . import views 


urlpatterns =[

     path("blogposts/", views.BlogPostListCreate.as_view() , name="blogpost_view_create"),
     path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name="update"),

]