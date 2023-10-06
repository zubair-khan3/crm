from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('record/<int:pk>', views.single_record, name='single_record')
]
