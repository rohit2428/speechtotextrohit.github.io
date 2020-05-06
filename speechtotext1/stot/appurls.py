from django.urls import path
from . import views
#from . views import all


urlpatterns = [

    path('',views.index),
    path('submit',views.all),

    ]
