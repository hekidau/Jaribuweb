from django.urls import path
from . import views
#from myorder.views import firsthello

urlpatterns = [
    path('update_profile_picture/', views.update_profile_picture),
    #path('myorder/index/', firsthello,name='firsthello'),
]