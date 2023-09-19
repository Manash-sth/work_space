from django.urls import path
from .views import *

urlpatterns = [
    path('', TestApi.as_view(), name='test_api')
]