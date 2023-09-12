from django.urls import path
from . import  views
urlpatterns=[
    path('',views.person_list,name='list'),
    path('<int:id>/',views.person_detail)
]