from django.contrib import admin
from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('',views.home),
    path('services/csignup',views.csignup),
    path('services/psignup',views.psignup),
    path('services/msignup',views.msignup),
    path('services/dsignup',views.dsignup),
    path('services/clist',views.Carpenter_list),
    path('services/plist',views.Plumber_list),
    path('services/mlist',views.Mason_list),
    path('services/dlist',views.Driver_list),
    path('services/userform',views.user),
    path('services',views.server_list),
    # path('serviced',views.raone),

]
