from django.urls import path

from . import views 

app_name = 'integers'

urlpatterns = [
	path('', views.index)
]