#from .views import Blog
from django.urls import path
from .views import home,blog,home_detail,book,book_detail,Create


urlpatterns = [
    path('blog/',blog ,name="blog"),
    path('home/', home, name='home'),
    path('detail/<int:pk>/',home_detail,name="detail"),
    path('book/', book, name='book'),
    path('book/<slug:slug>/',book_detail,name='book_detail'),
    path('create/',Create.as_view(),name='create')


]
