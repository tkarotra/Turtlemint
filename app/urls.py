from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('get-data-ajax', getDataAjax, name='get-data-ajax'),
    path('get-policy/<int:pk>/', getPolicy, name='get-policy'),
    path('change-model', changeModel, name='change-model'),
]