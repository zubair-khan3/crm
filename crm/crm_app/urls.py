from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('single_record/<int:pk>', views.single_record, name='single_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('user_profile/<int:pk>', views.user_profile, name='user_profile'),
    path('confirm_delete/<int:pk>',views.confirm_delete,name='confirm_delete'),
    path('add_record',views.add_record,name="add_record"),
    path('update_record/<int:pk>',views.update_record,name='update_record')
]
