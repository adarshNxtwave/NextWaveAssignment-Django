from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('v1',views.query1,name ='view1'),
    path('v2',views.query2,name ='view2'),
    path('v3',views.query3,name ='view3'),
    path('add',views.add,name ='view4'),
]