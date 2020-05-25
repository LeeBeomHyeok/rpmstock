from django.urls import path
from . import views


urlpatterns = [
    path('', views.showDB, name='confirmstock'),
]
