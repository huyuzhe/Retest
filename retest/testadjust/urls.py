
from .views import Receive_data
from django.urls import path

urlpatterns = [
    path(r'test/', Receive_data.as_view()),

]
