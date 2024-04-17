from django.urls import path
from . import views
#from myorder.views import firsthello

urlpatterns = [
    path('index/', views.my_hello),
    #path('myorder/index/', firsthello,name='firsthello'),
]