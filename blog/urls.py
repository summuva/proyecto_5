
from django.urls import path
from .views import BlogListView
# Register your models here.
app_name = 'blog'

urlpatterns = [

    path('', BlogListView.as_view(), name='home' )
]