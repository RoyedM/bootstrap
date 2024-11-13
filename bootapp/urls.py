from django.urls import path
from . import views
app_name = 'bootapp'

urlpatterns = [
    path('',views.home, name="home"),
] 