from django.urls import path 
#from . import views
from .views import HomePageView, PostDetailView, NewPostView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomePageView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('new_post/', NewPostView.as_view(), name= 'new-post'),
]