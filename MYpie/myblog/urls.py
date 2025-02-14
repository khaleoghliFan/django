#from .views import Blog
from django.urls import path
from .views import home,blog


urlpatterns = [
    path('blog/',blog ,name="blog"),
    path('home/', home, name='home'),
]