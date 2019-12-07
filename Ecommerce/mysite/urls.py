from django.urls import path
from .views import index, edit , create , delete , update ,add_product

urlpatterns=[

    path('' , index , name='index'),
    path('create/', create ,name ='create'),
    path('add_product/', add_product ,name ='add_product'),
    path('edit/<id>/', edit ,name ='edit'),
    path('delete/<id>/', delete ,name ='delete'),
    path('update/<id>/',update  ,name ='update')
    
]