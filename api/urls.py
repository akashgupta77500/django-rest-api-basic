from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('data1', views.data1, name='data1'),
    path('data/<int:pk>', views.data, name='data'),
    path('create_data', views.create_data, name='create_data'),
    path('update_data', views.update_data, name='update_data'),
    path('delete', views.delete, name='delete'),

]